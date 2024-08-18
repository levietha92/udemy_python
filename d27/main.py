import tkinter

window = tkinter.Tk()

window.title("Ahoy")
window.minsize(500,300)
window.config(padx=100, pady=100)

label = tkinter.Label(text="Yooohooo", font=("Arial", 30, "italic"))
# label.pack(side='top') # place on the screen, without this it doesnt show
label.grid(column=0, row=0)
label.config(text="New text")

# Button

def button_clicked():
    # print("I got cliked")
    new_text = input.get()
    label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack() #without this it doesn't show
button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3,row=2)

window.mainloop()

"""
Tinkter layout
1. Pack() --> relatively on top on each other, no control from us
2. Place() --> determine the x,y of the widget, scaling up is hard
3. Grid() --> divide the layout into grid and place widget into each of this unit
    , things are put into relative position of each other
Note: do not mix these layouts

Padding
"""