
print('Welcome to the love calculator')

yourName = input('What is your name : ').lower()
herName = input('What is her name: ').lower()
# print(yourName)
names = yourName + herName 

# print(names.count('s'))
t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

true = t + r + u + e
print(true)

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

love = l + o + v + e
print(love)

loveScore = str(true) + str(love)
loveScore = int(loveScore)

if (loveScore < 10 or loveScore > 90):
  print(f'Your love score is {loveScore} you go together like coke and mentos ')

elif (loveScore >= 40 or loveScore <= 50):
  print(f'Your love score is {loveScore} you are alright together ')
else:
  print(f'Your love score is {loveScore} ')