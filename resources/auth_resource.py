from flask import make_response

from models import UserModel
from .base_resource import BaseResource


class AuthResource(BaseResource):
    def post(self, user, Schema):
        return make_response({"message":"logged in"}, 201)

    def delete(self, user, Schema):
        return make_response({"message":"logged out"}, 201)