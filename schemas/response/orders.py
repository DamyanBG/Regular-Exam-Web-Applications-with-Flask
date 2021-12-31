from marshmallow import fields, validate

from schemas.bases import BaseOrderSchema


class OrderCreateResponseSchema(BaseOrderSchema):
    pk = fields.Integer(required=True)
    stl_url = fields.String(required=True, validate=validate.Length(max=255))
    create_on = fields.DateTime(required=True)
    customer_pk = fields.Integer()
