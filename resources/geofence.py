from flask_restful import Resource

class GeofenceResource(Resource):
    def get(self):
        return {'message': 'hi'}, 200