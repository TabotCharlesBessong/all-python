
# we import all our files and modules which we will need for the project
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
from hangman_arts import logo , stages

# The variable that will tell if our game is over
end_of_game = False
lives = 6

print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
# This blank list will guide us through our solution
display = []
for _ in range(word_length):
    display += "_"
    
print(display)    

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])