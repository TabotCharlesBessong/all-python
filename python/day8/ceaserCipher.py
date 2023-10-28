
from art import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(logo)
shiftLen = int(input('How many times wil you like to shift: '))
letter = input('Enter your letter: ').lower()
direction = input("Type 'encode' if you want to encrypt and 'decode' if you want to decrypt: ").lower()


letterLen = len(letter)

# def encrypt(word,shift):
#   cipherText = ""
#   for w in word:
#     position = alphabet.index(w)
#     newPosition = position + shift
#     if newPosition > 25:
#       newPosition -= 25
#     newLetter = alphabet[newPosition]
#     cipherText += newLetter
#   print(f"The encryption of {letter} is {cipherText} ")  
  
# def decrypt(word,shift):
#   cipherText = ""
#   for w in word:
#     position = alphabet.index(w)
#     newPosition = position - shift
#     if newPosition < 0:
#       newPosition += 25
#     newLetter = alphabet[newPosition]
#     cipherText += newLetter
#   print(f"The decryption of {letter} is {cipherText} ")    
 

# if direction == 'encode':
#   encrypt(word=letter, shift=shiftLen)
    
# elif direction == 'decode':
#   decrypt(word=letter, shift=shiftLen)  
 
# else:
#   print('wrong choice , please enter "encode" to encrypt and "decode" to decrypt ')
  
def ceaser(met,word,shift):
  cipherText = ""
  # if shift >25
  for w in word:
    position = alphabet.index(w)
    if met == 'encode':
      newPosition = position + shift
      if newPosition > 25:
        newPosition -= 25
    elif met == 'decode':
      newPosition = position - shift
      if newPosition < 0:
        newPosition += 25
    newLetter = alphabet[newPosition]
    cipherText += newLetter   
  print(f"The encryption of {letter} is {cipherText} ")
  

ceaser(met=direction, word=letter , shift=shiftLen)  