from tkinter import Canvas, Tk, Button, PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
font = ("Ariel", 40, "italic")

window.title("Language Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bd=0, background=BACKGROUND_COLOR)

card_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, anchor="center", image=card_img)
canvas.grid(row=0, column=1, columnspan=2, rowspan=2)
canvas.create_text(400, 150, text="Title", font=font)
canvas.create_text(400, 250, text="Description", font=(font, 50, "bold"))

right_img = PhotoImage(file="images/right.png")
left_img = PhotoImage(file="images/wrong.png")
button_right = Button(image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, bd=0)
button_right.grid(row=3, column=1)
button_left = Button(image=left_img, background=BACKGROUND_COLOR, highlightthickness=0, bd=0)
button_left.grid(row=3, column=2)
window.mainloop()
