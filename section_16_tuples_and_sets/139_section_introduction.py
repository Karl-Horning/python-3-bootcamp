# Tuples are commonly used for UNCHANGING data
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
   print(month)

i = len(months) - 1
while i >= 0:
   print(months[i])
   i -= 1

# Tuples can be used as keys in dictionaries
locations = {
   (35.6895, 39.6917): 'Tokyo Office',
   (40.7128, 74.0060): 'New York Office',
   (37.7749, 122.4194): 'San Francisco Office'
}

cat = {
   'name': 'Biscuit',
   'age': 0.5,
   'favourite_toy': 'my chapstick'
}

print(cat.items()) # dict_items([('name', 'Biscuit'), ('age', 0.5), ('favourite_toy', 'my chapstick')])

# count
x = (1, 2, 3, 3, 3)
print(x.count(1))
print(x.count(3))

# index
t = (1, 2, 3, 3, 3)
print(t.index(1)) # 0
# print(t.index(5)) # ValueError: tuple.index(x): x not in tuple
print(t.index(3)) # 2 - only the first matching index is returned