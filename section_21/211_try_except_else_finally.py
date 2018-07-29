# try:
#    num = int(input('Please enter a number: '))
# except:
#    print('That\'s not a number!')
# else:
#    print('This is the ELSE')
# finally:
#    print('RUNS NO MATTER WHAT!')

while True:
   try:
      num = int(input('Please enter a number: '))
   except ValueError:
      print('That\'s not a number!')
   else:
      print(f'You entered {num}')
      break
   finally:
      print('RUNS NO MATTER WHAT!')