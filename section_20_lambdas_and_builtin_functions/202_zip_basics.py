# EXAMPLE 1
first_zip = zip([1,2,3], [4,5,6])
print(list(first_zip))
print(dict(first_zip))

# EXAMPLE 2
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*five_by_two)))