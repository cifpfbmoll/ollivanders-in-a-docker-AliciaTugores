from flask_restful import fields, marshal_with, abort
from repository.db import *
from domain.types import *

class Service:

    resource_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    @staticmethod
    @marshal_with(resource_fields)
    def get_objeto(name):

        if not name:
            abort(404, message="Es necesario el nombre del item")

        item = get_objeto(name)

        if not item:
            abort(404, message="El item {} no existe".format(name))

        return item

    @staticmethod
    @marshal_with(resource_fields)
    def get_sell_in(sell_in):
        if not sell_in:
            abort(404, message="Es necesario el nombre del item")

        item = get_sell_in(sell_in)

        if not item:
            abort(404, message="El item con sell_in {} no existe".format(sell_in))

        return item

    @staticmethod
    @marshal_with(resource_fields)
    def get_quality(quality):
        if not quality:
            abort(404, message="Es necesario el nombre del item")

        item = get_quality(quality)

        if not item:
            abort(404, message="El item con quality {} no existe".format(quality))

        return item

    
    @staticmethod
    @marshal_with(resource_fields)
    def get_inventario():

        item = get_inventario()

        if not item:
            abort(404, message="No hay items en el inventario")

        return item


    @staticmethod
    def post_objeto(args):
        item = post_objeto(args)
        return item

    @staticmethod
    def delete_objeto(args):
        item = delete_objeto(args)
        return item