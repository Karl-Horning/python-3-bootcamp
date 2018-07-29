instructor = {
   'name': 'Colt',
   'owns_dog': True,
   'num_courses': 4,
   'favourite_language': 'Python',
   'is_hilarious': False,
   44: 'My favourite number!'
}

print('name' in instructor) # True
print('awesome' in instructor) # False
print('Colt' in instructor.values()) # True
print('Steele' in instructor.values()) # False
print(instructor.values())