def compare(guess, actual):
  if guess < actual:
    print("greater")
    if abs(guess-actual)<2:
      print("nearby")
      return False
    elif abs(guess-actual)<5:
      print("far")
      return False
    else:
      print("too far")
      return False
      
      
  elif guess == actual:
    print(f"correct guess: {guess}")
    return True
    
    
  else:
    print("lesser")
    if abs(guess-actual)<2:
      print("nearby")
      return False
      
    elif abs(guess-actual)<5:
      print("far")
      return False
      
    else:
      print("too far")
      return False
      
import random
from art import logo
print(logo)

level_map = {"easy":10, "hard":5}

actual = random.choice(range(100))
level = input(f"select mode: Easy or Hard: ").lower().strip()
for i in range(level_map[level]):
  guess = int(input('enter a number: '))
  if compare(guess, actual):
    break
  if i == level_map[level]:
    print(f'actual number: {actual}')
  print(f"remaining chances: {level_map[level]-i}")

  
  

    