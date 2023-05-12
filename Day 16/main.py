from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

coffee_list = menu.get_items()
is_on = True


while is_on:
    coffee_choice = input(f"What would you like? ({coffee_list}): ").lower()

    if coffee_choice == "report":
        coffe_maker.report()
        money_machine.report()
        continue
        
    elif coffee_choice == "off":
        is_on = False
        continue

    user_choice = menu.find_drink(coffee_choice)
    
    if user_choice == None:
        continue
    
    check_resources = coffe_maker.is_resource_sufficient(user_choice)
    
    if check_resources == False:
        continue

    coffee_cost = user_choice.cost
    user_payed = money_machine.make_payment(coffee_cost)
    
    if user_payed:
        coffe_maker.make_coffee(user_choice)