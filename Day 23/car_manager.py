from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
START_POINT = -250
END_POINT = 250
MOVE_INCREMENT = 10
CARS_TO_SPAWN = 10

# screen = Screen()

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.counter = 0
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def move_left(self):
        self.car_speed
        for car in self.cars:
            car.forward(self.car_speed)

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.counter += 1
            car = Turtle()
            car.shape("square")
            car.penup()
            car.setheading(180)
            car.goto(300, random.randint(START_POINT, END_POINT))
            car.resizemode("user")
            car.shapesize(1, 2, 1)
            car.color(random.choice(COLORS))
            car.speed(STARTING_MOVE_DISTANCE)
            self.cars.append(car)

    def reset_car(self, car_to_delete):
       car_to_delete.goto(300, random.randint(START_POINT, END_POINT))
