from marshmallow import fields
from marshmallow_enum import EnumField

from models import Status
from schemas.bases import BaseCartSchema


class CartCreateResponseSchema(BaseCartSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    customer_pk = fields.Integer(required=True)
    product_pk = fields.Integer(required=True)
    status = EnumField(Status, by_value=True)
