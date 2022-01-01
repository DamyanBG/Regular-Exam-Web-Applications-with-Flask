from marshmallow import fields, validate

from schemas.bases import BaseProductSchema


class ProductCreateResponseSchema(BaseProductSchema):
    pk = fields.Integer(required=True)
    photo_url = fields.String(required=True, validate=validate.Length(max=255))
    create_on = fields.DateTime(required=True)
