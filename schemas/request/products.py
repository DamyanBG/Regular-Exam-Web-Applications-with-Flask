from marshmallow import fields

from schemas.bases import BaseProductSchema


class ProductCreateRequestSchema(BaseProductSchema):
    photo = fields.String(required=True)
    photo_extension = fields.String(required=True)


class ProductUpdateRequestSchema(BaseProductSchema):
    photo_url = fields.String(required=True)
