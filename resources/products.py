from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.products import ProductsManager
from models import RoleType
from schemas.request.products import ProductCreateRequestSchema
from schemas.response.products import ProductCreateResponseSchema
from utils.decorators import permission_required, validate_schema


class ListCreateDeleteUpdateProduct(Resource):
    @auth.login_required
    def get(self):
        # TO DO
        products = ProductsManager.get_all()
        schema = ProductCreateResponseSchema()
        return schema.dump(products, many=True)

    @auth.login_required
    @permission_required(RoleType.worker)
    @validate_schema(ProductCreateRequestSchema)
    def post(self):
        product = ProductsManager.create(request.get_json())
        schema = ProductCreateResponseSchema()
        return schema.dump(product), 201

    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, pk_):
        ProductsManager.delete(pk_)
        return {"message": "Success"}, 204

    @auth.login_required
    @permission_required(RoleType.worker)
    @validate_schema(ProductCreateRequestSchema)
    def put(self, pk_):
        updated_product = ProductsManager.update(request.get_json(), pk_)
        schema = ProductCreateResponseSchema()
        return schema.dump(updated_product)