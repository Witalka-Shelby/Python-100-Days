from turtle import Turtle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ALIGMENT = "center"
FONT = ("Arial", 10, "bold")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        with open("highscore.txt") as score_in_txt:
            highscore_txt = int(score_in_txt.read())

        self.color("white")
        self.penup()
        self.score = 0
        self.high_score = highscore_txt
        self.setpos(0, 270)
        self.hideturtle()

        self.refresh_score()
    

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("highscore.txt", "w") as score_in_txt:
            score_in_txt.write(str(self.high_score))
        
        
    def refresh_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} -- HIGHSCORE: {self.high_score}", False, align=ALIGMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGMENT, font=FONT)