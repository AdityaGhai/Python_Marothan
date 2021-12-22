from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    new_question = Question(data["question"], data["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_question():
    quiz.new_question()

print("Congratulations You have completed the Quiz.")
print(f"Your score is {quiz.score} out of {quiz.question_no}")