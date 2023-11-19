def make_order(coffee_type):
    water_required = MENU["coffee_type"]["ingredients"]["water"]
    milk_required = MENU["coffee_type"]["ingredients"]["milk"]
    coffee_required = MENU["coffee_type"]["ingredients"]["coffee"]

    if resources["water"] < water_required:
        print("Sorry there is not enough water.")
    elif resources["milk"] < milk_required:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < coffee_required:
        print("Sorry there is not enough coffee.")
    else:

        print("Please insert the coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickels = float(input("How many nickels?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        total_coins_value = quarters + dimes + nickels + pennies

        if total_coins_value >= MENU["espresso"]["cost"]:
            change = total_coins_value - MENU["espresso"]["cost"]

            resources["money"] += MENU["espresso"]["cost"]
            resources["water"] -= water_required
            resources["milk"] -= cappuccino_milk_required
            resources["coffee"] -= cappuccino_coffee_required

            print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
order = input(" What would you like? (espresso/latte/cappuccino):").lower()

if order == "off":
    exit()
elif order == "report":
    print(resources)

elif order == "espresso":
    espresso_water_required = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee_required = MENU["espresso"]["ingredients"]["coffee"]

    if resources["water"] < espresso_water_required:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < espresso_coffee_required:
        print("Sorry there is not enough coffee.")
    else:

        print("Please insert the coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickels = float(input("How many nickels?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        total_coins_value = quarters + dimes + nickels + pennies

        if total_coins_value >= MENU["espresso"]["cost"]:
            change = total_coins_value - MENU["espresso"]["cost"]

            resources["money"] += MENU["espresso"]["cost"]
            resources["water"] -= espresso_water_required
            resources["milk"] -= cappuccino_milk_required
            resources["coffee"] -= espresso_coffee_required

            print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

elif order == "cappuccino":
    espresso_water_required = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk_required = MENU["cappuccino"]["ingredients"]["milk"]
    espresso_coffee_required = MENU["cappuccino"]["ingredients"]["coffee"]

    if resources["water"] < espresso_water_required:
        print("Sorry there is not enough water.")
    elif resources["milk"] < cappuccino_milk_required:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < espresso_coffee_required:
        print("Sorry there is not enough coffee.")
    else:

        print("Please insert the coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickels = float(input("How many nickels?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        total_coins_value = quarters + dimes + nickels + pennies

        if total_coins_value >= MENU["espresso"]["cost"]:
            change = total_coins_value - MENU["espresso"]["cost"]

            resources["money"] += MENU["espresso"]["cost"]
            resources["water"] -= espresso_water_required
            resources["milk"] -= cappuccino_milk_required
            resources["coffee"] -= espresso_coffee_required

            print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")





