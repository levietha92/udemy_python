import tkinter

window = tkinter.Tk()

window.title("Ahoy")
window.minsize(500,300)

label = tkinter.Label(text="Yooohooo", font=("Arial", 30, "italic"))
label.pack(side='top') # place on the screen, without this it doesnt show
label.config(text="New text")

# Button

def button_clicked():
    # print("I got cliked")
    new_text = input.get()
    label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack() #without this it doesn't show

# Entry
input = tkinter.Entry(width=10)
input.pack()

window.mainloop()
