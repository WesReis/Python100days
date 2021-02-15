from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

available = Menu()
barista = CoffeeMaker()
cash = MoneyMachine()
machine_on = True

print(available.find_drink("latte").cost)
while machine_on:
    # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    order = input(f"What would you like? {available.get_items()}: ")
    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if order == "off":
        machine_on = False
    # TODO: 3. Print report.
    elif order == "report":
        barista.report()
        cash.report()
    # TODO: 4. Check resources sufficient?
    else:
        if barista.is_resource_sufficient(available.find_drink(order)):
    # TODO: 5. Process coins.
            if cash.make_payment(available.find_drink(order).cost):
    # TODO: 6. Check transaction successful?
    # TODO: 7. Make Coffee.
                barista.make_coffee(available.find_drink(order))
