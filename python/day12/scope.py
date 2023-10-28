# global variables
enemies = 1
def increaseEnemies():
  # local variable 
  # modifying global variable 
  global enemies
  enemies += 2
  print(f"Enemies inside function: {enemies} ")
  
increaseEnemies()
print(f"Enemies outside function : {enemies} ")  

# no block scope
gameLevel = 3
enemiesL = ['skeleton','zombie','alien']
if gameLevel < 5:
  newEnemy1 = enemiesL[0]
  
print(newEnemy1)  

# block scope
def increaseEnemiesF():
  enemiesF = ['skeleton','zombie','alien']
  if gameLevel < 5:
    newEnemy2 = enemiesF[0]
  print(newEnemy2)
 
# modifying without changing the value of the global variable

friends = 6
def updateFriends():
  return friends + 2

newFriends = updateFriends()
print(newFriends)
print(friends)

# global constant 
PI = 3.14159