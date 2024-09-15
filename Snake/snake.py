from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

positions = [(0, 0),(-20, 0),(-40, 0)]

class Snake():
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):    
        for position in positions:
            self.add_segment(position)
        
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")    
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())    

    def move(self):
        for index in range(len(self.segments) -1 , 0, -1):
            new_x = self.segments[index -1].xcor()
            new_y = self.segments[index -1].ycor()
            self.segments[index].goto(new_x, new_y)
    
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)            

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]