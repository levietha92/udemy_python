from tkinter import *
from tkinter import messagebox
from pwd_gen import password_generator
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_insert():
    new_pwd = password_generator()
    pwd_entry.insert(index=0,string=new_pwd)
    pyperclip.copy(new_pwd) # this helps you copy into clipboard
    cfm_popup = messagebox.askyesno(title="Password generated", message=f"Your password is {new_pwd}")
    return cfm_popup
    
def password_confirm():
    if password_insert() != True:
        password_insert()
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    cfm_popup = messagebox.askokcancel(title=website, message=f"You sure?")
    if cfm_popup == True:
        with open("data.txt", mode="a") as file:
            row_insert = f"{website} | {email} |  {pwd} \n"
            print(row_insert)
            file.write(row_insert)   
    # then delete them
    website_entry.delete(0,'end')
    pwd_entry.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=1)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=canvas_image)
canvas.grid(column=1, row=0)

#Website
website_text = Label(text="Website", width=15)
website_text.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#Email
email_text = Label(text="Email/Username", width=15)
email_text.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"mumbojumbo@gmail.com")

#Password
pwd_text = Label(text="Password", width=15)
pwd_text.grid(column=0,row=3)

pwd_entry = Entry(width=21)
pwd_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Pwd", command=password_confirm)
generate_button.grid(column=2,row=3)

#Add button
add_button = Button(text="Add",width=32, bg="red", command=add_password)
add_button.grid(column=1,row=4,columnspan=2)

# FUNCTIONS: receive the input when user click ADD, save input to txt file




window.mainloop()