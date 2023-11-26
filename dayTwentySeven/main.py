import tkinter

window = tkinter.Tk()
window.title("Mile to kilometers converter")
window.minsize(width=500, height=400)
radio = tkinter.StringVar()
label = tkinter.Label(text="Convert to Kilometers")
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
    text = float(inp.get())
    convert_tokm = text * MILES_DEFAULT
    convert_tomi = text * KM_DEFAULT
    selected = check_selected()
    if selected == "Km":
        label.config(text=f"In a {text} Mile{'s' if text > 1 else ''} {convert_tokm} Kilometers")
    else:
        label.config(text=f"In a {text} Kilometer{'s' if text > 1 else ''} {convert_tomi} Miles")


ki_radio = tkinter.Radiobutton(text="Km", variable=radio, value="Km")
mi_radio = tkinter.Radiobutton(text="Mi", variable=radio, value="Mi")
ki_radio.pack()
mi_radio.pack()

button = tkinter.Button(text="Convert", command=button_clicked)
button.pack()

inp = tkinter.Entry(width=50)
inp.focus()
inp.pack()
inp.get()

window.mainloop()
