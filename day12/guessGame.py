
import random


GUESS = random.randint(1,101)
easyLimit = 10
mediumLimit = 8
hardLimit = 5
# userGuess = int(input(""))

score = 0

def guessGame():
  level = input("You can choose easy game , medium game , hard game\n Type easy for easy game , medium for medium game ,hard for hard game: \n").lower()
  
  if level == 'easy':
    limit = easyLimit
  elif level == 'medium':
    limit = mediumLimit
  elif level == 'hard':
    limit = hardLimit
  else:
    print('Please chose again , you chose the wrong level.')
  
  while limit != 0 :
    userGuess = int(input(f"You have {limit} attempts remaining to guess the number: ")) 
    limit -= 1 
    if userGuess == GUESS:
      print(f"You got it you guessed {userGuess} and the guess was {GUESS} ")
      global score 
      score += limit
      print(f"You have {limit} left so your score is {score} points ")
      limit = 0
    elif userGuess > GUESS:
      print('Too high')  
    else:
      print('Too low')  
      # return "you got it" 
# print(GUESS) 

def play():
  play = input("Would you like to play the guess game?\n y or n: ").lower()
  if play == 'y':
    guessGame()
  else:
    return 
  
  # while play == 'y':
    # guessGame() 
# guessGame()

def playAgain():
  again = input("Would you like to play again?\n y or n: ").lower()
  
  # while again == 'y':
  #   play()
  
  if again == 'y':
    play()
  else:
    return
  """
  if again == 'y':
    play()
  else:
    return
  
  if statements do have a draw back which is they check the condition only once , so we are going to use the while loop
  """
  

play()  
playAgain()  