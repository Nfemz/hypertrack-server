from resources.root import RootResource
from resources.device import DeviceResource, DevicesResource
from resources.location import LocationResource
from app_config import api, app, db
    
api.add_resource(RootResource, '/')
api.add_resource(DeviceResource, '/device/<string:device_id>')
api.add_resource(DevicesResource, '/devices')
api.add_resource(LocationResource, '/locations/<string:device_id>')

db.create_all()

if __name__ == '__main__':
    app.run(port=5000, debug=True)