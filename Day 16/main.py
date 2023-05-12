from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True


while is_on:
    coffee_list = menu.get_items()
    coffee_choice = input(f"What would you like? ({coffee_list}): ").lower()

    if coffee_choice == "report":
        coffe_maker.report()
        money_machine.report()
        
    elif coffee_choice == "off":
        is_on = False

    else:
        user_choice = menu.find_drink(coffee_choice)
        coffee_cost = user_choice.cost

        if coffe_maker.is_resource_sufficient(user_choice) and money_machine.make_payment(coffee_cost):
            coffe_maker.make_coffee(user_choice)