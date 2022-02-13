from tkinter import *

def clicked():
    label3.config(text = float(input.get())* 1.609)


window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

#entry
input = Entry(width=10)
input.grid(column=1,row=0)

#label
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

#button
button = Button(text="Calculate", command=clicked)
button.grid(column=1, row=2)

window.mainloop()
