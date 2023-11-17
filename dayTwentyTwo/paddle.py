from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.w = width
        self.h = height
        self.goto(self.w, 0)

    def move_up(self):
        if self.ycor() < self.h / 2 - 50:
            y = self.ycor() + 40
            self.goto(self.xcor(), y)
        else:
            self.move_down()

    def move_down(self):
        if self.ycor() > -self.h / 2 + 50:
            y = self.ycor() - 40
            self.goto(self.xcor(), y)
        else:
            self.move_up()
