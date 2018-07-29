# def frequency(collection, primitive):
#    count = 0
#    while primitive in collection:
#       count += 1
#       collection.pop(collection.index(primitive))
#    return count

def frequency(collection, primitive):
   return collection.count(primitive)

print(frequency([1,2,3,4,4,4], 4)) # 3
print(frequency([True, False, True, True], False)) # 1