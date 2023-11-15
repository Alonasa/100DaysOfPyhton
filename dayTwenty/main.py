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
    check_pos = new_food.pos()

    if new_snake.head.distance(new_food) < 7:
        new_snake.eat_food()
        new_snake.grow_snake()
        new_food.move_food(WIDTH - 5, HEIGHT - 5)

screen.exitonclick()
