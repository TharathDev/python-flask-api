from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager

from routes import *
from db import engine, Base
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def home():
    return "HELLO"

# Add Blueprint
[
    app.register_blueprint(route)
    for route in globals().values()
    if isinstance(route, Blueprint)
]

with app.app_context():
    Base.metadata.create_all(engine)
