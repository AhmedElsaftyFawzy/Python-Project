# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb = []

# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb.append((red, green, blue))


from turtle import Turtle, Screen, colormode
from random import choice


paint_color = [
                (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
                (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
                (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
                (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                (176, 192, 208), (168, 99, 102)
            ]

colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.teleport(-200, -200)
timmy.hideturtle()
timmy.penup()

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, choice(paint_color))
        timmy.forward(50)
    timmy.teleport(-200)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)



Screen = Screen()
Screen.exitonclick()