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
canvas.grid(column=1, row=0)

#Website
website_text = tkinter.Label(text="Website", width=15)
website_text.grid(column=0, row=1)

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

#Email
email_text = tkinter.Label(text="Email/Username", width=15)
email_text.grid(column=0,row=2)

email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)

#Password
pwd_text = tkinter.Label(text="Password", width=15)
pwd_text.grid(column=0,row=3)

pwd_entry = tkinter.Entry(width=21)
pwd_entry.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Pwd")
generate_button.grid(column=2,row=3)

#Add button
add_button = tkinter.Button(text="Add",width=32)
add_button.grid(column=1,row=4,columnspan=2)
window.mainloop()