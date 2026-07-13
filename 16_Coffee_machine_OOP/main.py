from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
money_process = MoneyMachine()
menu = Menu()

machine = True
while machine:
    choice = menu.get_items()
    option = input(f"What would you like? {choice}: ").lower()
    if option == "report":
        coffe_machine.report()
        money_process.report()
    elif option == "off":
        print("Shutting down...")
        machine = False
    else:
        drink = menu.find_drink(option)
        if drink and coffe_machine.is_resource_sufficient(drink):
            if money_process.make_payment(drink.cost):
                coffe_machine.make_coffee(drink)

    print("\n")
