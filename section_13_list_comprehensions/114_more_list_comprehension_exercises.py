# answer = []

# for num in [1, 2, 3, 4]:
#    if num in [3, 4, 5, 6]:
#       answer.append(num)

answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer)

# answer2 = []

# for name in ['Elie', 'Tim', 'Matt']:
#    answer2.append(name[::-1].lower())

answer2 = [val[::-1].lower() for val in ['Elie', 'Tim', 'Matt']]
print(answer2)