
print('Welcome to the python pizza delivery app')
size = input('What size of pizza do you want ? S , M or large:  ')
addPepperoni = input('Do you want to add pepperoni ? Y or N')
extraCheese = input('Do you want cheese ? Y or N: ')
# price 

if (size == 'L' or size == 'l'):
  if (addPepperoni == 'y' or addPepperoni == 'Y'):
    if (extraCheese == 'y' or extraCheese == 'Y'):
      price = 25 + 3 + 1
      print(f'Your pizza is ${price} ')
      
    else:
      price = 25 + 3
      print(f'Your pizza is ${price} ')
    
      
  elif (extraCheese == 'y' or extraCheese == 'Y'):
    # if (extraCheese == 'y' or extraCheese == 'Y'):
      price = 25 + 1
      print(f'Your pizza is ${price} ')
      # pass
  else:
    
    price = 25
    print(f'Your pizza is ${price} ') 

elif (size == 'M' or size == 'm'):
  if (addPepperoni == 'y' or addPepperoni == 'Y'):
    if (extraCheese == 'y' or extraCheese == 'Y'):
      price = 20 + 3 + 1
      print(f'Your pizza is ${price} ')
      
    else:
      price = 20 + 3
      print(f'Your pizza is ${price} ')
    
      
  elif (extraCheese == 'y' or extraCheese == 'Y'):
    # if (extraCheese == 'y' or extraCheese == 'Y'):
      price = 20 + 1
      print(f'Your pizza is ${price} ')
      # pass
  else:
    
    price = 15
    print(f'Your pizza is ${price} ')
    
    
elif (size == 'S' or size == 's'):
  if (addPepperoni == 'y' or addPepperoni == 'Y'):
    if (extraCheese == 'y' or extraCheese == 'Y'):
      price = 15 + 3 + 1
      print(f'Your pizza is ${price} ')
      
    else:
      price = 15 + 3
      print(f'Your pizza is ${price} ')
    
      
  elif (extraCheese == 'y' or extraCheese == 'Y'):
    # if (extraCheese == 'y' or extraCheese == 'Y'):
      price = 15 + 1
      print(f'Your pizza is ${price} ')
      # pass
  else:
    
    price = 15
    print(f'Your pizza is ${price} ')
    
else:
  print('wrong choice')