from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    quote = response.json()["quote"]
    if response.status_code == 200:
        if len(quote) < 90:
            canvas.itemconfig(quote_text, text=quote)
        else:
            return get_quote()
    else:
        canvas.itemconfig(quote_text, text="Sorry, I am tired((")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 200, text="Kanye Quote Goes HERE", width=285, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
