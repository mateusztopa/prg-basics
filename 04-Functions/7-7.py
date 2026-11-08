def f(binary_number):
    for char in binary_number:
        if char != '1' and char != '0':
            return False
    return True
number = str(input("Enter number: "))
result = f(number)
print(f"{result}")