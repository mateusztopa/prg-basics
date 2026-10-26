a = input("Enter hours: ")
b = input("Enter minutes: ")
c = input("Enter time format: ")

def time_string(hours, minutes, time_format):
    result = ''
    if time_format == 24:
        result = hours + ':' + minutes
    elif time_format == 12:
        if hours == 0:
            hours = 12
            period = 'am'
        elif hours <= 12:
            period = 'am'
        else:
            hours = hours - 12
            period = 'pm'
        result = hours + ':' + minutes + period
    return result

time = time_string(a,b,c)
print(time)