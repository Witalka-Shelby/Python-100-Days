from turtle import Turtle
DISTANCE_BETWEEN = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_length = 3
        self.snake_body = []
        self.draw_snake()
        self.head = self.snake_body[0]

    def draw_snake(self):
        for i in range(self.snake_length):
            new_body_part = Turtle("square")
            new_body_part.color("white")
            new_body_part.penup()
            if i > 0:
                add_body_to_end = list(self.snake_body[i - 1].position())
                add_body_to_end[0] -= DISTANCE_BETWEEN
                new_body_part.goto(add_body_to_end)
            self.snake_body.append(new_body_part)

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)