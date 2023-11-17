from turtle import Turtle


class MiddleLine(Turtle):
    def __init__(self, height):
        super().__init__()
        self.penup()
        self.border_h = int(height / 2)

    def dashed(self):
        for _ in range(0, self.border_h - 10, 10):
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(10)

    def draw_dashed(self):
        self.hideturtle()
        self.pensize(5)
        self.goto(0, self.border_h)
        self.color("white")
        self.lt(270)
        self.dashed()
