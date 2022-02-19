from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
word_learn = data.to_dict(orient="records")
random_word = {}

def card_words():
    global random_word, flip_card
    random_word = random.choice(word_learn)
    window.after_cancel(flip_card)
    canvas.itemconfig(cancas_image, image=card_front)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random_word["French"])
    flip_card = window.after(3000, english_ans)

def english_ans():
    canvas.itemconfig(cancas_image, image = card_back)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=random_word["English"])

def right():
    global word_learn
    word_learn = [x for x in word_learn if not (random_word["French"] == x.get("French"))]
    data = pd.DataFrame(word_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    card_words()

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=40, pady=40)
flip_card = window.after(3000, english_ans)

# creating canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
cancas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 30, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# creating buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=right)
right_button.grid(row=1, column=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_words)
wrong_button.grid(row=1, column=0)

card_words()

window.mainloop()
