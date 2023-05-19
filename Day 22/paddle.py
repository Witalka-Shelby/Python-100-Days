from turtle import Turtle

DISTANCE_BETWEEN = 20
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, player_num) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        if player_num == 2:
            self.goto(350, 0)
        else:
            self.goto(-350, 0)
        self.color("white")
        self.resizemode("user")
        self.shapesize(1, 5, 1)
        self.setheading(UP)
        

    def up(self):
        if self.ycor() < 240:
            self.forward(MOVE_DISTANCE)


    def down(self):
        if self.ycor() > -240:
            self.backward(MOVE_DISTANCE)