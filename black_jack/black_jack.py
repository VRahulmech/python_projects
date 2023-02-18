cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []

import random
def draw_card():
  return random.choice(cards)

def initial_dist(player, computer):
  player.append(draw_card())
  player.append(draw_card())
  computer.append(draw_card())
  computer.append(draw_card())


def win_lose(player, computer):
    if sum(player)<=21 and sum(computer)<=21:
      if sum(player) > sum(computer):
        print(f"computer sum: {sum(computer)}")
        print('you win')
      elif sum(player)==sum(computer):
        print('draw')
      else:
        print(f"computer sum: {sum(computer)}")
        print('you lost')

    elif sum(player)<=21:
      print(f"computer sum: {sum(computer)}")
      print('you win')
    else:
      print(f"computer sum: {sum(computer)}")
      print('you lost')


while True:
  print('Do you want to play the game?')
  user_input = input("press 'y' if yes else 'n' : ")
  player.clear()
  computer.clear()
  if user_input == 'n':
    break
  else:
    initial_dist(player, computer)
    
    print(f"your cards: {player},")
    
    print(f"sum: {sum(player)}")

    print(f"computer : {computer[0]}")

    while True:
      ask = input('do you want to pick the card? "y" or "n": ')
      if ask=="n":
        break
      else:
        player.append(draw_card())
        if (sum(player)>21) and (11 in player):
          for i in range(len(player)):
            if player[i]==11:
              player[i]=1
              break
        elif sum(player)>21:
          print('you lost')
          print(f"computer sum: {sum(computer)}")
          break
        print(f"your cards: {player}")
        print(f"sum: {sum(player)}")

    while sum(computer)<16 and sum(player)<=21:
      computer.append(draw_card())
      

    win_lose(player, computer)
    
          

  
      

      
      
    
    


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

