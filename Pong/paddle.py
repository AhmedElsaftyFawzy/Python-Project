from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def upward(self):
        y = self.ycor()
        self.goto(self.xcor(), y +20)

    def downward(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)    
