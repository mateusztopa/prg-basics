def how_many(sentence,letter):
    text = sentence
    total = 0
    for char in text:
        if char == letter:
            total += 1
    return total