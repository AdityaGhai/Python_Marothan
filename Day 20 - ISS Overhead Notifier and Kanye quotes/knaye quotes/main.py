from tkinter import *
import requests

def get_quote():
    api = requests.get("https://api.kanye.rest")
    quotes = api.json()["quote"]
    canvas.itemconfig(quote, text=quotes)

window = Tk()
window.title("Kanye says...")
window.config(pady=50, padx=50)

#creating canvas
canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=bg_img)
quote = canvas.create_text(150, 207, text="kanye quotes here", width=250, font=("Arial", 18, "bold"))
canvas.grid()

# creating button
emoji_img = PhotoImage(file="kanye.png")
button = Button(image=emoji_img, highlightthickness=0, command= get_quote)
button.grid()

window.mainloop()