from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list= password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():

    global data
    web_txt = entry_web.get()
    user_txt = entry_email.get()
    pass_txt = entry_pass.get()
    new_data =  {
        web_txt:{
            "Email":user_txt,
            "Password":pass_txt
        }
    }

    if len(user_txt)<1 or len(pass_txt)<1:
        messagebox.showerror(title="Oops", message="Please fill every entry.")

    else:

        is_ok = messagebox.askokcancel(title=web_txt, message=f"These are the details entered: \nEmail: {user_txt} "
                                                              f"\nPassword: {pass_txt} \nIS this Ok to Save?")

        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    # reading the json file
                    data = json.load(file)
                    # updating the data
                    data.update(new_data)

            except FileNotFoundError:
                data = new_data

            finally:
                with open("passwords.json", "w") as f:
                    # writing the updated data on json file
                    json.dump(data, f, indent=4)
                entry_web.delete(0, END)
                entry_pass.delete(0, END)

#---------------------------Password Search-----------------------------#
def search():
    website = entry_web.get()
    try:
        with open("passwords.json", "r") as file:
            pass_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="You haven't saved any passwords yet.")

    else:
        if website in pass_data:
            email_usr = pass_data[website]["Email"]
            password = pass_data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email_usr} \nPassword: {password}")

        else:
            messagebox.showerror(title="Oops", message=f"Sorry, No file name \"{website}\" exists in database")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# creating canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# creating Labels
label_web = Label(text="Website:")
label_web.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

# creating entry
entry_web = Entry(width=35)
entry_web.grid(row=1, column=1)
entry_web.focus()

entry_email = Entry(width=55)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "aditya@email.com")

entry_pass = Entry(width=35)
entry_pass.grid(row=3, column=1)

# creating buttons
button_search = Button(text="Search", width=15, command=search)
button_search.grid(row=1, column=2)

button_gen_pass = Button(text="Generate Password", width=15, command=pass_gen)
button_gen_pass.grid(row=3, column=2)

button_add = Button(text="Add", width=46, command=save_pass)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()
