from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.sc += 1
        score.rewrite()

    #collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        score.reset()
        snake.reset()

    #collision with the tail
    for sagment in snake.segments[1:]:
        if snake.head.distance(sagment) < 10:
            score.reset()
            snake.reset()





screen.exitonclick()