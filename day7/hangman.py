
import random
from words import word_list
import arts


wordList = word_list
chosenWord = random.choice(wordList)
print(chosenWord)

stages = arts.stages 
logo = arts.logo

display = []
for a in chosenWord:
  display += '_' 

print(display) 

endOfGame = False
life = len(stages)
while not endOfGame:
  guess = input("Enter a letter in the word: ") 

  for position in range(len(chosenWord)):
    letter = chosenWord[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosenWord:    
    life -=1
    if life == 0:
      endOfGame = True
      print('You loose!')

  print(f"{' '.join(display)}")
  
  if '_' not in display:
    endOfGame = True 
    print('You win!')
    
  print(stages[life])
     