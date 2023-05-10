from art import logo
import random

def play_blackjack():
    global game
    print(logo)
    player_cards = [draw_card(), draw_card()]
    print(player_cards)
    computers_card = [draw_card()]
    print("".join(str(computers_card)))
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        computers_card.append(draw_card())
        player_cards.append(draw_card())
        print(f"You picked a {player_cards[-1]}")
    else:
        computers_card.append(draw_card())
    
    while sum(computers_card) < 17:
        computers_card.append(draw_card())
    

    sum_player = sum(player_cards)
    sum_computer = sum(computers_card)
    print(f"Your final hand: {player_cards}: {sum_player}")
    print(f"Computer's final hand: {computers_card}: {sum_computer}")

    if sum_player > 21 or sum_computer > 21:
        if sum_player > 21:
            print("You lose")
            return
        else:
            print("Dealer lose")
            return

    if sum(player_cards) > sum(computers_card):
        print("You Win")
    else:
        print("You lose")


    another_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if another_game == "y":
        another_game = ""
        play_blackjack()
    else:
        game = False
        return


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    picked_card = random.choice(cards)
    if picked_card == 11:
        while picked_card != 11 or picked_card != 1:
            picked_card = int(input("Type 11 or 1"))
            print("Just 1 or 11 allowed !!")
    return picked_card

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_blackjack()

print("Game finished")