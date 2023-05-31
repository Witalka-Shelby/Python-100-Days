from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

words_csv = pandas.read_csv("./day 31/data/french_words.csv")
words_dict = words_csv.to_dict(orient="records")

def get_word():
    global words_dict
    random_word = random.choice(words_dict)
    test_word = random.choice([random_word["French"], random_word["English"]])
    # print(random_word["French"])
    # print(random_word["English"])
    canvas.itemconfigure(show_word, text=test_word)

window = Tk()
window.title("Fla5hy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Part
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="./day 31/images/card_front.png")
card_back_png = PhotoImage(file="./day 31/images/card_back.png")
canvas.create_image(400, 263, image=card_front_png)
show_language = canvas.create_text(400, 150, text="French", font=("Ariel", "40", "italic"))
show_word = canvas.create_text(400, 263, font=("Ariel", "40", "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button
wrong_img = PhotoImage(file="./day 31/images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=get_word)
wrong_btn.grid(row=1, column=0)

# Right Button
right_img = PhotoImage(file="./day 31/images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=get_word)
right_btn.grid(row=1, column=1)

get_word()

window.mainloop()