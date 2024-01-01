from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Resets the timer to default settings"""
    global reps
    reps = 0
    window.after_cancel(timer)
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="✔" * reps)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Activates the count_down function which gets the converted number of minutes in seconds by multiplying by 60"""
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 8:
        count_down(long_break_sec)
        label_title.config(text="Break", fg=RED)
    elif reps > 8:
        reset_timer()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Updates the timer on the screen and call itself each 1 second"""
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min if count_min > 9 else "0" + str(count_min)}:"
                                       f"{count_sec if count_sec > 9 else "0" + str(count_sec)}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Because break appears on each 2 reps, divide by 2 to add one checkmark after each work iteration
        checkmark.config(text="✔" * math.floor(reps / 2))
        # Bring the window in front of any application and ring the system sound on each iteration,
        # for user to be alerted of the current stage
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Create Title "Timer" label
label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

# Create canvas with image and timer text
canvas = Canvas(width=204, height=226, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 113, image=tomato_image)
timer_text = canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Create Start and Reset buttons
button_start = Button(text="Start", bg="white", font=(FONT_NAME, 10, "bold"), borderwidth=0, border="0",
                      highlightthickness=0, relief="flat", command=start_timer)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", bg="white", font=(FONT_NAME, 10, "bold"), borderwidth=0, border="0",
                      highlightthickness=0, relief="flat", command=reset_timer)
button_reset.grid(column=2, row=2)

# Create Checkmark
checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
