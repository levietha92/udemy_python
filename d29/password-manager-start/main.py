import tkinter
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=1)
canvas_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=canvas_image)
canvas.pack()

window.mainloop()