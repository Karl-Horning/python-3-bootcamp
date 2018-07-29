#define single_letter_count below:
# def single_letter_count(word, letter):
#    word = list(word.lower())
#    letter = letter.lower()
#    count = 0
#    for l in word:
#       if l == letter:
#          count += 1
#    return count

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l")) # 3