cities = ['Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago', 'Los Angeles', 'Shanghai', 'Tokyo', 'Oslo']
print(len(set(cities)))
print(list(set(cities)))

# ADD
# Adds an element to a set. If the element is already in the set, the set doesn't change
s = set([1, 2, 3])

s.add(4)

print(s) # {1, 2, 3, 4}

s.add(4)

print(s) # {1, 2, 3, 4}

# REMOVE
# Removes a value from the set - returns a KeyError if the value is not found
# Use discard to not return an error
set1 = {1, 2, 3, 4, 5, 6} 

set1.remove(3)

print(set1) # {1, 2, 4, 5, 6}

# COPY
# Creates a copy of the set
s = set([1, 2, 3])
another_s = s.copy()
print(another_s) # {1, 2, 3}
print(another_s is s) # False

# CLEAR
# Removes all the contents of the set
s = set([1, 2, 3])

s.clear()

print(s) # set()

# Set Math
math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

# To generate a set with all unique students
print(math_students | biology_students) # {'Jane', 'Matthew', 'Aparna', 'Helen', 'Oliver', 'James', 'Charlotte', 'Prashant', 'Mesut'}

# To generate a set with students who are in both courses
print(math_students & biology_students) # {'James', 'Matthew'}