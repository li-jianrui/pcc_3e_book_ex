def vehicles(maker, model, **vehicle_info):
    """Build a dictionary containing everything we know about a vehicle."""
    vehicle_info['maker'] = maker
    vehicle_info['model'] = model
    return vehicle_info

vehicle1 = vehicles('subaru', 'outback', color='blue', tow_package=True)
vehicle2 = vehicles('tesla', 'model s', color='red', autopilot=True)
print(vehicle1)
print(vehicle2)