from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
WIDTH = 1000
HEIGHT = 600
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()
new_food = Food()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.turn_left, "Left")
screen.onkey(new_snake.turn_right, "Right")

no_wall = True

while no_wall:
    screen.update()
    time.sleep(0.2)
    new_snake.move()
    print(new_snake.pos())
    print(new_food.pos())

    if new_snake.pos() == new_food.pos():
        new_snake.eat_food()
        new_snake.create_snake()
        move = new_food.move_food(WIDTH - 5, HEIGHT - 5)
        new_food.goto(move)

screen.exitonclick()
