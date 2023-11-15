from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(0.5, 0.5)

    def move_food(self, width, height):
        pos_x = int(width / 2 - 5)
        pos_y = int(height / 2 - 5)
        x = random.randint(-pos_x, pos_x)
        y = random.randint(-pos_y, pos_y)
        return x, y
