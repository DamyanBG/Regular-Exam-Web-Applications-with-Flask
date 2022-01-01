from marshmallow import fields
from marshmallow_enum import EnumField

from models import Status, Shipped
from schemas.bases import BaseCartSchema, BaseCartCloseSchema


class CartCreateResponseSchema(BaseCartSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    customer_pk = fields.Integer(required=True)
    product_pk = fields.Integer(required=True)
    status = EnumField(Status, by_value=True)


class CartResponseSchema(BaseCartCloseSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    customer_pk = fields.Integer(required=True)
    product_pk = fields.Integer(required=True)
    status = EnumField(Status, by_value=True)
    quantity = fields.Integer(required=True)
    shipped = EnumField(Shipped, by_value=True)
