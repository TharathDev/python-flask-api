from flask_restful import Resource

from utils import request_validator

class BaseResource(Resource):
    method_decorators = [request_validator]