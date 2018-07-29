from random import randint

print('...rock...')
print('...paper...')
print('...scissors...')

player = input("Player, enter your choice: ").lower()

num = randint(0, 2)

if num == 0:
   ai = 'rock'
elif num == 1:
   ai = 'paper'
else:
   ai = 'scissors'

print(f'Computer plays {ai}')

if player == ai:
   print('Draw!')
elif player == 'rock':
   if ai == 'scissors':
      print('Player wins')
   else:
      print('Computer wins')
elif player == 'paper':
   if ai == 'rock':
      print('Player wins')
   else:
      print('Computer wins')
elif player == 'scissors':
   if ai == 'paper':
      print('Player wins')
   else:
      print('Computer wins')
else:
   print('Please enter a valid move...')