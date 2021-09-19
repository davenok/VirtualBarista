from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from colorama import Fore, Style

my_menu = Menu()
my_barista = CoffeeMaker()
my_cashbox = MoneyMachine()

virtual_barista_running = True
while virtual_barista_running:
    print(f"{Fore.RED}Welcome to the Virtual Barista.{Style.RESET_ALL}")
    print("pssst: SECRET ADMIN COMMANDS:\n[report, refill, quit]")
    user_order = ""
    while user_order == "":
        user_order = input(f"Please enter your order ({my_menu.get_items()}) :").lower()
    if user_order == "quit":
        virtual_barista_running = False
    elif user_order == "report":
        my_barista.report()
        my_cashbox.report()
    elif user_order == "refill":
        my_barista.refill_machine()
    elif user_order not in my_menu.get_items():
        print("Invalid order")
    else:
        print("Looking up recipe")
        order = my_menu.find_drink(user_order)
        # print(f"ORDER: {order}")
        if my_barista.is_resource_sufficient(order):
            print("I can make that! Easy Peasy, just give me some money first!")
            print(f"That will be ${order.cost}")
            if my_cashbox.make_payment(order.cost):
                my_barista.make_coffee(order)
    print("=-=-=-=-=-=-=-=-=-=-=")
