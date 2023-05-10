import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")


user_input = input("Guess a letter: ").lower()


for position in range(len(chosen_word)):
    if chosen_word[position] == user_input:
        display[position] = user_input


# for count, letter in enumerate(chosen_word):
#     if letter == user_input:
#         display[count] = letter
#     else:
#         print("")

print(display)