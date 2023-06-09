from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    option = menu.get_items()
    choose = input(f"What would you like? ({option}): ")
    choose_item = menu.find_drink(choose)
    if choose == "off":
        is_on = False
        print("The coffee machine is off")
    elif choose == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_maker.is_resource_sufficient(choose_item) and money_machine.make_payment(choose_item.cost):
        coffee_maker.make_coffee(choose_item)
