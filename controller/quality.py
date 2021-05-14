from flask_restful import Resource, reqparse
from services.service import Service

class Quality(Resource):
    def get(self, quality):
        return Service.get_quality(quality), 200