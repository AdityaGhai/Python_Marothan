from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_bet = False

user_bet = screen.textinput("Place your bet!", "Choose which color turtle will win- ")
colors = ["red", "green", "blue", "orange", "purple"]
y_position = [-100, -50, 0, 50, 100]
all_turtles = []

for turtle in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x =-230, y = y_position[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_bet = True

while is_bet:
    for current_turtle in all_turtles:
        if current_turtle.xcor() > 230:
            is_bet = False
            if current_turtle.pencolor() == user_bet:
                print("Congrats! You have won.The {current_turtle.pencolor()} turtle won the race.")
            else:
                print(f"You've lost! The {current_turtle.pencolor()} turtle won the race.")
        current_turtle.forward(random.randint(0,10))


screen.exitonclick()