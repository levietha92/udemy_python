import tkinter
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    new_password = []
    random.ran
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    with open("data.txt", mode="a") as file:
        row_insert = f"{website} | {email} |  {pwd} \n"
        print(row_insert)
        file.write(row_insert)
        # then delete them
        website_entry.delete(0,'end')
        pwd_entry.delete(0,'end')
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
website_entry.focus()

#Email
email_text = tkinter.Label(text="Email/Username", width=15)
email_text.grid(column=0,row=2)

email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"mumbojumbo@gmail.com")

#Password
pwd_text = tkinter.Label(text="Password", width=15)
pwd_text.grid(column=0,row=3)

pwd_entry = tkinter.Entry(width=21)
pwd_entry.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Pwd")
generate_button.grid(column=2,row=3)

#Add button
add_button = tkinter.Button(text="Add",width=32, bg="red", command=add_password)
add_button.grid(column=1,row=4,columnspan=2)

# FUNCTIONS: receive the input when user click ADD, save input to txt file


window.mainloop()