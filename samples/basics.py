from sense_hat import SenseHat
sense = SenseHat()
# print("Temperature (C): ", round(sense.get_temperature(), 2))
print("{0:<18} {1}".format("Temperature (C):", round(sense.get_temperature(), 2)))

print("{0:<18} {1}".format("Pressure (?):", round(sense.get_pressure(), 2)))
print("{0:<18} {1}".format("Humidity (%):", round(sense.get_humidity(), 2)))
# print("Pressure: ", round(sense.get_pressure(), 2))
# print("Humidity (%):", round(sense.get_humidity(), 2))
