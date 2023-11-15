from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.create_food()
        self.pos = ()

    def create_food(self):
        dot = Turtle("square")
        dot.shapesize(0.5, 0.5)
        dot.color("white")
        dot.penup()
        dot.goto(x=50.0, y=0.0)

    def move_food(self, width, height):
        pos_x = int(width / 2 - 5)
        pos_y = int(height / 2 - 5)
        x = random.randint(-pos_x, pos_x)
        y = random.randint(-pos_y, pos_y)
        return x, y
