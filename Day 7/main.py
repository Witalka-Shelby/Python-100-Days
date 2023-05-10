import hangman_art
import hangman_words
import random

print(hangman_art.logo)

hangman_word = random.choice(hangman_words.word_list)
hangman_word_list = list(hangman_word)
censored_word = []

for letter in hangman_word:
    censored_word.append("_")

print(hangman_word)
# print(" ".join(censored_word))
# print(len(hangman_art.stages))

wrong_counter = 0
while "_" in censored_word and wrong_counter != 7:
    print(" ".join(censored_word))
    user_input = input("Guess a letter: ")
    if user_input not in hangman_word_list:
        wrong_counter += 1
        print(f"You guessed {user_input}, that's not in the word. You lose a life")
    else:
        print("You guessed a letter")
        for count, letter in enumerate(hangman_word_list):
            if letter == user_input.lower():
                censored_word[count] = letter
    print(hangman_art.stages[len(hangman_art.stages) - 1 - wrong_counter])

if wrong_counter == 7:
    print("Game over")
else:
    print("Won")