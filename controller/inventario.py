from flask_restful import Resource, reqparse
from services.service import Service


class Inventario(Resource):
    
    def get(self):
        return Service.get_inventario(), 200