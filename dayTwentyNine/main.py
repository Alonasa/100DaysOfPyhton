# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import Tk, Canvas, PhotoImage

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.resizable(False, False)
window.title("Password manager")

screen_width = window.winfo_screenwidth()
canvas = Canvas(width=400, height=500, background="#ffffff")
main_img = PhotoImage(file="logo.png")
canvas.create_image(200, 120, anchor="center", image=main_img)

canvas.grid()

window.mainloop()
