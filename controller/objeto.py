from flask_restful import Resource, reqparse
from services.service import Service


class Objeto(Resource):
    
    def get(self, name):
        # curl http://localhost:5000/objeto/"Aged%20Brie"
        return Service.get_objeto(name), 200

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='name required')
        parser.add_argument('sell_in', type=int, required=True,
                            help='sellIn required')
        parser.add_argument('quality', type=int, required=True,
                            help='quality required')
        return parser.parse_args()

    def post(self):
        args = self.parseRequest()     
        return Service.post_objeto(args), 201

    def delete(self):
        args = self.parseRequest()     
        return Service.delete_objeto(args), 200