from tkinter import Canvas, Tk, PhotoImage, Button
import time

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.resizable(False, False)
window.title("Pomodoro")

screen_width = window.winfo_screenwidth()
canvas = Canvas(width=400, height=500, background=YELLOW)
main_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 150, image=main_img)


def timer():
    start_time = time.time()
    while True:
        seconds = time.time()
        time_elapsed = (start_time - seconds) / 60
        print(time_elapsed)
        return str(time_elapsed)


canvas.create_text(200, 170, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

button_start = Button(text="Start", width=10, height=1, background=GREEN, foreground=YELLOW, activebackground=RED,
                      activeforeground=YELLOW, font=(FONT_NAME, 15, "bold"))
button_start.place(x=35, y=320)

button_reset = Button(text="Reset", width=10, height=1, background=GREEN, foreground=YELLOW, activebackground=RED,
                      activeforeground=YELLOW, font=(FONT_NAME, 15, "bold"))
button_reset.place(x=225, y=320)

window.mainloop()
