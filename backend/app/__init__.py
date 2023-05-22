from flask import Flask, jsonify
from flask_cors import CORS

from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    CORS(app, resources={r'/*': {'origins':'*'}})
    configure_blueprint(app, bp)

    return app

def configure_blueprint(app, blueprint):
    app.register_blueprint(blueprint)