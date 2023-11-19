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


def make_order(request):
    if request == "off":
        exit()
    elif request == "report":
        print(resources)
    elif request == "espresso" or "cappuccino" or "latte":
        water_required = MENU[request]["ingredients"]["water"]
        coffee_required = MENU[request]["ingredients"]["coffee"]
        if "milk" in MENU[request]["ingredients"]:
            milk_required = MENU[request]["ingredients"]["milk"]
        else:
            milk_required = 0

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

            if total_coins_value >= MENU[request]["cost"]:
                change = total_coins_value - MENU[request]["cost"]

                resources["money"] += MENU[request]["cost"]
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required

                print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {request} ☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")

    new_order = input(" What would you like? (espresso/latte/cappuccino):").lower()
    make_order(new_order)


order = input(" What would you like? (espresso/latte/cappuccino):").lower()
make_order(order)






