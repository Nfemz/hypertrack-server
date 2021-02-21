from flask_restful import Resource
from flask import request
from utils import handleBatteryUpdate, handleDeviceStatusUpdate, handleLocationUpdate, addLocationPoint

class RootResource(Resource):
    def get(self):
        return {
            'message': 'Welcome to the root level of the hypertrack test server',
            "/": {
                "GET": "Returns the root directory with documentation",
                "POST": "Webhook endpoint to receive incoming data from HyperTrack"
                },
            "/device/:device_id": {
                "GET": "Returns the most up to date info on the device",
                "POST": "Updates the device document"
            },
            "/devices": {
                "GET": "Returns all devices"
            },
            "locations/:device_id": {
                "GET": "Returns the history of all location updates on the device"
            }
        }
        
    def post(self):
        data = request.json
        for item in data:
            if (item['type'] == 'device_status'):
                handleDeviceStatusUpdate(item)
                
            elif (item['type'] == 'location'):
                handleLocationUpdate(item)
                addLocationPoint(item)
            elif (item['type'] == 'battery'):
                handleBatteryUpdate(item)
        
        return {'update_body': data}, 201