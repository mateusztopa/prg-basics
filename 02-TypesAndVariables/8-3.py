###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

#getting the value in Clesius
Celsius = float(input("write temperature in Celsius: "))
#calculating value in Celsus into values in Fahrenheit and Kelvin
Kelvin = (Celsius + 273.15)
Fahrenheit = (Celsius * 1.8) + 32
#printing the results
print(f"temperature in:\nKelvin: {round(Kelvin)}\nin Fahrenheit{round(Fahrenheit)}")