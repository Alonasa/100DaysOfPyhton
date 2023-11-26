import math
from tkinter import Canvas, Tk, PhotoImage, Button, Label

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
raund = 0
timer_switcher = ""


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global raund
    window.after_cancel(timer_switcher)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    raund = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global raund
    raund += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if raund % 8 == 0:
        timer(long_break)
        title_label.config(text="Break", foreground=RED)
    if raund % 2 == 0:
        timer(short_break)
        title_label.config(text="Break", foreground=PINK)
    else:
        timer(work)
        title_label.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def timer(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer_switcher
        timer_switcher = window.after(1000, timer, count - 1)
    else:
        start_timer()
        check_marks = ""
        work_sessions = math.floor(raund / 2)
        for _ in range(work_sessions):
            check_marks += "✔"
        check_mark.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.resizable(False, False)
window.title("Pomodoro")

screen_width = window.winfo_screenwidth()
canvas = Canvas(width=400, height=500, background=YELLOW)
main_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 180, image=main_img)
title_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.place(x=155, y=15)

timer_text = canvas.create_text(200, 200, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

button_start = Button(text="Start", width=10, height=1, background=GREEN, foreground=YELLOW, activebackground=RED,
                      activeforeground=YELLOW, font=(FONT_NAME, 15, "bold"), command=start_timer)
button_start.place(x=35, y=370)

check_mark = Label(height=1, background=YELLOW, foreground=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.place(x=30, y=310)

button_reset = Button(text="Reset", width=10, height=1, background=GREEN, foreground=YELLOW, activebackground=RED,
                      activeforeground=YELLOW, font=(FONT_NAME, 15, "bold"), command=reset_timer)
button_reset.place(x=225, y=370)

window.mainloop()
