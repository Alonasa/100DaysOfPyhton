from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, width):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(width, 0)
