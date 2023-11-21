from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
coffee_menu = Menu()
coin_machine = MoneyMachine()

options = coffee_menu.get_items()
is_on = True

while is_on:
    order = input(f"What would you like? ({options}): ").lower()

    if order == "report":
        coffee_maker.report()
        coin_machine.report()

    elif order == "off":
        is_on = False

    else:
        order = coffee_menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(order) and coin_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
            print(f"Here is your {order}. Enjoy!")





