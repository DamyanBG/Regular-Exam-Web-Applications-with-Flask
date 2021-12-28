from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.offers import OfferManager
from models import RoleType
from schemas.request.offers import OfferCreateRequestSchema
from schemas.response.offers import OfferCreateResponseSchema
from utils.decorators import validate_schema, permission_required


class ListCreateOffer(Resource):
    @auth.login_required
    def get(self):
        # TO DO
        offers = OfferManager.get_all()
        schema = OfferCreateResponseSchema()
        return schema.dump(offers, many=True)

    @auth.login_required
    @permission_required(RoleType.worker)
    @validate_schema(OfferCreateRequestSchema)
    def post(self):
        offer = OfferManager.create(request.get_json())
        schema = OfferCreateResponseSchema()
        return schema.dump(offer)


class OfferDetail(Resource):
    def get(self, pk_):
        pass

    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, pk_):
        OfferManager.delete(pk_)
        return {"message": "Success"}, 204

    @auth.login_required
    @permission_required(RoleType.worker)
    @validate_schema(OfferCreateRequestSchema)
    def put(self, pk_):
        updated_offer = OfferManager.update(request.get_json(), pk_)
        schema = OfferCreateResponseSchema()
        return schema.dump(updated_offer)


class AcceptOffer(Resource):
    @auth.login_required
    @permission_required(RoleType.customer)
    def get(self, pk_):
        offer = OfferManager.accept(pk_)
        schema = OfferCreateResponseSchema()
        return schema.dump(offer)


class RefuseOffer(Resource):
    @auth.login_required
    @permission_required(RoleType.customer)
    def get(self, pk_):
        offer = OfferManager.refuse(pk_)
        schema = OfferCreateResponseSchema()
        return schema.dump(offer)
