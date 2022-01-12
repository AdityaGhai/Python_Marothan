from turtle import Screen
from snake import Snake
from food import Food
from scroeboard import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

saap = Snake()
khana = Food()
scoreboard = Score()

screen.listen()
screen.onkey(saap.up, "Up")
screen.onkey(saap.down, "Down")
screen.onkey(saap.left, "Left")
screen.onkey(saap.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    saap.move()

    #detect collision with food
    if saap.head.distance(khana) < 15:
        khana.refresh()
        saap.extend()
        scoreboard.refresed_score()

    #detect collision with wall
    if saap.head.xcor() > 280 or saap.head.xcor() < -280 or saap.head.ycor() > 280 or saap.head.ycor() < -280:
        scoreboard.score_reset()
        saap.reset()

    # detect collision with tail
    for segment in saap.all_segment[1:]:
        if saap.head.distance(segment) < 12:
            scoreboard.score_reset()
            saap.reset()



screen.exitonclick()
