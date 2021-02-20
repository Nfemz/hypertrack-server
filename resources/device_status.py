from flask_restful import Resource

class DeviceStatusResource(Resource):
    def get(self):
        return {'message': 'hi'}, 200