from turtle import Turtle

FONT = ("Courier", 14, 'bold')
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.text = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()

    def print_score(self):
        self.write(f"Score: {self.text}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.text += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.text = "GAME OVER"
        self.goto(-120, 0)
        self.color("yellow")
        self.write(self.text, font=("Courier", 40, "bold"))
