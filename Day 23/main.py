import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cr055!ng G4m3")
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()
screen.update()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
game_speed = 0.1

while game_is_on:
    time.sleep(game_speed)
    screen.update()
    car.add_car()

    for car_nr in car.cars:
        if car_nr.xcor() < -280:
            car.reset_car(car_nr)
        
        if car_nr.distance(player) <= 18:
            score.game_over()
            game_is_on = False

    if player.ycor() > 270:
        score.refresh_score()
        player.lvl_up()
        car.car_speed += 1
    
    car.move_left()

screen.exitonclick()