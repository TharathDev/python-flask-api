from flask import Blueprint
from flask_restful import Api

from resources import UserResource

userRoute = Blueprint("user_route", __name__)

api = Api(userRoute)

api.add_resource(UserResource, "/users")
