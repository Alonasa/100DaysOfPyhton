from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(0.3, 0.3)
        self.speed("fastest")

    def move_food(self, width, height):
        x = random.randint(-width, width)
        y = random.randint(-height, height)
        self.goto(x, y)
