from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as f:
            self.highscore = int(f.read())
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} HighScore = {self.highscore}", align= ALIGNMENT, font= FONT)

    def refresed_score(self):
        self.score += 1
        self.update_score()

    def score_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)


