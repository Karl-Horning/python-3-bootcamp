class Mother:
   def __init__(self):
      self.eye_colour = 'brown'
      self.hair_colour = 'dark brown'
      self.hair_type = 'curly'

class Father:
   def __init__(self):
      self.eye_colour = 'blue'
      self.hair_colour = 'blond'
      self.hair_type = 'straight'

class Child(Mother, Father):
   pass