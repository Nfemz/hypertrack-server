from models.location import Location, location_schema
from flask_restful import Resource
import json

class LocationResource(Resource):
    def get(self, device_id):
        locations = Location.get_locations_by_device_id(device_id)
        result = []
        if locations:
            for location in locations:
                result.append(json.loads(location_schema.dumps(location)))
        return result, 200