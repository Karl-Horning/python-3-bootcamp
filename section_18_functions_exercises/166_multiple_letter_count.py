# flesh out multiple_letter count:
def multiple_letter_count(word):
    word = word.lower()
    return {l: word.count(l) for l in word}

print(multiple_letter_count("awesome")) # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}