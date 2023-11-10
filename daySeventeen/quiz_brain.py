class QuizBrain:
    def __init__(self, q_list, q_score):
        self.question_number = 0
        self.question_list = q_list
        self.score = q_score

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_item = self.question_list[self.question_number]
        self.question_number += 1
        question = input(f"{self.question_number}: {q_item.text} True or False ? ").capitalize()
        self.check_answer(question, q_item.answer)

    def check_answer(self, current_question, right_answer):
        if current_question == right_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, wrong answer")
        print(f"The correct answer is {right_answer}")
        print(f"Your current score is: {self.score}/{len(self.question_list)}")
