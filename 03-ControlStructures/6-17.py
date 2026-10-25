time_24 = input("Enter time (24-hour format): ")

hour_str = time_24[:2]
minutes = time_24[3:]

hour = int(hour_str)

if hour == 0:
    hour_12 = 12
    period = "am"
elif hour < 12:
    hour_12 = hour
    period = "am"
elif hour == 12:
    hour_12 = 12
    period = "pm"
else:
    hour_12 = hour - 12
    period = "pm"

print(f"Time in 12-hour format: {hour_12}:{minutes}{period}")
