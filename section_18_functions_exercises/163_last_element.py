'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

# def last_element(l):
#    if not l:
#       return None
#    return l[-1]

def last_element(l):
   if l:
      return l[-1]
   return None

print(last_element([1, 2, 3]))