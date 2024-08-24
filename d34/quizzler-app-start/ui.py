from tkinter import *

THEME_COLOR = "#063970"
FONT = ("Arial",30, "normal")

class QuizUI:
    def __init__(self):
        self.window = Tk()
        self.window.config(bg=THEME_COLOR,padx=50,pady=50)
        self.window.title("Quizzler")

        #question window
        self.canvas = Canvas(height=250,width=300,background="white")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.canvas.create_text(140,130,text="Question here",font=FONT)

        #score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=FONT, pady=20)
        self.score.grid(column=1, row=0)

        #button
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=1,row=2)
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=0,row=2)
        
        
        
        
        self.window.mainloop()
