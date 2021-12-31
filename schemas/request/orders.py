from marshmallow import fields

from schemas.bases import BaseOrderSchema


class OrderCreateRequestSchema(BaseOrderSchema):
    stl = fields.String(required=True)


class OrderUpdateRequestSchema(BaseOrderSchema):
    stl_url = fields.String(required=True)
