# print('...rock...')
# print('...paper...')
# print('...scissors...')

# player1 = input("enter Player 1's choice: ")
# player2 = input("enter Player 2's choice: ")

# if player1 and player2:
#    print('SHOOT!')

#    if player1[0] == player2[0]:
#       print('Draw!')
#    elif player1[0] == 'r' and player2[0] == 's':
#       print('Player 1 wins')
#    elif player1[0] == 'p' and player2[0] == 'r':
#       print('Player 1 wins')
#    elif player1[0] == 's' and player2[0] == 'p':
#       print('Player 1 wins')
#    else:
#       print('Player 2 wins')
# else:
#    print('Please both enter a value')


print('...rock...')
print('...paper...')
print('...scissors...')

player1 = input("enter Player 1's choice: ")
player2 = input("enter Player 2's choice: ")

if player1 == player2:
   print('Draw!')
elif player1 == 'rock':
   if player2 == 'scissors':
      print('Player 1 wins')
   elif player2 == 'paper':
      print('Player 2 wins')
elif player1 == 'paper':
   if player2 == 'rock':
      print('Player 1 wins')
   elif player2 == 'scissors':
      print('Player 2 wins')
elif player1 == 'scissors':
   if player2 == 'paper':
      print('Player 1 wins')
   elif player2 == 'rock':
      print('Player 2 wins')
else:
   print('Something went wrong...')