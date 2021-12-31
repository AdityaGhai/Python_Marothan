from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, 0)


    def go_up(self):
        if self.ycor() < 243:
            new_y = self.ycor() + 20
            self.setposition(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.setposition(self.xcor(), new_y)
