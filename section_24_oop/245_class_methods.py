class User:
   active_users = 0

   def __init__(self, first, last, age):
      self.first = first
      self.last = last
      self.age = age
      User.active_users += 1

   def logout(self):
      User.active_users -= 1
      print(f'{self.first} has logged out')

   def full_name(self):
      return f'{self.first} {self.last}'

   def initials(self):
      return f'{self.first[0]}.{self.last[0]}.'

   def likes(self, thing):
      return f'{self.first} likes {thing}'

   def is_senior(self):
      return self.age >= 65

   def birthday(self):
      self.age += 1
      return f'Happy {self.age}th, {self.first}'

   @classmethod
   def display_active_users(cls):
      return f'There are currently {cls.active_users} active users'

   @classmethod
   def from_string(cls, data_str):
      first, last, age = data_str.split(',')
      return cls(first, last, int(age))

user1 = User('Joe', 'Smith', 68)
user2 = User('Blanca', 'Lopez', 41)

dave = User.from_string('Dave,Biggins,41')

print(dave.first)
print(dave.full_name())