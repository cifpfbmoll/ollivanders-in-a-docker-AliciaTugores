from flask import Flask
from flask_restful import Resource, Api
from controller.objeto import Objeto
from controller.wellcome import Wellcome
from controller.sell_in import Sell_in
from controller.quality import Quality
from controller.inventario import Inventario
from repository.db import *

def create_app():

    app = Flask(__name__)
    db.init_app(app)

    with app.app_context():
        init_db()

    api = Api(app)
    api.add_resource(Wellcome, "/")
    api.add_resource(Inventario, "/inventory")
    api.add_resource(Objeto, "/objeto/name/<name>", "/objeto")
    api.add_resource(Sell_in, "/objeto/sellin/<sell_in>")
    api.add_resource(Quality, "/objeto/quality/<quality>")
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug = True)