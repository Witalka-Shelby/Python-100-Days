from art import logo
import random

HARD_MODE = 5
EASY_MODE = 10

def guessing(guessed_number, random_number, turns):
    """Checks guessed number if it's random number"""
    if guessed_number == random_number:
        print("You guessed the number.")
        return True, turns
    elif guessed_number > random_number:
        print("Too high.")
        turns -= 1
        return False, turns
    else:
        print("Too low.")
        turns -= 1
        return False, turns

def lives(mode):
    if mode == "hard":
        return HARD_MODE
    else:
        return EASY_MODE

def game():
    print(logo)

    random_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'hard' else game will be easy: ").lower()
    turns = lives(difficulty)

    game_over = False

    while turns != 0 and game_over != True:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        win_game, turns = guessing(guessed_number=guess_number, random_number=random_number, turns=turns)
        if win_game:
            game_over = True


    if win_game == True:
        print("You Won")
    else:
        print("You've run out of guesses, you lose.")

game()