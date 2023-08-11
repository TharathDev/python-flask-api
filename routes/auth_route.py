from flask import Blueprint
from flask_restful import Api

from resources import AuthResource

authRoute = Blueprint("auth_route", __name__)

api = Api(authRoute)

api.add_resource(AuthResource, "/auth")
