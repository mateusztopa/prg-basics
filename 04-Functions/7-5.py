import in_range

number = int(input("A number: "))
check = in_range.is_in_range(number)
if check == True:
    check = 'yes'
else:
    check = 'no'
print(f"Number {number} in the range <2,15>: {check}")