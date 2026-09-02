class SmartThermostat():
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0
    def __init__(self,appliance_name,initial_temp):
        self.__appliance_name = self.appliance_name
        print(appliance_name)

thermostat = SmartThermostat("Living Room AC", 24.0)
print(thermostat.__appliance_name)  # Output: Living Room AC
print(thermostat.target_temp)     # Output: 24.0

thermostat.target_temp = 28.0     # Updates successfully
print(thermostat.target_temp)     # Output: 28.0

try:
    thermostat.target_temp = 5.0  # Out of range!
except ValueError as e:
    print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.
