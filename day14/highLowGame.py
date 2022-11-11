# import 
import random
from art import logo , vs
from data import data

 
# display art
print(logo)

# generate a random account
def generateRandom():
  return random.choice(data)

accountA = generateRandom()
print(f"{accountA['name']} is a {accountA['description']} from the {accountA['country']} ")
print(vs)

accountB = generateRandom()
# if accountA == accountB:
  # accountB = generateRandom()
print(f"{accountB['name']} is a {accountB['description']} from the {accountB['country']} ")

# have user guess the correct answer
guess = input("Do you want to choose A for the first account or B for the second: ").lower()

# Check the user answer 
def checkAnswer(guess,account1,account2):
  if guess == 'a':
    if account1['follower_count'] > account2['follower_count']:
      return True
    else:
      return False
  else:
    if account1['follower_count'] > account2['follower_count']:
      return False
    else:
      return True
      
checkAnswer(guess,accountA,accountB)  

# Give user feedback about their guess   
def score():
  score = 0
  if checkAnswer(guess,accountA,accountB):
    score +=1
    print(f"Correct your score is {score} points ")
    return score
  else:
    print("You lost the game")
    return score

score()  

def playAgain():
  again = input("Would you like to play again\n Yes : y or no:n").lower()
  if again == "y":
    checkAnswer(guess,accountA,accountB)
    score()
  else:
    print('Thank you for playing') 
    score() 
    
playAgain()    