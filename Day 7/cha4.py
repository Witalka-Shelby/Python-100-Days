import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6

while not end_of_game:
    user_input = input("Guess a letter: ").lower()
    
    if user_input in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == user_input:
                display[position] = user_input
    else:
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True

    print(display)

    if "_" not in display:
        print("You win")

    print(hangman_art.stages[lives])

print("Game Over")