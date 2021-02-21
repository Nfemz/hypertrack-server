from resources.root import RootResource
from resources.device import DeviceResource, DevicesResource
from resources.location import LocationResource
from app_config import api, app, db

db.create_all()
    
api.add_resource(RootResource, '/')
api.add_resource(DeviceResource, '/device/<string:device_id>')
api.add_resource(DevicesResource, '/devices')
api.add_resource(LocationResource, '/locations/<string:device_id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)