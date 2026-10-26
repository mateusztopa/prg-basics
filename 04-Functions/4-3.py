###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

def triangle_area(a,b,c):
    p = (a + b + c) /2 
    s = math.sqrt(p * (p - a) * (p - b) *(p - c))
    return s

print(f'The area of a triangle with sides {a},{b},{c} is {triangle_area(a,b,c)}')
