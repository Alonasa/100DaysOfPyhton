from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
WIDTH = 500
HEIGHT = 500
MAX_X = int(WIDTH / 2) - 7
MAX_Y = int(HEIGHT / 2) - 7
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()
new_food = Food()
score = Score(MAX_Y)

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.turn_left, "Left")
screen.onkey(new_snake.turn_right, "Right")

game_play = True

while game_play:
    screen.update()
    time.sleep(0.05)
    new_snake.move()
    check_pos = new_food.pos()

    if new_snake.head.distance(new_food) < 6:
        score.increase_score()
        new_snake.eat_food()
        new_snake.update()
        new_food.move_food(MAX_X, MAX_Y)

    if (new_snake.head.xcor() > MAX_X or new_snake.head.xcor() < -MAX_X or
            new_snake.head.ycor() > MAX_Y or new_snake.head.ycor() < -MAX_Y):
        score.reset()
        new_snake.reset()

    for part in new_snake.snake_body[1:]:
        if part == new_snake.head:
            pass
        elif new_snake.head.distance(part) < 2:
            score.reset()
            new_snake.reset()

screen.exitonclick()
