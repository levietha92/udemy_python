import tkinter
import time
import math
"""EVENT DRIVEN GUI --> need some event to be registered and triggering an action
"""

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 1 #5
LONG_BREAK_MIN = 1 #20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    #dynamic typing is possible in python!
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(countdown_text, text=f"{count_min}:{count_sec}")
    # print(f"{count_min}:{count_sec}")
    if count > 0:
        window.after(100, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

# Windows
window = tkinter.Tk()
window.title("Podomoroh")
window.config(bg=YELLOW)

# Canvas
canvas = tkinter.Canvas(width=280, height=250,bg=YELLOW, highlightthickness=0)
tomota_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(140,130, image=tomota_img)

countdown_text = canvas.create_text(140,145, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)
# count_down(5)

# Texts
timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME,50,"normal"))
timer.grid(column=1, row=0)

checkmark = tkinter.Label(text="✅", bg=YELLOW, highlightthickness=0)
checkmark.grid(column=1, row=2)

# Buttons
left_button = tkinter.Button(text="Start", font=(FONT_NAME,20,"bold"), bg=YELLOW, highlightthickness=0, command=start_timer)
left_button.grid(column=0, row=2)
right_button = tkinter.Button(text="Reset", font=(FONT_NAME,20,"bold"), bg=YELLOW, highlightthickness=0)
right_button.grid(column=2,row=2)



window.mainloop()