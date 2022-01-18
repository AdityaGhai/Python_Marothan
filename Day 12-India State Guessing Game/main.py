import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=750, height=800)
image = "india_states.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_loc(x,y):
#     print(f"{int(x)},{int(y)}")
# turtle.onscreenclick(get_mouse_loc)

data = pd.read_csv("states_data.csv")
all_states = data.state.to_list()

guessed_states=[]
learn_states = []
while len(guessed_states)<30:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct",
                                    prompt="What the other state's name:").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

for state in all_states:
    if state not in guessed_states:
        learn_states.append(state)
learn_csv=pd.DataFrame(learn_states)
learn_csv.to_csv("Learn_States.csv", index=False)
