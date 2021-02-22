from models.device import Device, device_schema
from flask_restful import Resource
from flask import request
import json
from utils import handleDeviceUserUpdate, handleUpdateDeviceStatusOnly

class DeviceResource(Resource):
    def get(self, device_id):
        device = Device.get_device(device_id)
        return json.loads(device_schema.dumps(device)), 200
    
    def post(self, device_id):
        data = request.json
        if 'device_user' in data:
            handleDeviceUserUpdate(data['device_user'], device_id)
        if 'device_status' in data:
            handleUpdateDeviceStatusOnly(data['device_status'], device_id)
        return {'update_body': data}, 201

    
class DevicesResource(Resource):
    def get(self):
        devices = Device.get_all_devices()
        result = []
        if devices:
            for device in devices:
                result.append(json.loads(device_schema.dumps(device)))
        return result, 200