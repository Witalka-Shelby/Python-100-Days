from menu import MENU
from menu import resources


def report(c_resources):
    """print current_resources"""
    global money
    water = c_resources['water']
    milk = c_resources['milk']
    coffee = c_resources['coffee']
    report = f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g
Money: ${money}"""
    
    return print(report)


def user_input(u_input, menu_list):
    items_menu_list = []
    for item in menu_list:
        items_menu_list.append(item)

    if u_input in items_menu_list:
        return u_input
        
    elif u_input == "report":
        return u_input
        
    elif u_input == "off":
        return False
    
    else:
        print("Pick one Coffee")


def resources_check(user_pick):
    """checks all ingredients"""
    global MENU
    global current_resources
    check = []
    for ingredient in MENU[user_pick]['ingredients']:
        ingredient_cost = MENU[user_pick]['ingredients'][ingredient]
        if ingredient_cost < current_resources[ingredient]:
            check.append(True)
        else:
            print(f"Sorry not enough {ingredient}")
            check.append(False)
    
    return check


def calc_coins():
    """calc all inserted coins"""
    print("Please insert coins.")
    money_value = int(input("how many quarters?: ")) * 0.25
    money_value += int(input("how many dimes?: ")) * 0.10
    money_value += int(input("how many nickles?: ")) * 0.05
    money_value += int(input("how many penniess?: ")) * 0.01
    return money_value


current_resources = resources

money = 0

is_on = True

while is_on:
    coffee_pick = input("What would you like? (espresso/latte/cappuccino): ").lower()
    user_pick = user_input(u_input=coffee_pick, menu_list=MENU)

    if user_pick == False:
        is_on = False

    elif user_pick == "report":
        report(current_resources)

    elif user_pick == "espresso" or user_pick == "latte" or user_pick == "cappuccino":
        are_there_enough_resources = resources_check(user_pick)

        if False in are_there_enough_resources:
            print("restart")

        all_coins = calc_coins()
        
        coffee_cost = MENU[user_pick]['cost']

        if all_coins >= coffee_cost:
            exchange = all_coins - coffee_cost
            print(f"Here is your exchange {round(exchange, 3)}")
            money += coffee_cost

            # temp = MENU[user_pick]['ingredients']

            for ingredient in MENU[user_pick]['ingredients']:
                # print(MENU[user_pick]['ingredients'][ingredient])
                current_resources[ingredient] -= MENU[user_pick]['ingredients'][ingredient]
            
            print(f"Here is your {user_pick.title()}")
        else:
            print("Not enough Coins")