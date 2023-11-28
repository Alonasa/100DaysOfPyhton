# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.resizable(False, False)
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
main_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, anchor="center", image=main_img)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)
email = Label(text="Email/username: ")
email.grid(row=2, column=0)
password = Label(text="Password: ")
password.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate password")
password_button.grid(row=3, column=2, padx=0, pady=0)
add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
