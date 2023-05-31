from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = {}

words_csv = pandas.read_csv("./day 31/data/french_words.csv")
words_dict = words_csv.to_dict(orient="records")

def get_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(canvas_background, image=card_front_png)
    canvas.itemconfigure(card_language, text="French", fill="black")
    canvas.itemconfigure(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, reveal_card)

    
def reveal_card():
    global current_card
    canvas.itemconfig(canvas_background, image=card_back_png)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    
    

window = Tk()
window.title("Fla5hy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, reveal_card)

# Card Part
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="./day 31/images/card_front.png")
card_back_png = PhotoImage(file="./day 31/images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front_png)
card_language = canvas.create_text(400, 150, text="French", font=("Ariel", "40", "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", "40", "italic"))
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