from tkinter import Tk, Canvas, Label, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
Categories = {
    "25": "Art",
    "18": "Computers",
    "21": "Sports"
}

OPTIONS = ["25", "18", "21"]


class QuizInterface:
    def __init__(self, question: QuizBrain):
        self.quiz = question

        self.window = Tk()
        self.window.title("Quizer")
        self.window.config(width=350, height=450, padx=20, pady=20, background=THEME_COLOR)
        self.score = Label(text=f"Score: 0", font=FONT, fg="white",
                           background=THEME_COLOR)
        self.score.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Text", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        yes_img = PhotoImage(file="images/true.png")
        no_img = PhotoImage(file="images/false.png")
        self.button_yes = Button(image=yes_img, highlightthickness=0, bd=0, command=self.answer_true)
        self.button_yes.grid(row=2, column=0)
        self.button_no = Button(image=no_img, highlightthickness=0, bd=0, command=self.answer_false)
        self.button_no.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(background="white")
            self.score.config(text=f"{self.quiz.score} / {self.quiz.question_number}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text.capitalize())
        else:
            self.canvas.itemconfig(self.question, text="You're reach the end of the Quiz")
            self.canvas.config(background="white")
            self.button_yes.config(state="disabled")
            self.button_no.config(state="disabled")

    def answer_true(self):
        self.answer_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.answer_feedback(self.quiz.check_answer("False"))

    def answer_feedback(self, is_right):
        bg = "green" if is_right else "red"
        self.canvas.config(background=bg, highlightthickness=0, bd=0)
        self.window.after(1000, self.get_next_question)
