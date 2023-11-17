from turtle import Turtle


class Score(Turtle):
    def __init__(self, y):
        super().__init__()
        self.text = 0
        self.penup()
        self.goto(0, y - 20)
        self.color("white")
        self.hideturtle()
