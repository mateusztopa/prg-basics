#fee calculator
hours = int(input("Enter hours: "))
fee = 0
for i in range(1, hours + 1):
    if i == 1 or i == 2:
        fee += 5
    elif i == 3 or i == 4 or i == 5 or i == 6:
        fee += 15
    else:
        fee += 20

print(f"fee: {fee} PLN")