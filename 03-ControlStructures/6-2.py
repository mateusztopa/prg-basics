###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
letter_number = 0
# Count vowels in the text
while letter_number < len(text):
    char = text[letter_number]
    if char in vowels:
        vowel_count += 1
    letter_number =+ 1
print(f"The number of vowels in the text is: {vowel_count}")
