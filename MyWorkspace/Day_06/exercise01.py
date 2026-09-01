class SmartThermostat():
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0
    def __init__(self,appliance_name,initial_temp):
        __appliance_name = appliance_name