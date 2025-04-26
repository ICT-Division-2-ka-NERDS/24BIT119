# 24bit119

# Que-7

class Weather:
    def __init__(self):
        self.parameters = []

    def add_parameter(self, parameter):
        """Add a weather parameter to the list."""
        self.parameters.append(parameter)

    def __contains__(self, item):
        """Overload the 'in' operator to check if an item is in the parameters list."""
        return item in self.parameters

    def __str__(self):
        """Return a string representation of the weather parameters."""
        return ', '.join(self.parameters)

weather = Weather()

weather.add_parameter("Temperature: 25°C")
weather.add_parameter("Humidity: 60%")
weather.add_parameter("Wind Speed: 15 km/h")

print("Weather Parameters:", weather)

print("Is 'Temperature: 25°C' in weather parameters?", "Temperature: 25°C" in weather)
print("Is 'Rainfall: 10 mm' in weather parameters?", "Rainfall: 10 mm" in weather) 
