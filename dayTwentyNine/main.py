# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
import re


# ---------------------------- SAVE PASSWORD ------------------------------- #


def validate_email(mail):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, mail):
        return True
    else:
        return False


def save():
    website_info = website_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()
    is_positive = messagebox.askokcancel(title=website_info,
                                         message=f"You have entered such data:\nEmail: {email_info}\n"
                                                 f"Password: {password_info}\nIs it ok to save?")

    fields = [
        ('website', website_info),
        ('email', email_info),
        ('password', password_info)
    ]
    if is_positive:
        for field, value in fields:
            if len(value) > 8:
                if field == 'email':
                    if validate_email(value):
                        with open("passwords.txt", "a") as pass_data:
                            pass_data.write(
                                f"website: {website_info} | email: {email_info} | password: {password_info}\n")
                            website_entry.delete(0, 'end')
                            password_entry.delete(0, 'end')
                        messagebox.showinfo(title="Successful Operation", message="Data was saved")
                    else:
                        messagebox.showinfo(title="Invalid field", message="Email is invalid. Please check your email")

            else:
                messagebox.showinfo(message=f"Field {field.capitalize()} is too short")


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
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate password")
password_button.grid(row=3, column=2, padx=0, pady=0)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
