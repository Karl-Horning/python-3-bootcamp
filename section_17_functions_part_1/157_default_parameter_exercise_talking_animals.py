# Define speak below:
# def speak(animal='dog'):
#    if animal == 'pig':
#       return 'oink'
#    elif animal == 'duck':
#       return 'quack'
#    elif animal == 'cat':
#       return 'meow'
#    elif animal == 'dog':
#       return 'woof'
#    return '?'

def speak(animal='dog'):
   noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
   return noises.get(animal, '?')

print(speak('cat'))
print(speak('dog'))
print(speak('monkey'))