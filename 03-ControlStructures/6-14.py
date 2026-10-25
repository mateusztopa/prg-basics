facebook = False
twitter = True
instagram = True
good_influncer = 0
if facebook:
    good_influncer += 1
if twitter:
    good_influncer += 1
if instagram:
    good_influncer += 1
if good_influncer >= 2:
    print("You are a good influencer!")