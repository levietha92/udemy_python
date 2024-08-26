from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question

THEME_COLOR = "#063970"
RIGHT_COLOR = "#abdbe3"
WRONG_COLOR = "#873e23"
FONT = ("Arial",30, "normal")

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(bg=THEME_COLOR,padx=50,pady=50)
        self.window.title("Quizzler")

        #question window
        self.canvas = Canvas(width=300,height=250,background="white")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.question_text = self.canvas.create_text(
            150,125,
            text="Question here",
            font=FONT,
            width=280 #this is to wrap the text
            )

        #score
        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=FONT, pady=20)
        self.score.grid(column=1, row=0)

        #button
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.click_true)
        self.true_button.grid(column=1,row=2)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.click_false)
        self.false_button.grid(column=0,row=2)
        
        self.get_next_question()
        
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.score.config(text=f"Score: {self.quiz.user_score}")
            print(f"{self.quiz.question_number} - {question_text}, {self.quiz.current_question.answer}")
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz")

    def click_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=RIGHT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)
        self.window.after(1000,func=self.get_next_question) # this is the key to make it move to next question
