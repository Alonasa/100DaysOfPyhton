# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import tkinter
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
import re

from dayFive.password_generator import generate_password
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #


def validate_email(mail):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, mail):
        return True
    else:
        return False


def save():
    website_info = website_entry.get().lower()
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
                        item = {
                            website_info: {
                                "email": email_info,
                                "password": password_info
                            }
                        }
                        try:
                            with open("passwords.json", "r") as pass_data:
                                data = json.load(pass_data)

                        except FileNotFoundError:
                            with open("passwords.json", "w") as pass_data:
                                json.dump(item, pass_data, indent=2)
                        else:
                            data.update(item)

                        with open("passwords.json", "w") as pass_data:
                            json.dump(data, pass_data, indent=2)

                            website_entry.delete(0, 'end')
                            password_entry.delete(0, 'end')
                        messagebox.showinfo(title="Successful Operation", message="Data was saved")
                    else:
                        messagebox.showinfo(title="Invalid field", message="Email is invalid. Please check your email")

            else:
                messagebox.showinfo(message=f"Field {field.capitalize()} is too short")


def password_gen():
    secure_password = generate_password()
    password_entry.insert(index=0, string=secure_password)
    autoclip(password_entry)


def autoclip(entry):
    entry.clipboard_append(entry.get())


def get_password():
    resource = website_entry.get()
    try:
        with open("passwords.json", "r") as pass_data:
            data = json.load(pass_data)
            item = data[resource.lower()]
            print(item)
            if item:
                email_entry.delete(0, tkinter.END)
                email_entry.insert(string=item["email"], index=0)
                password_entry.delete(0, tkinter.END)
                password_entry.insert(string=item["password"], index=0)

    except KeyError:
        messagebox.showinfo(title="Not Found", message=f"There's no data for {resource.capitalize()}")
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="Theres no any passwords in database")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Not Found", message="Database is empty")


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

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(string="alona@mail.com", index=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=14, command=get_password)
search_button.grid(row=1, column=2, padx=5)
password_button = Button(text="Generate password", command=password_gen)
password_button.grid(row=3, column=2, padx=5, pady=0)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
