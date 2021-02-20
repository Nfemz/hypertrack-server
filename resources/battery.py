from flask_restful import Resource
from app_config import db
from models.battery import BatteryStatus, battery_status_schema 

class BatteryResource(Resource):
    def get(self):
        result = db.session.query(BatteryStatus).all()
        print(battery_status_schema.dump(result[0]))
        return battery_status_schema.dump(result[0])