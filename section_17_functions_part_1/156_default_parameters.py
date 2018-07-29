def exponent(num, power=2):
   return num ** power

print(exponent(2,3))
print(exponent(3))
print(exponent(7))

def add(a, b):
   return a + b

def math(a, b, fn=add):
   return fn(a, b)

def subtract(a, b):
   return a - b

print(math(2, 2)) # 4
print(math(2, 2, subtract)) # 0