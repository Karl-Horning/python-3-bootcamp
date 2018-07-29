# def intersection(lis1, lis2):
#    return [item for item in lis1 if item in lis2]

def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

print(intersection([1, 2, 3], [2, 3, 4])) # [2, 3]
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z'])) # ['z']