from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    counter = 1
    colormode(255)
    tim.color(randint(0, 255),
        randint(0, 255),
        randint(0, 255))
        
    while counter != num_sides + 1:
        tim.forward(60)
        tim.right(angle)
        counter += 1

for i in range(3, 11):
      draw_shape(i)


screen = Screen()
screen.exitonclick()