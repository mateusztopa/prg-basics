###
# Calculates the sum of the digits in a number
#
def sum_digits(any_number):
    number = any_number
    sum = 0
    abs(number)
    number_str = str(number)
    for i in number_str:
        number_int = int(i)
        sum += number_int
    return sum


any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')