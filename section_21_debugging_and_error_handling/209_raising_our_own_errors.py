def colourise(text, colour):
   colours = ('cyan', 'yellow', 'blue', 'green', 'magenta')
   if type(colour) is not str:
      raise TypeError('colour must be an instance of str')
   if type(text) is not str:
      raise TypeError('text must be an instance of str')
   if colour not in colours:
      raise ValueError('colour is an invalid colour')
   print(f'Printed {text} in {colour}')

colourise('hello', 'red')
colourise(34, 'red')