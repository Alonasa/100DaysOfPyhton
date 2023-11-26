import tkinter

window = tkinter.Tk()
window.title("Mile to kilometers converter")
window.minsize(width=400, height=300)
radio = tkinter.StringVar()
label = tkinter.Label(text=f"Converter")
label.pack()

MILES_DEFAULT = 1.60934
KM_DEFAULT = 0.621371


def check_selected():
    selected_option = radio.get()
    if selected_option == "Km":
        return "Km"
    else:
        return "Mi"


def button_clicked():
    selected = check_selected()
    text = float(get_input.get())
    to_kilometers = text * MILES_DEFAULT
    to_miles = text * KM_DEFAULT
    if selected == "Km":
        label.config(text=f"In a {text} Mile{'s' if text > 1 else ''} {to_kilometers:.2f} Kilometers")
    else:
        label.config(text=f"In a {text} Kilometer{'s' if text > 1 else ''} {to_miles:.2f} Miles")


kilometers_radio = tkinter.Radiobutton(text="Km", variable=radio, value="Km")
miles_radio = tkinter.Radiobutton(text="Mi", variable=radio, value="Mi", tristatevalue=0)
kilometers_radio.place(x=150, y=85)
miles_radio.place(x=200, y=85)

button = tkinter.Button(text="Convert", command=button_clicked)
button.pack()

get_input = tkinter.Entry(width=30)
get_input.focus()
get_input.place(x=110, y=60)
get_input.get()

window.mainloop()
