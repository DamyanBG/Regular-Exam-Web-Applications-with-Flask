from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.cart import CartManager
from models import RoleType
from schemas.request.cart import CartCreateRequestSchema
from schemas.response.cart import CartCreateResponseSchema
from utils.decorators import permission_required, validate_schema


class CreateCart(Resource):
    @auth.login_required
    @permission_required(RoleType.customer)
    @validate_schema(CartCreateRequestSchema)
    def post(self, pk_):
        current_user = auth.current_user()
        cart = CartManager.create(request.get_json(), pk_, current_user.pk)
        schema = CartCreateResponseSchema()
        return schema.dump(cart), 201

    @auth.login_required
    @permission_required(RoleType.customer)
    @validate_schema(CartCreateRequestSchema)
    def put(self, pk_):
        current_user = auth.current_user()
        cart = CartManager.update(request.get_json(), pk_, current_user.pk)
        schema = CartCreateResponseSchema()
        return schema.dump(cart), 201


class CloseListCart(Resource):
    @auth.login_required
    @permission_required(RoleType.customer)
    def put(self):
        current_user = auth.current_user()
        cart = CartManager.finish(current_user.pk)
        return cart

    @auth.login_required
    @permission_required(RoleType.customer)
    def get(self):
        # TO DO
        current_user = auth.current_user()
        cart = CartManager.get_your_cart(current_user.pk)
        schema = CartCreateResponseSchema()
        return schema.dump(cart, many=True)


class ListCartForWorkers(Resource):
    @auth.login_required
    @permission_required(RoleType.worker)
    def get(self):
        cart = CartManager.get_all()
        schema = CartCreateResponseSchema()
        return schema.dump(cart, many=True)


