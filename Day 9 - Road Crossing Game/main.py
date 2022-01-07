import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_forward()

    # detect collision with car
    for car in cars.all_car:
        if player.distance(car) < 27:
            game_is_on = False
            score.game_over()

    # When player cross the road
    if player.ycor() > 280:
        score.new_level()
        player.new_level()



screen.exitonclick()
