# OOP, 1 hour to make
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
currency = money_machine.CURRENCY
is_on = True

while is_on == True:
  drink = menu.find_drink(input("What do you want? "))
  if drink.name in menu.get_items():
    print(f"Your {drink.name} costs {currency}{drink.cost}")
    ingredients = drink.ingredients
    if coffee_maker.is_resource_sufficient(drink) == True:
      enough = money_machine.make_payment(drink.cost)
      if enough == True:
        coffee_maker.make_coffee(drink)
    else:
      is_on = False
  else:
    coffee_maker.report()
    money_machine.report()
    print("We don't have that order on the menu")
    print(f"Please choose from this list {menu.get_items()}")
  