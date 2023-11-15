from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
WIDTH = 1000
HEIGHT = 600
MAX_X = int(WIDTH / 2) - 5
MAX_Y = int(HEIGHT / 2) - 5
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()
new_food = Food()
score = Score()

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

    if new_snake.head.distance(new_food) < 6:
        score.increase_score()
        new_snake.eat_food()
        new_snake.update()
        new_food.move_food(MAX_X, MAX_Y)
    if new_snake.head.xcor() > MAX_X or new_snake.head.xcor() < -MAX_X or new_snake.head.ycor() > MAX_Y or new_snake.head.ycor() < -MAX_Y:
        score.game_over()
        no_wall = False

screen.exitonclick()
