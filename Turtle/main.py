from turtle import Turtle, Screen, colormode
from random import randint, choice

tim = Turtle()
tim.shape("turtle")
colormode(255)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# for _ in range(20):
#     for _ in range(1):
#         tim.pendown()
#         tim.forward(5)
#     for _ in range(1):
#         tim.penup()
#         tim.forward(5)   


# n = 3

# def draw(n):
#     tim.pencolor(randint(0, 255) , randint(0, 255) , randint(0, 255))
#     for _ in range(n):
#         tim.forward(50)
#         tim.right(360/n)

# for i in range(0, 10):
#     draw(n + i)


# directions = [tim.forward, tim.back, tim.right, tim.left]

# tim.speed(0)
# tim.pensize(10)
# for _ in range(200):
#     tim.pencolor(randint(0, 255) , randint(0, 255) , randint(0, 255))
#     choice(directions)(90)


tim.speed("fastest")
for i in range(1, int(360 / 5) +1):
    tim.pencolor(randint(0, 255) , randint(0, 255) , randint(0, 255))
    tim.circle(100)
    tim.setheading(i*5)



screen = Screen()
screen.exitonclick()
