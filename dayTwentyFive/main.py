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
states = data.state.to_list()

counter = 0
count_states = len(states)
correct = 0
guessed_states = []

while counter <= count_states:
    counter += 1
    answer = screen.textinput(title=f"{correct}/{count_states} States Correct",
                              prompt="What's another State name?").title()
    if answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
        
    if answer in states:
        guessed_states.append(answer)
        correct += 1
        idx = states.index(answer)
        t = Turtle()
        t.penup()
        t.hideturtle()
        st = data.y
        location = data[data.state == answer]
        t.goto(int(location.x.iloc[0]), int(location.y.iloc[0]))
        t.text = answer
        t.write(f"{t.text}", align="center", font=FONT)
