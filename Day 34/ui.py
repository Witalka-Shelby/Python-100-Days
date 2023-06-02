from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.timer = None
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Qu!zZl3R")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.timer = self.window.after(0)

        # score label
        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", "13", "bold"))
        self.score.grid(row=0, column=1)

        # white canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text_canvas = self.canvas.create_text(150, 125, fill=THEME_COLOR, font=("Arial", "20", "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # true button
        true_img = PhotoImage(file="./day 34/images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_btn_meth)
        self.true_btn.grid(row=2, column=0)

        # false button
        false_img = PhotoImage(file="./day 34/images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.fals_btn_meth)
        self.false_btn.grid(row=2, column=1)

        self.get_next_quiz()

        self.window.mainloop()
    
    def get_next_quiz(self):
        self.canvas.configure(bg="white", highlightthickness=0)
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text_canvas, text="No more Questions!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn_meth(self):
        is_rigt = self.quiz.check_answer("True")
        self.give_feedback(is_rigt)
    
    def fals_btn_meth(self):
        is_rigt = self.quiz.check_answer("False")
        self.give_feedback(is_rigt)

    def give_feedback(self, is_rigt):
        if is_rigt:
            self.canvas.configure(bg="green", highlightthickness=0)
        else:
            self.canvas.configure(bg="red", highlightthickness=0)
        
        self.window.after(1000, self.get_next_quiz)