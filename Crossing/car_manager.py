COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle 
from random import randint

class CarManager:
    def __init__(self):
        self.all_cars = [] 
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1,8)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(COLORS[randint(0,5)])
            new_car.penup()
            new_car.goto(300,randint(-250,250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed) 

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
