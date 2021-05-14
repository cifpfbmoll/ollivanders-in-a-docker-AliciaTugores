from flask_restful import Resource


class Wellcome(Resource):
    def get(self):
        return {"Wellcome": "to Ollivanders"}
