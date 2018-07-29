# __mro__ attribute on the class
# use the mro() method on the class
# use the builtin help(cls) method

class A:
   def do_something(self):
      print('Method Defined in: A')

class B(A):
   def do_something(self):
      print('Method Defined in: B')

class C(A):
   def do_something(self):
      print('Method Defined in: C')

class D(B, C):
   pass
   # def do_something(self):
   #    print('Method Defined in: D')

# print(D.__mro__)
# print(D.mro())
help(D)
# thing = D()
# thing.do_something()

#       A
#    /    \
#   B     C
#   \    /
#     D

# D, C, A, Object