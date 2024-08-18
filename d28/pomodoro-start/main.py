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
start_time = time.time()
elapsed_time = time.time() - start_time #diff, abs seconds
time_left = WORK_MIN*60 - elapsed_time 
time_left_c = time.gmtime(time_left)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Podomoroh")
window.config(bg=YELLOW)

canvas = tkinter.Canvas(width=280, height=250,bg=YELLOW, highlightthickness=0)
tomota_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(140,130, image=tomota_img)
canvas.create_text(140,130, text=f"{time_left_c.tm_min}:{time_left_c.tm_sec}", fill="white", font=(FONT_NAME,35,"bold"))
canvas.pack()


window.mainloop()