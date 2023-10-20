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
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0

    # noinspection TIMER giving a warning
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    status.config(text="Timer")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS = REPS + 1

    work_timer = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    # status = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
    # status.config(bg=YELLOW, fg=GREEN)
    # status.grid(column=1, row=0)

    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        count_down(work_timer)
        status.config(text="Work", bg=YELLOW, fg=GREEN)
        marks = ""
        for _ in  range(math.floor(REPS/2)):
            marks += "✔"
        checkmarks.config(text=marks)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        count_down(short_break)
        status.config(text="Break", bg=YELLOW, fg=PINK)
    elif REPS == 8:
        count_down(long_break)
        status.config(text="BREEEAK", bg=YELLOW, fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()


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
checkmarks = Label(font=(FONT_NAME, 15, "bold"))
checkmarks.config(bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)












window.mainloop()
