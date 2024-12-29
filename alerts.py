import warnings
class PowerError(Exception):
    pass
class WaterLevelWarning(Warning):
    pass

def power_outage_detected(outage_detected):
    if outage_detected:
        raise PowerError('A power outage has been detected somewhere in the system')
    else:
        print('All systems receiving power')

def water_levels_check(liters):
    if liters < 200:
        warnings.warn('Water levels have fallen below 200 liters', WaterLevelWarning)
    else:
        print('Water levels are adequate')

outage_detected = False
liters = 200

power_outage_detected(outage_detected)
water_levels_check(liters)

#The code provided demonstrates custom exception handling and warnings in Python. Here's a breakdown of the key concepts:
#1. **Custom Exception**: The `PowerError` class is a custom exception that inherits from Python's built-in `Exception` 
# class. It's used to signal a specific error condition related to power outages.
#2. **Custom Warning**: The `WaterLevelWarning` class is a custom warning that inherits from Python's built-in `Warning` 
# class. It's used to issue a warning when water levels fall below a certain threshold.
#3. **Raising Exceptions**: The `power_outage_detected` function raises a `PowerError` if a power outage is detected 
# (`outage_detected` is `True`). Otherwise, it prints a message indicating that all systems are receiving power.
#4. **Issuing Warnings**: The `water_levels_check` function uses the `warnings.warn` method to issue a `WaterLevelWarning` 
# if the water level is below 200 liters. Otherwise, it prints a message indicating that water levels are adequate.
#5. **Function Calls**: The `power_outage_detected` and `water_levels_check` functions are called with the variables 
# `outage_detected` and `liters`, respectively, to check the system's status.
#This code helps manage specific error and warning conditions in a system, allowing for appropriate responses to power 
# outages and low water levels.