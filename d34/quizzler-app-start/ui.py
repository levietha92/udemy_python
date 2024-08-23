from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=50, pady=50)
        # self.window.minsize(400,600)
        
        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50) #this padY is how we create space between the canvas and buttons
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "normal"))
        self.score_label.grid(column=1,row=0)

        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 30, "bold"))
        
        self.get_next_question()
    
        right_button_img = PhotoImage(file="images/true.png")
        wrong_button_img = PhotoImage(file="images/false.png")
        self.right = Button(image=right_button_img, highlightthickness=0)
        self.right.grid(column=0, row=2)
        self.wrong = Button(image=wrong_button_img, highlightthickness=0)
        self.wrong.grid(column=1, row=2)
        
        self.window.mainloop()


    def get_next_question(self):
        qtext = self.quiz.next_question
        self.canvas.itemconfig(self.question_text,text=qtext)