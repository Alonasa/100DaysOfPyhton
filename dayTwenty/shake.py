from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Turtle()
snake.shape("square")
snake.shapesize(0.2, 0.8)
snake.color("white")

dot = Turtle()
dot.shape("square")
dot.shapesize(0.2, 0.2)
dot.color("white")
dot.penup()
dot.goto(x=50.0, y=0.0)

screen.exitonclick()
