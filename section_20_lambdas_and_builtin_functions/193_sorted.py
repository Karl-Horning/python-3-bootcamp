# sorted (works on anything that is iterable)

# EXAMPLE 1:
more_numbers = [6,1,8,2]
sorted(more_numbers) # [1, 2, 6, 8]
print(more_numbers) # [6, 1, 8, 2]

# EXAMPLE 2:
users = [
   {'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']},
   {'username': 'katie', 'tweets': ['I love my cat']},
   {'username': 'jeff', 'tweets': []},
   {'username': 'bob123', 'tweets': [], 'num': 10, 'colour': 'teal'},
   {'username': 'doggo_luvr', 'tweets': ['dogs are the best', 'I\'m hungry']},
   {'username': 'guitar_gal', 'tweets': []}
]

# print(sorted(users, key=len))
# print(sorted(users, key=lambda user: user['username']))
print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))

# EXAMPLE 3:
songs = [
   {'title': 'happy birthday', 'playcount': 1},
   {'title': 'Survive', 'playcount': 6},
   {'title': 'YMCA', 'playcount': 99},
   {'title': 'Toxic', 'playcount': 31}
]

print(sorted(songs, key=lambda s: s['playcount'], reverse=True))