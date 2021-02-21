from app_config import db
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class Device(db.Model):
    device_id = db.Column(db.String, primary_key = True)
    _rev = db.Column(db.Integer)
    device_status = db.Column(db.String)
    recorded_at = db.Column(db.String)
    battery_status = db.Column(db.String)
    location_type = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    device_user = db.Column(db.String)
    
    def __init__(self, device_id, recorded_at):
        self.device_id = device_id
        self.recorded_at = recorded_at
        self._rev = 1
    
    def update_location(self, location_type, longitude, latitude, altitude, recorded_at):
        self.location_type = location_type
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.recorded_at = recorded_at
        self._rev += 1
        db.session.commit()
        return device_schema.dump(self.get_device(self.device_id))
        
    def update_battery_status(self, battery_status, recorded_at):
        self.battery_status = battery_status
        self.recorded_at = recorded_at
        self._rev += 1
        db.session.commit()
        return device_schema.dump(self.get_device(self.device_id))
        
    def update_device_status(self, device_status, recorded_at):
        self.device_status = device_status
        self.recorded_at = recorded_at
        self._rev += 1
        db.session.commit()
        return device_schema.dump(self.get_device(self.device_id))
    
    def update_device_user(self, device_user):
        self.device_user = device_user
        self._rev += 1
        db.session.commit()
        return device_schema.dump(self.get_device(self.device_id))    
        
    def get_location(self):
        return [self.latitude, self.longitude, self.altitude]
            
    def get_battery_status(self):
        return self.battery_status
    
    def get_device_status(self):
        return self.device_status
    
    def get_last_update_time(self):
        return self.recorded_at
    
    @staticmethod
    def get_device(device_id):
        return Device.query.get(device_id)
    
    @staticmethod
    def get_all_devices():
        return Device.query.all()
        
class DeviceSchema(SQLAlchemySchema):
    class Meta:
        model = Device
        
    device_id = auto_field()
    _rev = auto_field()
    device_status = auto_field()
    recorded_at = auto_field()
    battery_status = auto_field()
    location_type = auto_field()
    longitude = auto_field()
    latitude = auto_field()
    longitude = auto_field()
    device_user = auto_field()
    
device_schema = DeviceSchema()