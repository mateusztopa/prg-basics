import random

def random_numbers_generator(a,b):
    result = random.randint(a,b)
    return result

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(random_numbers_generator(first_number,second_number))