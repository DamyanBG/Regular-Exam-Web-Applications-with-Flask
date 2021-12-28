from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class BaseOrderSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=100))
    description = fields.String(required=True, validate=validate.Length(max=255))
    address = fields.String(required=True, validate=validate.Length(max=255))