from turtle import Turtle

FONT = ("Courier", 14, 'bold')
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self, y):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, y - 20)
        self.color("white")
        self.hideturtle()
        self.high_score = 0

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.print_score()
