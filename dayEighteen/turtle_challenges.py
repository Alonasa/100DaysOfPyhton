from turtle import Turtle, Screen

turtle_char = Turtle()
turtle_char.shape("turtle")
turtle_char.color("green")
count = 0

while count < 4:
    count += 1
    turtle_char.forward(100)
    turtle_char.left(90)

screen = Screen()
