import pandas
from turtle import Screen, Turtle


def get_difference(list_a, list_b):
    return set(list_a)-set(list_b)


us_states = pandas.read_csv("./day 25/50_states.csv")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("./day 25/blank_states_img.gif")
screen.title("Nam3 the Stat3s")

states_to_list = us_states["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name?").title()

    if user_input == "Exit":

        break

    guess = us_states[us_states["state"] == user_input]
    state = guess.state.to_string(index=False)
    if user_input.lower() == state.lower():
        if state in guessed_states:
            continue
        x_cor = int(guess.x.to_string(index=False))
        y_cor = int(guess.y.to_string(index=False))
        turtle.goto(x=x_cor, y=y_cor)
        turtle.write(user_input)
        guessed_states.append(state)

non_match = list(get_difference(states_to_list, guessed_states))
non_match_df = pandas.DataFrame(non_match)
non_match_df.to_csv("./day 25/states_to_learn.csv")