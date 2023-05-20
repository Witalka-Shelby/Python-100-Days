from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("P0nG")
screen.tracer(0)

# create paddles
paddle_1 = Paddle(1)
paddle_2 = Paddle(2)
pong_ball = Ball()
score_1 = Scoreboard(1)
score_2 = Scoreboard(2)

screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")


game_is_on = True
speed = 0.1

while game_is_on:
    time.sleep(speed)
    screen.update()
    pong_ball.move_ball()
    # print(speed)

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

    if pong_ball.xcor() > 330 and pong_ball.distance(paddle_2) < 50 or pong_ball.xcor() < -330 and pong_ball.distance(paddle_1) < 50:
        pong_ball.bounce_back()
        if speed > 0.01:
            speed -= 0.01
    
    if pong_ball.xcor() > 360:
        score_1.score += 1
        speed = 0.1
        pong_ball.refresh_ball()
        score_1.refresh_score()

    if pong_ball.xcor() < -360:
        score_2.score += 1
        speed = 0.1
        pong_ball.refresh_ball()
        score_2.refresh_score()
 


screen.exitonclick()