from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    email = fields.Email()
    phone = fields.Integer()
