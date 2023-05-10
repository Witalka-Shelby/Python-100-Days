from art import logo
from art import vs
from game_data import data
import random


def pick_data(twitter_list):
    picked_data = random.choice(twitter_list)
    return picked_data


def compare_picks(foll_a, foll_b):
    if foll_a > foll_b:
        return "a"
    else:
        return "b"


data_a = pick_data(data)
data_b = pick_data(data)
score = 0

while True:

    followers_a = data_a['follower_count']
    followers_b = data_b['follower_count']

    ###
    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    # print(data_a)
    # print(data_a['name'])

    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
    print(vs)
    print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")

    compare_result = compare_picks(foll_a=followers_a, foll_b=followers_b)

    player_pick = input("Who has more followers? 'A' or 'B': ").lower()

    if player_pick == compare_result:
        print("Win")
        score += 1
        if compare_result == "a":
            data_a = data_a
        else:
            data_a = data_b
        data_b = pick_data(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break