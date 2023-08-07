from flask import Flask, Blueprint

from routes import *
from db import engine, Base

app = Flask(__name__)

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
