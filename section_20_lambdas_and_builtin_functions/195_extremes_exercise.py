def extremes(collection):
   return (min(collection), max(collection))

print(extremes([1,2,3,4,5])) # (1, 5)
print(extremes([99,25,30,-7])) # (-7, 99)
print(extremes('alcatraz')) # ('a', 'z')