import calculations
text = str(input("Enter text: "))
letter = str(input("Enter letter: "))

result = calculations.how_many(text,letter)
print(f"the number of letter '{letter}': {result}")