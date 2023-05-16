from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def reset_game():
    tim.home()
    tim.clear()

def move(key):
    pass


screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset_game)
screen.listen()

screen.exitonclick()