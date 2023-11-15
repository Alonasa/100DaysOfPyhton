from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 5
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def eat_food(self):
        lenght = len(STARTING_POSITIONS)
        item = STARTING_POSITIONS[lenght - 1][0] - 10
        STARTING_POSITIONS.append((item, 0))
        print(STARTING_POSITIONS)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.shapesize(0.5, 0.5)
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.snake_body.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
