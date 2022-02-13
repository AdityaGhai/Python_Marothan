from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="TIMER", fg=GREEN)
    label_2.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global REPS
    REPS += 1
    work_time = WORK_MIN * 60
    short_time = SHORT_BREAK_MIN * 60
    long_time = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        label_1.config(text="BREAK", fg=RED)
        count_down(long_time)

    elif REPS % 2 ==0:
        label_1.config(text="BREAK", fg=PINK)
        count_down(short_time)

    else:
        label_1.config(text="WORK")
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count//60
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        marks = ""
        for _ in range(REPS//2):
            marks += "✓"
        label_2.config(text = marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=20, padx=50, bg=YELLOW)

#creating canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

#creating button
start_button = Button(text="Start", width=5, command=timer_start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", width=5, command=timer_reset)
reset_button.grid(row=2, column=2)

#label
label_1 = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
label_1.grid(row=0, column=1)

label_2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
label_2.grid(row=3, column=1)




window.mainloop()



