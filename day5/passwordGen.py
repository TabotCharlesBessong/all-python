
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9' ]

symbols = ['!','<','>','$','&','(',')','[',']','+','-','*','{','}','?']

print("Welcome to the password generator python series")

letterNum = int(input("How many letter do you want your password to have : "))
numLen = int(input("Number of numbers do you want your password to have : "))
symbolLen = int(input("Number of symbols do you want your password to have? :"))

# my own implementation (The easiest way to)
password = []
lettersPas = []
numberPas = []
symbolPas = []
for i in range(0,letterNum):
  ranL = letters[random.randint(0,letterNum)]
  # lettersPas.append(letters[i])
  lettersPas.append(ranL)
print(lettersPas)  
  
for i in range(0,numLen):
  ranN = numbers[random.randint(0,numLen)]
  # numberPas.append(numbers[i]) 
  numberPas.append(ranN) 
print(numberPas)  
  
for i in range(0,symbolLen):
  ranS = symbols[random.randint(0,symbolLen)]
  # symbolPas.append(symbols[i]) 
  symbolPas.append(ranS) 
print(symbolPas) 

password = lettersPas + numberPas + symbolPas
print(password) 

# tutors implementation

password1 = ""

for char in range(1, letterNum + 1):
  randomChar = rn