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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Create Title "Timer" label
label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

# Create Title "Break" label
# label_title = Label(text="Break", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
# label_title.grid(column=1, row=0)

# Create canvas with image and timer text
canvas = Canvas(width=204, height=226, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 113, image=tomato_image)
canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Create Start and Reset buttons
button_start = Button(text="Start", bg="white", font=(FONT_NAME, 10, "bold"), borderwidth=0, border="0",
                      highlightthickness=0, relief="flat")
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", bg="white", font=(FONT_NAME, 10, "bold"), borderwidth=0, border="0",
                      highlightthickness=0, relief="flat")
button_reset.grid(column=2, row=2)

# Create Checkmark
loop = 1
text = "✔" * loop
checkmark = Label(text=text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
checkmark.grid(column=1, row=3)


window.mainloop()
