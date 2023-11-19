import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        cars = []
        self.create_cars()
        self.x_move = MOVE_INCREMENT
        self.y_move = MOVE_INCREMENT
        self.move_cars()

    def create_car(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.shape("square")
        self.shapesize(0.5, 2.5)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x, y)
        self.speed(STARTING_MOVE_DISTANCE)

    def create_cars(self):
        for _ in range(200, 300):
            self.cars.append(self.create_car())

    def move_cars(self):
        for car in self.cars:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            car.goto(new_x, new_y)
