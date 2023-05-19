from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 10, "bold")

class Scoreboard(Turtle):
    def __init__(self, player_num) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        if player_num == 2:
            self.goto(200, 270)
        else:
            self.goto(-200, 270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", False, align=ALIGMENT, font=FONT)