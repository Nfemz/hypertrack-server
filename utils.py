from models.device import Device
from models.location import Location
from app_config import db

def addLocationPoint(item):
    device_id = item['device_id']
    recorded_at = item['recorded_at']
    data = item['data']
    geometry = data['geometry']
    
    location_type = geometry['type']
    longitude = geometry['coordinates'][0]
    latitude = geometry['coordinates'][1]
    altitude = geometry['coordinates'][2]
    
    location = Location(device_id, recorded_at, location_type, longitude, latitude, altitude)
    db.session.add(location)

def handleLocationUpdate(item):
    device = Device.get_device(item['device_id'])
    if not device:
        device = Device(item['device_id'], item['recorded_at'])
        db.session.add(device)
    
    recorded_at = item['recorded_at']
    data = item['data']
    geometry = data['geometry']
    
    location_type = geometry['type']
    longitude = geometry['coordinates'][0]
    latitude = geometry['coordinates'][1]
    altitude = geometry['coordinates'][2]
    
    return device.update_location(location_type, longitude, latitude, altitude, recorded_at)

def handleDeviceStatusUpdate(item):
    device = Device.get_device(item['device_id'])
    if not device:
        device = Device(item['device_id'], item['recorded_at'])
        db.session.add(device)
    
    device_status = item['data']['value']
    recorded_at = item['recorded_at']
    return device.update_device_status(device_status, recorded_at)

def handleBatteryUpdate(item):
    device = Device.get_device(item['device_id'])
    if not device:
        device = Device(item['device_id'], item['recorded_at'])
        db.session.add(device)
        
    battery_status = item['data']['value']
    recorded_at = item['recorded_at']
    
    return device.update_battery_status(battery_status, recorded_at)