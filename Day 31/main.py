from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Fla5hy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Card Part
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="./day 31/images/card_front.png")
card_back_png = PhotoImage(file="./day 31/images/card_back.png")
canvas.create_image(400, 263, image=card_front_png)
canvas.create_text(400, 150, text="French", font=("Ariel", "40", "italic"))
canvas.create_text(400, 263, text="trovue", font=("Ariel", "40", "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button
wrong_img = PhotoImage(file="./day 31/images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

# Right Button
right_img = PhotoImage(file="./day 31/images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(row=1, column=1)

window.mainloop()