from art import logo
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list):
    """Take a list of cards and calculate teh sum of it"""
    if len(list) == 2 and sum(list) == 21:
        return 0
    
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    
    return sum(list)

def compare(u_score, c_score):
    """compare both scores"""
    if u_score == comp_score:
        return print("It's a draw")
    elif c_score == 0:
        return print("Comp Wins")
    elif u_score == 0:
        return print("User Wins")
    elif u_score > 21:
        return (print("User loses"))
    elif c_score > 21:
        return (print("Comp loses"))
    elif u_score > c_score:
        return print("User Wins")
    else:
        return print("Comp Wins")
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards} and your score {user_score}")
        print(f"Computers first card {user_cards[0]}")


        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:        
            draw_another_card = input("Draw another card? y or n: ")
            if draw_another_card == "y":
                user_cards.append(deal_card())

            else:
                while comp_score < 17 and comp_score != 0:
                    computer_cards.append(deal_card())
                    comp_score = calculate_score(computer_cards)
                is_game_over = True

        compare(u_score=user_score, c_score=comp_score)

while input("restart game? Type y or n: ") == "y":
    os.system("cls")
    play_game()