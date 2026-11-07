
def month(h):
    months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if h == 1:
        month_return = months[0]
    else:
        month_return = months[h - 1]
    return month_return