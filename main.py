import math
from tkinter import *


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
def start_timer():
    count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Create image for the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00",  fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Status text
status = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
status.config(bg=YELLOW, fg=GREEN)
status.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)


# ✔ Checkmarks
status = Label(text="✔✔✔✔", font=(FONT_NAME, 15, "bold"))
status.config(bg=YELLOW, fg=GREEN)
status.grid(column=1, row=3)

# Reset button
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)












window.mainloop()
