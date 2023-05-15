from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_entry in question_data:
    question_bank.append(Question(question_entry['text'], question_entry['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")