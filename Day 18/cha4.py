from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

def random_side():
    side = ["left", "right"]
    pick = random.choice(side)
    if pick == "left":
        return tim.left(90)
    else:
        return tim.right(90)


def random_color():
    colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_shape():
    tim.pensize(5)
    tim.speed(40)
    colormode(255)
    tim.color(random_color())
    random_side()    
    tim.forward(10)
    
for i in range(3, 1000):
    draw_shape()


screen = Screen()
screen.exitonclick()