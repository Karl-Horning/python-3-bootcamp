people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
nums = [2, 30, 60, 22, 4, 8]

print(all([name[0] == 'C' for name in people]))
print(all([num % 2 == 0 for num in nums]))