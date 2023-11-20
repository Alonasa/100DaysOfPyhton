import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        car = Turtle("square")
        car.shapesize(0.5, 2.5)
        y_pos = random.randint(-260, 290)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300, y_pos)
        self.cars.append(car)
        self.hideturtle()

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
