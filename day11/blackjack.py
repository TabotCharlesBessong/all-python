
import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def dealer():
  """Returns a random card from the deck"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card
  
def calculateScore(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user,computer):
  if user == computer:
    return "Draw"
  elif computer == 0:
    return "You loose computer has blackjack"
  elif user == 0:
    return "You win you have blackjack"
  elif user > 21:
    return "You lost you went to far"
  elif computer > 21:
    return "You win computer has gone to far"
  elif user > computer:
    return "You win"
  else:
    return "You loose"   

userCards = []
computerCards = []
isGameOver = False
# newCard = int(input("Enter your new card"))

for i in range(2):
  userCards.append(dealer())
  computerCards.append(dealer()) 

while not isGameOver:
    
  userScore = calculateScore(userCards)  
  computerScore = calculateScore(computerCards)  
  print(f"The user cards are {userCards} and their current score is {userScore} ")
  print(f"The computer first  card is {computerCards[0]}  ")

  if userScore == 0 or computerScore == 0 or userScore > 21:
    isGameOver = True
  else:
    again = input("Will you like to continue ? y or n: ")
    if again == 'y':
      userCards.append(dealer())  
    else:
      isGameOver = True
          

while computerScore == 0 and computerScore < 17:
  computerCards.append(dealer())
  computerScore = calculateScore(computerScore)
compare(userScore,computerScore)  
  

# my stupid implementation
# def playAgain():
  # if again == 'yes':
    # newCard = random.choice(cards)
    # userCards.append(newCard)
    # computerCards.append(random.choice(cards))
    # userScore = calculateScore(userCards)
    # computerScore = calculateScore(computerCards)
    # if userScore > 21 and userScore > computerScore:
      # # print(f"with a score of {userScore} and computer score of {computerScore} you lost ")
      # 
    # elif userScore > 21 and userScore < computerScore:
      # # print(f"with a score of and computer score of {computerScore} {userScore} you lost ")
      # 
    # elif userScore < 21:
      # print(f"With a score of {userScore} you win ")
      # 
  # else:
    # isGameOver = True