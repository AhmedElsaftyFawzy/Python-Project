FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(-210 ,250)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1   
        self.update()

    def game_over(self):
        self.teleport(0,0)
        self.write(f"Game Over", align="center", font=FONT)

