from resources.battery import BatteryResource
from resources.geofence import GeofenceResource
from resources.location import LocationResource
from resources.device_status import DeviceStatusResource
from resources.root import RootResource
from app_config import api, app

    
api.add_resource(RootResource, '/')
api.add_resource(DeviceStatusResource, '/deviceStatus')
api.add_resource(LocationResource, '/location')
api.add_resource(GeofenceResource, '/geofence')
api.add_resource(BatteryResource, '/battery')

if __name__ == '__main__':
    app.run(port=5000, debug=True)