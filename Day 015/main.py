from menu import MENU, resources

stop_machine = False
resources_available = True


def report():
    """Function to print the report of resources on the coffee machine."""
    print(f"Water: {resources['water']}ml.")
    print(f"Milk: {resources['milk']}ml.")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${resources['profit']:.2f}")


def check_resources(drink):
    """This function will check if there are enough resources to make a drink."""
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        return False
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return False
    else:
        return True


def no_resources(drink):
    """This function will print which resources are missing."""
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, not enough water.")
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry, not enough milk.")
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, not enough coffee.")


#   a. if not enough money "Sorry that's not enough money. Money refunded."
#   b. if enough money then add that cost to bank
#   c. if too much money offer change "Here is $x in change."
def process_payment(pay, price, drink):
    if pay < price:
        return "Sorry that's not enough money. Money refunded."
    elif pay >= price:
        resources["water"] -= MENU[prompt]["ingredients"]["water"]
        resources["coffee"] -= MENU[prompt]["ingredients"]["coffee"]
        resources["milk"] -= MENU[prompt]["ingredients"]["milk"]
        resources["profit"] += pay
        return f"Here is ${pay - cost:.2f} in change.\nHere's your {drink}.  ☕ Enjoy!"


# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):☕ "
#   a. Check users input
#   b. prompt should show up again to serve next customer
while not stop_machine:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. "Off" prompt to end the program
    if prompt == "off":
        stop_machine = True
    # TODO: 3. Report option to generate all resources on the machine
    elif prompt == "report":
        report()
    # TODO: 4. When product selected check that there are enough resources
    #   a. if not enough print "Sorry there's not enough ..."
    else:
        resources_available = check_resources(prompt)
        if not resources_available:
            no_resources(prompt)
        else:
            # TODO: 5. Process coins payment
            # Maybe make this into a function?
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            paid = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
            cost = MENU[prompt]["cost"]
            # TODO: 6. Check transaction successful:
            print(process_payment(paid, cost, prompt))
            # TODO: 7. make coffee
            #   a. deduct resources
            #   b. tell user "Here's your drink. Enjoy!"
