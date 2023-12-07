from tkinter import Tk, Canvas

THEME_COLOR = "#375362"

window = Tk()
window.title("Quizer")

canvas = Canvas(width=350, height=450)
canvas.grid(row=0, column=1)

window.mainloop()
