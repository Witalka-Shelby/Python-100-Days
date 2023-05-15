from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

def draw_circle():
    return tim.circle(100)


def random_color():
    colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_shape():
    tim.pensize(1)
    tim.speed(40)
    colormode(255)
    tim.color(random_color())
    draw_circle()


counter = 0
while counter <= 360:
    draw_shape()
    tim.left(counter)
    counter += 5


screen = Screen()
screen.exitonclick()