import tkinter

window = tkinter.Tk()

window.title("Ahoy")
window.minsize(500,300)

label = tkinter.Label(text="Yooohooo", font=("Arial", 30, "italic"))
label.pack(side='top') # place on the screen, without this it doesnt show

window.mainloop()