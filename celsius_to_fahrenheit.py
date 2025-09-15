# Sample list of temperatures in Celsius
celsius_temps = [0, 10, 20, 30, 37, 100]

# Use a lambda function and map to convert to Fahrenheit
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)