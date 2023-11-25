import tkinter

window = tkinter.Tk()
window.title("Mile to kilometers converter")
window.minsize(width=500, height=400)

label = tkinter.Label(text="Kilometers: ")
label.pack()

MILES_DEFAULT = 1.60934


def button_clicked():
    print("I got click")
    text = float(input.get())
    convert = text * MILES_DEFAULT
    label.config(text=f"In a {text} Mile{'s' if text > 1 else ''} {convert} Kilometers")


button = tkinter.Button(text="Convert", command=button_clicked)
button.pack()

input = tkinter.Entry(width=50)
input.pack()
input.get()

window.mainloop()
