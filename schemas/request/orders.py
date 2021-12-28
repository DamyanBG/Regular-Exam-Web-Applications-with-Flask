from marshmallow import fields
from schemas.bases import BaseOrderSchema


class OrderCreateRequestSchema(BaseOrderSchema):
    stl = fields.String(required=True)
