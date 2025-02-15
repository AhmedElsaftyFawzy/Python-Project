from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed(0)
        self.refresh()
        
    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))
