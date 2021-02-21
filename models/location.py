from app_config import db
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String)
    recorded_at = db.Column(db.String)
    location_type = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    
    def __init__(self, device_id, recorded_at, location_type, longitude, latitude, altitude):
        self.device_id = device_id
        self.recorded_at = recorded_at
        self.location_type = location_type
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        
    @staticmethod
    def get_locations_by_device_id(device_id_search):
        return db.session.query(Location).filter_by(device_id = device_id_search)

class LocationSchema(SQLAlchemySchema):
    class Meta:
        model = Location
    
    id = auto_field()
    device_id = auto_field()
    recorded_at = auto_field()
    location_type = auto_field()
    longitude = auto_field()
    latitude = auto_field()
    altitude = auto_field() 
    
location_schema = LocationSchema()