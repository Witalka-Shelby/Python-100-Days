from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput("Who wins the race?", "Pick a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_start = -60
is_race_on = False

for turtle_nr in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_nr])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_start)
    all_turtles.append(new_turtle)
    y_start += 30

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        location = turtle.position()

        if location[0] > 0:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_guess == turtle.pencolor():
                print(f"You did win, The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost, The {winning_color} turtle is the winner!")
                
            if is_race_on == False:
                break
        
        turtle.forward(random.randint(5, 10))


screen.exitonclick()
