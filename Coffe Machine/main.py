from coffee_types import MENU, resources


def make_espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]


def make_latte():
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]


def make_cappuccino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]


def count_money(quarters, dimes, nickels, pennies):
    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)


def calculate_change(amount, coffee_type):
    change = amount - MENU[coffee_type]["cost"]
    return round(change, 2)


machine_on = True
money = 0

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Generating machine report
    if user_choice == "report":
       for key in resources:
           if key == "water":
               print(f"Water: {resources[key]}ml")
           if key == "milk":
               print(f"Milk: {resources[key]}ml")
           if key == "coffee":
               print(f"Coffee: {resources[key]}g")
       print(f"Money: ${money}")

    # If the user wants an espresso
    elif user_choice == "espresso":
        make_espresso()
        if resources['water'] < 0:
            resources['water'] = 0
            print("Sorry there is not enough water.")
        else:
            user_money = count_money(float(input("how many quarters? ")), float(input("how many dimes? ")),
                                     float(input("how many nickels? ")), float(input("how many pennies? ")))
            if user_money >= MENU["espresso"]["cost"]:
                if user_money > MENU["espresso"]["cost"]:
                    print(f"Here is ${calculate_change(user_money,'espresso')} in change.")
                money += MENU["espresso"]["cost"]
                print("Here is your espresso! Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded. ")

    # If the user wants a latte
    elif user_choice == "latte":
        make_latte()
        if resources['water'] < 0:
            resources['water'] = 0
            print("Sorry there is not enough water.")
        else:
            user_money = count_money(float(input("how many quarters? ")), float(input("how many dimes? ")),
                                     float(input("how many nickels? ")), float(input("how many pennies? ")))
            if user_money >= MENU["latte"]["cost"]:
                if user_money > MENU["latte"]["cost"]:
                    print(f"Here is ${calculate_change(user_money,'latte')} in change.")
                money += MENU["latte"]["cost"]
                print("Here is your latte! Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded. ")

    # If the user wants a cappuccino
    else:
        make_cappuccino()
        if resources['water'] < 0:
            resources['water'] = 0
            print("Sorry there is not enough water.")
        else:
            user_money = count_money(float(input("how many quarters? ")), float(input("how many dimes? ")),
                                     float(input("how many nickels? ")), float(input("how many pennies? ")))
            if user_money >= MENU["cappuccino"]["cost"]:
                if user_money > MENU["cappuccino"]["cost"]:
                    print(f"Here is ${calculate_change(user_money,'cappuccino')} in change.")
                money += MENU["cappuccino"]["cost"]
                print("Here is your cappuccino! Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded. ")

    if user_choice == "off":
        machine_on = False













