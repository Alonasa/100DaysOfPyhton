from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(STARTING_POSITION)
        self.right(270)

    def move(self):
        get_y = self.ycor()
        self.goto(0, get_y + 5)
