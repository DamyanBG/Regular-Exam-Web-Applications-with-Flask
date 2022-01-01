from marshmallow import fields

from schemas.bases import BaseCartSchema, BaseCartCloseSchema


class CartCreateRequestSchema(BaseCartSchema):
    pass


class CartCloseRequestSchema(BaseCartCloseSchema):
    pass
