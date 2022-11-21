
from menu import MenuItem , Menu 
from moneyMachine import MoneyMachine
from coffeeMaker import CoffeeMaker 

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

isOn = True

while isOn:
  options = menu.get_items()
  choice = input(f"What would you like ({options}) ")
  if choice == 'off':
    isOn = False
  elif choice == 'report':
    coffeeMaker.report()
    moneyMachine.report()
  else:
    drink = menu.find_drink(choice)
    # if coffeeMaker.is_resource_sufficient(drink):
    #   if (moneyMachine.make_payment(drink.cost)):
    #     coffeeMaker.make_coffee(drink)
    
    # alternatively 
    if coffeeMaker.is_resource_sufficient and moneyMachine.make_payment(drink.cost):
      coffeeMaker.make_coffee(drink)
    # print(drink)