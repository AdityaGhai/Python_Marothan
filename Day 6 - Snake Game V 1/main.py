from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

saap = Snake()

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





screen.exitonclick()
