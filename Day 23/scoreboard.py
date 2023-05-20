from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = 0
        self.refresh_score()
        
    def refresh_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, font=FONT)