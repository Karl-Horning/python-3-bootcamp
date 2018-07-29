# Custom For Loop
# for num in [1, 2, 3]
# for chr in 'hi there'

def my_for(iterable, func):
   iterable = iter(iterable)
   while True:
      try:
         i = next(iterable)
      except StopIteration:
         break
      else:
         func(i)

def square(x):
   print(x * x)

# my_for('hello', print)
my_for([1, 2, 3, 4], square)