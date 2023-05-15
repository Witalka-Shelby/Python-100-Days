from turtle import Turtle, Screen, colormode
import colorgram
import random

def get_colors():
    colors_list = []
    colors_in_jpg = colorgram.extract('C:\\Users\\*******\\Desktop\\Python 100 Days\\Day 18\\*****.jpg', 25)
    for i in colors_in_jpg:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        color = (r, g, b)
        colors_list.append(color)

    return colors_list


def draw_shape():
    global colors
    colormode(255)
    tim.color(random.choice(colors))
    tim.dot(20)
    tim.penup()

tim = Turtle()
colors = get_colors()

y_counter = 0

while y_counter < 500:
    for i in range(1, 11):
        draw_shape()
        tim.forward(50)
    y_counter += 50
    tim.home()
    tim.sety(y_counter)

screen = Screen()
screen.exitonclick()