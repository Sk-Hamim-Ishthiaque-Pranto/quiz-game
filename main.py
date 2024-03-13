from data import question_data1
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data1:
    question_bank.append(Question(i['question'], i['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_a_question():
    quiz.next_question()

print("You have completed the quiz 😄")
print(f"Your Final score is {quiz.correct_count}")
