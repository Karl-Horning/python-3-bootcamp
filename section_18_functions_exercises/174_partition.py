def isEven(num):
   return num % 2 == 0

def partition(collection, callback):
    result = [[i for i in collection if isEven(i)],[i for i in collection if not isEven(i)]]
    return result

# def partition(l, callback):
    # return [[l.pop(l.index(i)) for i in l if callback(i)],l]

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]