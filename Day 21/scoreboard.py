from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 10, "bold")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.setpos(0, 270)
        self.hideturtle()

        self.refresh_score()
    
    def refresh_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", False, align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGMENT, font=FONT)