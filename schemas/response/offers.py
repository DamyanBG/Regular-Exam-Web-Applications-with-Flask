from marshmallow import fields
from marshmallow_enum import EnumField

from models.enums import State
from schemas.bases import BaseOfferSchema


class OfferCreateResponseSchema(BaseOfferSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    status = EnumField(State, by_value=True)
