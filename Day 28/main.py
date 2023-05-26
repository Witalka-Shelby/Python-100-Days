
from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✅"
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    global reps
    global marks
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="T!m3R")
    timer_text
    canvas.itemconfig(timer_text, text="00:00")
    marks = ""
    checkmarks_label.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    count_formated = f"{count_min}:{count_sec}"
    # print(count_formated)
    canvas.itemconfig(timer_text, text=count_formated)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        global marks
        for _ in range(math.floor(reps / 2)):
            marks += CHECKMARK

        checkmarks_label.config(text=marks)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("P0m0d0r0")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./day 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer_label = Label(text="T!m3R", font=(FONT_NAME, 25, "bold") , bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_label.grid(column=1, row=0)

checkmarks_label = Label(font=(FONT_NAME, 10, "bold") , fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmarks_label.grid(column=1, row=4)

start_button = Button(text="Start", command=start_timer,highlightthickness=0)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=3)

window.mainloop()