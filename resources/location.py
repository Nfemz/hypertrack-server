from flask_restful import Resource

class LocationResource(Resource):
    def get(self):
        return {'message': 'hi'}, 200