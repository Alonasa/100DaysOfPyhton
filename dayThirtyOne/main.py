from tkinter import Canvas, Tk

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()

window.title("Language Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = Canvas(width=700, height=526, highlightthickness=0, bd=0, background=BACKGROUND_COLOR)

canvas.grid(row=0, column=1)


def create_rounded_rectangle(figure, x1, y1, x2, y2, radius, **kwargs):
    # Calculate coordinates for rounded rectangle
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]

    # Draw rounded rectangle on canvas
    return figure.create_polygon(points, **kwargs, smooth=True)


rounded_rectangle = create_rounded_rectangle(canvas, 0, 0, 700, 526, radius=25, fill="white", outline="")

window.mainloop()
