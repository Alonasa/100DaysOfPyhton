import random
from tkinter import Canvas, Tk, Button, PhotoImage
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")

item = {}


def change_word():
    global item
    item = random.choice(words)
    canvas.itemconfig(card_language, text="French")
    canvas.itemconfig(card_word, text=item["French"])
    return item


def learn_word():
    global item
    canvas.itemconfig(card_language, text="English")
    canvas.itemconfig(card_word, text=item["English"])


# ----------------------- UI------------------------------------------
window = Tk()
font = ("Ariel", 40, "italic")

window.title("Language Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bd=0, background=BACKGROUND_COLOR)

card_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, anchor="center", image=card_img)
canvas.grid(row=0, column=1, columnspan=2, rowspan=2)
card_language = canvas.create_text(400, 150, text="title", font=font)
card_word = canvas.create_text(400, 250, text="Description", font=(font, 50, "bold"))

right_img = PhotoImage(file="images/right.png")
left_img = PhotoImage(file="images/wrong.png")
button_right = Button(image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=change_word)
button_right.grid(row=3, column=1)
button_left = Button(image=left_img, background=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=learn_word)
button_left.grid(row=3, column=2)

window.mainloop()
