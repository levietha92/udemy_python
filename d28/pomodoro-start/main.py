import tkinter
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
countdown_text = "25:00"
start_time = time.time()


def count_down():    
    print("Clicked Start")
    while start_time != time.time():
        elapsed_time = time.time() - start_time #diff, abs seconds
        time_left = WORK_MIN*60 - elapsed_time 
        time_left_c = time.gmtime(time_left)
        countdown_text = f"{time_left_c.tm_min}:{time_left_c.tm_sec}"
        print(countdown_text)

# ---------------------------- UI SETUP ------------------------------- #

# Windows
window = tkinter.Tk()
window.title("Podomoroh")
window.config(bg=YELLOW)

# Canvas
canvas = tkinter.Canvas(width=280, height=250,bg=YELLOW, highlightthickness=0)
tomota_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(140,130, image=tomota_img)

canvas.create_text(140,145, text=countdown_text, fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)
canvas.update()

# Texts
timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME,50,"normal"))
timer.grid(column=1, row=0)

checkmark = tkinter.Label(text="✅", bg=YELLOW, highlightthickness=0)
checkmark.grid(column=1, row=2)
# Buttons
left_button = tkinter.Button(text="Start", font=(FONT_NAME,20,"bold"), bg=YELLOW, highlightthickness=0)
left_button.grid(column=0, row=2)
right_button = tkinter.Button(text="Reset", font=(FONT_NAME,20,"bold"), bg=YELLOW, highlightthickness=0)
right_button.grid(column=2,row=2)



window.mainloop()