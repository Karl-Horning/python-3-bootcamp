# clear
d = dict(a=1, b=2, c=3)
d.clear()
print(d) # {}

# copy
d = dict(a=1, b=2, c=3)
c = d.copy()
print(c) # {'a': 1, 'b': 2, 'c': 3}
c == d # True
c is d # False

# fromkeys
# Creates key-value pairs from comma separated values

{}.fromkeys('a', 'b') # { 'a': 'b' }
{}.fromkeys(['email'], 'unknown') # { 'email': 'unknown' }
{}.fromkeys('a', [1, 2, 3, 4, 5]) # { 'a': [1, 2, 3, 4, 5] }

new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user) # {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}

# get
d = dict(a=1, b=2, c=3)
print(d['a']) # 1
print(d.get('a')) # 1
print(d['b']) # 2
print(d.get('b')) # 2
# print(d['no_key']) # KeyError
print(d.get('no_key')) # None

# pop
instructor = {
   'name': 'Colt',
   'owns_dog': True,
   'num_courses': 4,
   'favourite_language': 'Python',
   'is_hilarious': False,
   44: 'My favourite number!'
}
instructor.pop('owns_dog') # True
print(instructor)

# popitem
# Removes a random item
d = dict(a=1, b=2, c=3, d=4, e=5)
d.popitem()
print(d)

# update
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

second['a'] = 'Amazing'
print(second)