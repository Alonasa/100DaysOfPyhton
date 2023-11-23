from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Courier", 8, "bold")

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
x = data["x"].tolist()
y = data["y"].tolist()
print(states)

counter = 0
count_states = len(states)
correct = 0
while counter <= count_states:
    counter += 1
    answer = screen.textinput(title=f"{correct}/{count_states} States Correct",
                              prompt="What's another State name?").title()
    if answer in states:
        correct += 1
        idx = states.index(answer)
        t = Turtle()
        t.penup()
        t.goto(x[idx], y[idx])
        t.hideturtle()
        t.text = answer
        t.write(f"{t.text}", align="center", font=FONT)

screen.exitonclick()
