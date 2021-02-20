from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

device_status_history = []
location_history = []
geofence_history = []
battery_history = []

class Webhook(Resource):
    def get(self):
        return {
            'message': 'Welcome to the root level of the hypertrack test server',
            "/": {
                "GET": "Returns the root directory with documentation",
                "POST": "Webhook endpoint to receive incoming data from HyperTrack"
                },
            "/deviceStatus": {
                "GET": "Returns history object of all device status updates received"
                },
            "/location": {
                'GET': "Returns history object of all location updates received"
                },
            "/geofence": {
                "GET": "Returns history object of all geofence updates received"
                },
            "/battery": {
                "GET": "Returns history object of all battery updates received"
                }
                }, 200
    def post(self):
        data = request.json
        print(data)
        for item in data:
            if (item['type'] == 'device_status'):
                device_status_history.append(item)
            elif (item['type'] == 'location'):
                location_history.append(item)
            elif (item['type'] == 'geofence'):
                geofence_history.append(item)
            elif (item['type'] == 'battery'):
                battery_history.append(item)
            else:
                return {'message': 'Invalid data received'}, 400
        
        return {'message': 'data posted correctly'}, 201
class DeviceStatus(Resource):
    def get(self):
        return device_status_history, 200

class Location(Resource):
    def get(self):
        return location_history, 200

class GeoFence(Resource):
    def get(self):
        return geofence_history, 200

class Battery(Resource):
    def get(self):
        return battery_history, 200
    
api.add_resource(Webhook, '/')
api.add_resource(DeviceStatus, '/deviceStatus')
api.add_resource(Location, '/location')
api.add_resource(GeoFence, '/geofence')
api.add_resource(Battery, '/battery')

if __name__ == '__main__':
    app.run(port=5000, debug=True)