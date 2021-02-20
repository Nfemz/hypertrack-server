from app_config import db
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class BatteryStatus(db.Model):
    __tablename__ = "battery"
    id = db.Column(db.Integer, primary_key=True)
    battery_status = db.Column(db.String)
    recorded_at = db.Column(db.String)
    
    def __init__(self, battery_status, recorded_at):
        self.battery_status = battery_status
        self.recorded_at = recorded_at
        

class BatteryStatusSchema(SQLAlchemySchema):
    class Meta:
        model = BatteryStatus
        
    id = auto_field()
    battery_status = auto_field()
    recorded_at = auto_field()
    
battery_status_schema = BatteryStatusSchema()