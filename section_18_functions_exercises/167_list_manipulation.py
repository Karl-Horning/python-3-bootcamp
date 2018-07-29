# def remove(userlist, location='end'):
#    if location == 'end':
#       userlist.pop()
#    elif location == 'beginning':
#       userlist.pop(0)
#    return userlist

# def add(userlist, location='end', value=0):
#    if location == 'end':
#       userlist.append(value)
#    elif location == 'beginning':
#       userlist.insert(0, value)
#    return userlist

# def list_manipulation(userlist, command, location, value):
#     return command(userlist, location, value)

def list_manipulation(collection, command, location, value=None):
    if command == 'remove' and location == 'end':
        return collection.pop()
    elif command == 'remove' and location == 'beginning':
        return collection.pop(0)
    elif command == 'add' and location == 'beginning':
        collection.insert(0, value)
    elif command == 'add' and location == 'end':
        collection.append(value)
    return collection

print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) # 1
print(list_manipulation([1,2,3], "add", "beginning", 20)) # [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) # [1,2,3,30]
