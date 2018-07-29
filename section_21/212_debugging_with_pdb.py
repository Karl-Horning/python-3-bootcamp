import pdb
first = 'First'
second = 'Second'
pdb.set_trace()
result = first + second
third = 'Third'
result += third
print(result)

# import pdb
# pdb.set_trace()

# Also commonly on one line: 
# import pdb; pdb.set_trace()

# Commmon PDB commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)