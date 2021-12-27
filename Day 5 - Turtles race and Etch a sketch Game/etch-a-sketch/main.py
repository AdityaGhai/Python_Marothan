from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    return tim.forward(10)

def move_back():
    return  tim.backward(10)

def rotate_left():
    return tim.left(10)

def rotate_right():
    return tim.right(10)

def delete_stamp():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key="w" , fun=move_forward)
screen.onkey(key="s" , fun=move_back)
screen.onkey(key="a" , fun=rotate_left)
screen.onkey(key="d" , fun=rotate_right)
screen.onkey(key="c" , fun=delete_stamp)



screen.exitonclick()
