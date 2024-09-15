from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwords():
    tim.back(10)


def anti_clock_wise():
    tim.left(5)


def clock_wise():
    tim.right(5)    


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwords)
screen.onkey(key="a", fun=anti_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()
