from flask_restful import Resource
from flask import request
from models.battery import BatteryStatus
from app_config import db

class RootResource(Resource):
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
        for item in data:
            if (item['type'] == 'device_status'):
                print('hi')
            elif (item['type'] == 'location'):
                print('hi')
            elif (item['type'] == 'geofence'):
                print('hi')
            elif (item['type'] == 'battery'):
                device_status_item = BatteryStatus(item['data']['value'], item['recorded_at'])
                db.session.add(device_status_item)
                db.session.commit()
            else:
                return {'message': 'Invalid data received'}, 400
        
        return {'message': 'data posted correctly'}, 201