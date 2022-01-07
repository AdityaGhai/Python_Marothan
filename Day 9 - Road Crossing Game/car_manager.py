from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1000


class CarManager():

    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,8)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1 , stretch_len=random.randint(1,3))
            car.color(random.choice(COLORS))
            car.penup()
            new_y = random.randint(-240, 240)
            car.goto(300, new_y)
            self.all_car.append(car)


    def move_forward(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def new_level(self):
        self.car_speed *= MOVE_INCREMENT
        self.move_forward()
