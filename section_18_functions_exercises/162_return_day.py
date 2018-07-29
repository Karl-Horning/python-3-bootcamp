'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

# def return_day(num):
#    day = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
#    if num <= 0 or num > 7:
#       return None
#    return day[num - 1]

def return_day(num):
    try:
        return ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

print(return_day(1))
print(return_day(7))
print(return_day(0))
print(return_day(8))