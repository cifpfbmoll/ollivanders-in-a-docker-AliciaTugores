from flask import Flask
from flask_restful import Resource, Api
from controller.wellcome import Wellcome
from controller.objeto import Objeto
from repository.db import *


def create_app():

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Wellcome, "/")
    api.add_resource(Objeto, "/objeto/<name>")

    return app
