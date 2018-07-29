# total = 0

# def increment():
#    total += 1
#    return total

# increment() # Error

# Using global scope
total = 0

def increment():
   global total
   total += 1
   return total

increment() # 1

# nonlocal let's us modify a parent's variables in a child (aka nested) function
def outer():
   count = 0
   def inner():
      nonlocal count
      count += 1
      return count
   return inner()