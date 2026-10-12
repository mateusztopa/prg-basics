###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
x = movie.upper()
print(x)
# print title in small letters
x = movie.lower()
print(x)
# print how many times the vowel "e" appears in the title
print(movie.count("e"))

# print where in the text is the word "Lord"
print(movie.find("Lord"))
# print where in the text is the word "dragon"
print(movie.find("dragon"))