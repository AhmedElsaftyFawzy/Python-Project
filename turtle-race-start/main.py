from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=500, height=400)
bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race? Enter a color : ")
colors = ["red", "yellow", "blue", "orange", "green", "purple"]

turtles = []
postion = 10

for i in range(0, 6):
    new = Turtle("turtle")
    new.color(colors[i]) 
    new.penup()
    new.goto(x=-240, y=-100 + postion)
    postion +=40
    turtles.append(new)
    

is_race_on = False

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You Won!! The Winner color is {winner}")
            else:
                print(f"You lose!! The Winner color is {winner}")

        turtle.forward(randint(0, 10))
            

screen.exitonclick()