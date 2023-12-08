from tkinter import Tk, Canvas, Label, Button, PhotoImage

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, question):
        self.window = Tk()
        self.window.title("Quizer")
        self.window.config(width=350, height=450, padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text="Score: 0", font=FONT, fg="white", background=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, width=280, text=question.capitalize(), font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        yes_img = PhotoImage(file="images/true.png")
        no_img = PhotoImage(file="images/false.png")
        self.button_yes = Button(image=yes_img, highlightthickness=0, bd=0)
        self.button_yes.grid(row=2, column=0)
        self.button_no = Button(image=no_img, highlightthickness=0, bd=0)
        self.button_no.grid(row=2, column=1)
        
        self.window.mainloop()
