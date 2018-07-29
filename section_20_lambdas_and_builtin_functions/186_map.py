nums = [2,4,6,8,10]
people = ['Darcy', 'Christina', 'Dana', 'Annabel']
names = [
   {'first': 'Rusty', 'last': 'Steele'},
   {'first': 'Colt', 'last': 'Steele'},
   {'first': 'Blue', 'last': 'Steele'}
]

doubles = list(map(lambda x: x*2, nums))
peeps = list(map(lambda name: name.upper(), people))
first_names = list(map(lambda x: x['first'], names))

print(doubles)
print(peeps)
print(first_names)