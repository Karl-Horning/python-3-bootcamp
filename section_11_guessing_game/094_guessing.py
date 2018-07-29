from random import randint

# keep_playing = 'yes'

# while keep_playing[0] != 'n':
#    ran_num = randint(1, 10)
#    guess = 0

#    while guess != ran_num:
#       guess = input('Guess a number between 1 and 10: ')
#       guess = int(guess)

#       if guess < ran_num:
#          print('Too low, try again!')
#       elif guess > ran_num:
#          print('Too high, try again!')
#       else:
#          print('You guessed it! You won!')
   
#    keep_playing = input('Do you want to keep playing? (y/n) ')
#    if keep_playing[0] == 'n':
#       print('Thank you for playing!')

ran_num = randint(1, 10)

while True:
   guess = input('Guess a number between 1 and 10: ')
   guess = int(guess)

   if guess < ran_num:
      print('Too low, try again!')
   elif guess > ran_num:
      print('Too high, try again!')
   else:
      print('You guessed it! You won!')
      play_again = input('Do you want to keep playing? (y/n) ')
      if play_again == 'y':
         ran_num = randint(1, 10)
         guess = None
      else:
         print('Thank you for playing!')
         break