names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(d):
   return list(map(lambda x: x['first'] + ' ' + x['last'], d))

# def extract_full_name(l):
#    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
