from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.orders import OrdersManager
from models.enums import RoleType
from schemas.request.orders import OrderCreateRequestSchema
from schemas.response.orders import OrderCreateResponseSchema
from utils.decorators import validate_schema, permission_required


class ListCreateOrder(Resource):
    @auth.login_required
    def get(self):
        # TO DO
        orders = OrdersManager.get_all()
        schema = OrderCreateResponseSchema()
        return schema.dump(orders, many=True)

    @auth.login_required
    @permission_required(RoleType.customer)
    @validate_schema(OrderCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        order = OrdersManager.create(request.get_json(), current_user.pk)
        schema = OrderCreateResponseSchema()
        return schema.dump(order)


class OrderDetail(Resource):
    def get(self, pk_):
        pass

    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, pk_):
        OrdersManager.delete(pk_)
        return {"message": "Success"}, 204

    @auth.login_required
    @permission_required(RoleType.customer)
    @validate_schema(OrderCreateRequestSchema)
    def put(self, pk_):
        updated_order = OrdersManager.update(request.get_json(), pk_)
        schema = OrderCreateResponseSchema()
        return schema.dump(updated_order)
