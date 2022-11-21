
import random

rock = '''
    ________
________)
   (______)    
   (______)    
   (_____)    
---.__ (____)    
'''

#  paper form
paper = '''
     ________
___' ________)____  
      ________)____
    ________)____   
____   (____)     
      
'''

# scissors form

scissors = '''
    _______
___' ____)____
       ________)
    __________)  
    (_____)
----.__(___)         
'''

myList = [rock,paper,scissors]

userChoice = int(input("What do you choose? Typo 0 for Rock , 1 for Paper , 2 for scissors: \n"))

print(f'You choose {myList[userChoice]}')


computerChoice = random.randint(0,2)
print(f'The computer choose{myList[computerChoice]}')


# my method of implementation 
# if ((userChoice == 0 and computerChoice == 1) or (userChoice == 1 and computerChoice == 2) or (userChoice == 2 and computerChoice == 0)):
#   print(f" You choose \n {userChoice} and the computer choose \n {computerChoice} and the winner is the Computer")

# elif ((userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0) or (userChoice == 2 and computerChoice == 1)):
#   print(f" You choose \n {userChoice} and the computer choose \n {computerChoice} and its a draw")

# elif (userChoice == computerChoice):
#   print(f" You choose \n {userChoice} and the computer choose \n {computerChoice} and this is a draw")
  
# else:
#   print('Please choose 0 for Rock , 1 for Paper and 2 for scissors')
  

if userChoice >= 3 or userChoice < 0: 
  print('You typed an invalid number you loose')
elif userChoice == 0 and computerChoice == 2:
  print("You win!")
elif userChoice == 2 and computerChoice == 0:
  print("You loose!") 
 
elif computerChoice > userChoice:
  print("You loose!") 
elif computerChoice == userChoice:
  print('Its a draw') 
elif userChoice > computerChoice:
  print('You win')       
 