from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_segment = []
        self.create_snake()
        self.head = self.all_segment[0]

    def create_snake(self):
        for position in START_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.all_segment.append(new_segment)

    def move(self):
            for segment in range(len(self.all_segment) - 1, 0, -1):
                x_cor = self.all_segment[segment - 1].xcor()
                y_cor = self.all_segment[segment - 1].ycor()
                self.all_segment[segment].goto(x_cor, y_cor)
            self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)