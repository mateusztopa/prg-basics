###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input("Enter temperature: "))
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot")
elif temperature <= 30 and temperature >= 15:
    print("It is warm")
elif temperature < 15 and temperature >= 0:
    print("it is cold")
elif temperature < 0:
    print(f"Worning, frost")
