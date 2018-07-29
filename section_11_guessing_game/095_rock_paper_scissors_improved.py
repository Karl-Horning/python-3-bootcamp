from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
   print(f'Player Score: {player_wins} | Computer Score {computer_wins}')
   print('...rock...')
   print('...paper...')
   print('...scissors...')

   player = input("Player, enter your choice: ").lower()
   if player == 'quit' or player == 'q':
      break

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
         player_wins += 1
      else:
         print('Computer wins')
         computer_wins += 1
   elif player == 'paper':
      if ai == 'rock':
         print('Player wins')
         player_wins += 1
      else:
         print('Computer wins')
         computer_wins += 1
   elif player == 'scissors':
      if ai == 'paper':
         print('Player wins')
         player_wins += 1
      else:
         print('Computer wins')
         computer_wins += 1
   else:
      print('Please enter a valid move...')
if player_wins > computer_wins:
   print('CONGRATS, YOU WON!')
elif player_wins == computer_wins:
   print("IT'S A TIE!")
else:
   print('OH NO :( THE COMPUTER WON!')
print(f'FINAL SCORES: Player Score: {player_wins} | Computer Score {computer_wins}')