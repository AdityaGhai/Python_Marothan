from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
"""Coffee Machine Main Code"""

coffee = CoffeeMaker()
money_store = MoneyMachine()
menu1 = Menu()

is_on = True
while is_on:
    options = menu1.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money_store.report()
    elif menu1.find_drink(choice):
        drink = menu1.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money_store.make_payment(drink.cost):
                coffee.make_coffee(drink)
