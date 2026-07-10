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

def check_resources(cofeeItems):
    var = True

    if cofeeItems["ingredients"]["water"]  > resources["water"]:
        print("Sorry, there is not enough water.")
        var = False
    if option != 'espresso'  and cofeeItems["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        var = False
    if cofeeItems["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        var = False

    return var

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes    = int(input("How many dimes?:    "))
    nickles  = int(input("How many nickles?:  "))
    pennies  = int(input("How many pennies?:  "))

    user_coins = quarters*.25 + dimes*.1 + nickles*.05 + pennies*.01

    return user_coins


def report():
    print(f"Water:  {resources['water']} ml")
    print(f"Milk:   {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} gr")
    print(f"Money:  ${resources['money']:.2f}")

def make_cofee(option):

    print(f"Here is your {option} ☕ Enjoy !\n")

    # update resources
    resources["money"] += MENU[option]["cost"]
    resources["water"] -= MENU[option]["ingredients"]["water"]
    resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
    if option != "espresso":
        resources["milk"] -= MENU[option]["ingredients"]["milk"]


machine = True
while machine:
    option = input("What do you like ? (espresso/latte/cappuccino): ").lower()

    if option == "report":
        report()
    elif option in ["espresso", "latte", "cappuccino"]:

        if check_resources(MENU[option]):
            #si hay suficientes recursos, recibir monedas
            user_money = process_coins()
            if user_money >= MENU[option]["cost"]:
                # dar cambio, servir bebida
                change = user_money - MENU[option]["cost"]
                print(f"Here is ${change:.2f} in change")

                make_cofee(option)

            else:
                print("Sorry, that's not enough money. Money refunded.")

    elif option == "off":
        print("shutting down")
        machine = False
    else:
        print("Invalid option")


