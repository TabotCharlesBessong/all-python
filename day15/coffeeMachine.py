
from data import MENU as menu , profit , resources

def isResourceSufficient(orderIngredient):
  """Checks and makes sure that there are always enough ingredients"""
  for item in orderIngredient:
    if orderIngredient[item] >= resources[item]:
      print(f"Sorry there is no enough {item} ")
      return False
  return True

def processCoins():
  """Return the total calculation of all coins input by the customer"""
  print('Please insert coins')
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

def checkTransaction(amount,cost):
  """Return true when payment accepted else false (and payment need to be above or equal to the cost) """
  if amount >= cost:
    change = round(amount - cost , 2)
    print(f"Here is your change {change} ")
    global profit
    profit += cost 
    return True
  else:
    print("Sorry that is not enough money!")
    return False
  
def makeCoffee(drinkName,orderIngredient):
  """Deduct the required resources from the ingredients"""
  for item in orderIngredient:
    resources[item] -= orderIngredient[item]
  print(f"Here is your {drinkName} 😍😍😍 ")

isOn = True

while isOn:

  choice = input("What would you like: \n (espresso/latte/cappuccino) ")
  if choice == "off":
    isOn = False
  elif choice == "report":
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${profit}")
  
  else:
    drink = menu[choice] 
    if isResourceSufficient(drink['ingredients']):
      payment = processCoins()
      if checkTransaction(payment,drink['cost']):
        makeCoffee(choice,drink['ingredients'])