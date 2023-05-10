import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
user_input = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == user_input:
        print("Right")
    else:
        print("Wrong")