from flask_restful import Resource, reqparse
from services.service import Service

class Sell_in(Resource):
    def get(self, sell_in):
        return Service.get_sell_in(sell_in), 200
