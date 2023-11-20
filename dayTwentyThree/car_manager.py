import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def create_car(self):
        generator = random.randint(1, 6)
        if generator > 4:
            car = Turtle("square")

            car.shapesize(0.5, 2.5)
            y_pos = random.randint(-260, 260)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, y_pos)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
