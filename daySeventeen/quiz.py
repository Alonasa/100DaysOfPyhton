from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
score = 0

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank, score)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
