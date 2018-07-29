def is_all_strings(collection):
   return all(isinstance(i, str) for i in collection)

print(is_all_strings(['a', 'b', 'c'])) # True
print(is_all_strings([2, 'a', 'b', 'c'])) # False
print(is_all_strings(['hello', 'goodbye'])) # True