from models.device import Device, device_schema
from flask_restful import Resource
import json

class DeviceResource(Resource):
    def get(self, device_id):
        device = Device.get_device(device_id)
        return json.loads(device_schema.dumps(device)), 200
    

    
class DevicesResource(Resource):
    def get(self):
        devices = Device.get_all_devices()
        result = []
        if devices:
            for device in devices:
                result.append(json.loads(device_schema.dumps(device)))
        return result, 200