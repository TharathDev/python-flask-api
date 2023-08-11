from flask import make_response
from passlib.hash import sha256_crypt

from models import UserModel
from .base_resource import BaseResource


class UserResource(BaseResource):
    def get(self, expression={}, Schema={}):
        user_model = UserModel()
        users = user_model.get_all(expression)
        users_json = user_model.jsonify(users, Schema, many=True)
        return make_response({"user": users_json}, 200)

    def post(self, user, Schema):
        user_model = UserModel(user)
        if hasattr(user, 'email'):
            # Replace password with its hashed value using sha256_crypt
            user.email = sha256_crypt(user.email.encode()).hexdigest()

        print(user)
        user_model.add()
        users_json = user_model.jsonify(Schema=Schema)
        return make_response(users_json, 201)

    def put(self, user, Schema):
        user_model = UserModel(user)
        user_model.update()
        # users_json = user_model.jsonify(Schema=Schema)
        return make_response("updated", 201)