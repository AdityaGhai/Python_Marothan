from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: 0", bg=THEME_COLOR, pady=20, fg="white", font=("Arial", 10, "bold"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_txt = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Here the question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.button_right = Button(image=right_img, highlightthickness=0, command=self.true)
        self.button_right.grid(row=2, column=0)

        self.button_wrong = Button(image=wrong_img, highlightthickness=0, command=self.false)
        self.button_wrong.grid(row=2, column=1)
        self.next_ques()


        self.window.mainloop()

    def next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_txt, text=question)

        else:
            self.canvas.itemconfig(self.canvas_txt, text="You have completed the quiz.")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def true(self):
        self.ans_check(self.quiz.check_answer("True"))


    def false(self):
        self.ans_check(self.quiz.check_answer("False"))

    def ans_check(self, check_ans):
        if check_ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_ques)


