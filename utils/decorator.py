

from functools import wraps
from flask import abort, request
from marshmallow import ValidationError

from schemas import *

def request_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        class_name = func.__qualname__.split(
            '.').pop(0).replace('Resource', 'Schema')

        module = __import__("schemas", fromlist=[])

        Schema = getattr(module, class_name) if hasattr(
            module, class_name) else None

        if not Schema:
            abort(500)

        expression = (
            dict(request.args.items())
            if func.__name__ == "get" else request.get_json()
        )

        schema = Schema()

        try:
            data = schema.load(expression, partial=(func.__name__ == "get" or func.__name__ == "patch"))
        
        except ValidationError: 
            abort(400)

        return func(data, Schema)
            
    return wrapper




