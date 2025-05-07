import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

items = menu.get_items()

coffee_on = True
while coffee_on:
    user = input(f"What would you like? ({items}): ")
    if user == "off":
        coffee_on = False
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




