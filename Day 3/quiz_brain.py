class QuizBrain:

    def __init__(self, q_bank):
        self.question_no = 0
        self.score = 0
        self.question_text = q_bank

    def still_question(self):
        return self.question_no < len(self.question_text)


    def new_question(self) -> object:
        current_question = self.question_text[self.question_no].text
        answer = self.question_text[self.question_no].answer
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {current_question} (True/False)? ")
        self.answer_evalute(user_ans, answer)


    def answer_evalute(self, u_ans , correct_ans):
        if u_ans.lower() == correct_ans.lower():
            self.score += 1
            print("Yes:) you got it right!")
        else:
            print("No:( your answer is wrong")
        print(f"The correct answer is {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_no}\n")
