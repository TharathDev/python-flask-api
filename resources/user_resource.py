from flask import make_response, request
from flask_restful import Resource

from db import session
from models import UserModel
from schemas import UserSchema


class UserResource(Resource):
    def get(self):
        expressions = dict(request.args.items())
        user_model = UserModel()
        users = user_model.get_all(expressions)
        users_json = user_model.jsonify(users, UserSchema, many=True)
        return make_response({"user": users_json}, 200)

    def post(self):
        user = request.get_json()
        user_model = UserModel(user)
        user_model.add()
        user_schema = UserSchema()
        users_json = user_schema.dump(user_model)
        return make_response(users_json, 201)
