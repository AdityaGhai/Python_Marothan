from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(360)
l_paddle = Paddle(-360)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # detect the collision of ball with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect when ball miss the right paddle
    if ball.xcor() > 380:
        ball.restart()
        score.l_point()

    # detect if ball miss the left paddle
    if ball.xcor() < -380:
        ball.restart()
        score.r_point()

    # Game over when anyone score 5 points
    if score.l_score == 5 or score.r_score == 5:
        game_is_on = False
        score.game_end()

screen.exitonclick()
