person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = {person[i][0]: person[i][1] for i in range(0, len(person))}

# Using a dictionary comprehension 
# answer = {thing[0]: thing[1] for thing in person}

# An alternate solution using a dict comprehension, without any references to list indexes:
# answer = {k:v for k,v in person}

# Finally, a really simple solution.  If you have a list of pairs, you can very easily turn it into a dictionary using dict() 
answer = dict(person)

print(answer)

