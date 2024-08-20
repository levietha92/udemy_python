from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
HIGHLIGHT_COLOR = "#FF5733"

FRONTCARD_COLOR = "#FFFFFF"
BACKCARD_COLOR = "#94c3ab"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")
WAIT_TIME = 3000 #miliseconds
timer = None
random_index = None
fr_word = ""
en_word = ""
learned = [["French", "English"]]

#------------------------------- FUNCTIONS -------------------------------#
def show_answer():
    global random_index, fr_word, en_word
    # change card to back
    card.create_image(400,263,image=card_back_img)
    # replace fr_word with en_word
    word_label.config(text=en_word, bg=BACKCARD_COLOR)
    # replace title with English
    title_label.config(text="English", bg=BACKCARD_COLOR)
    # when users cannot guess then they clicked this option, so this word should be kept in to_learn
    learned.append([fr_word,en_word])
    pd.DataFrame(learned).to_csv("data/learned.csv")
    
def countdown():
    global timer
    timer = window.after(WAIT_TIME, func=show_answer)

def next_word():
    global random_index, fr_word, en_word
    random_index = random.randint(0, len(data)-1)
    fr_word = to_learn.iloc[random_index]['French']
    en_word = to_learn.iloc[random_index]['English']
    print(random_index, fr_word, en_word)
    # change card to front
    card.create_image(400,263,image=card_front_img)
    # replace new fr_word
    word_label.config(text=fr_word, bg=FRONTCARD_COLOR)
    # replace title with LANG
    title_label.config(text="French", bg=FRONTCARD_COLOR)
    countdown() #thought of this correctly, yey
    # when users guess correctly, this word should be removed from to_learn
    to_learn.drop(axis=0, index=random_index, inplace=True)
    to_learn.to_csv("data/to_learn.csv")

#------------------------------- SETUP DATA -------------------------------#
data = pd.read_csv("data/french_words.csv")
to_learn = data #.to_dict(orient="records")
#the course used to_learn = data.to_dict(orient="records")
#that way it's easier to add and remove from the dict

#------------------------------- SETUP UI -------------------------------#
# Window
window = Tk()
window.title(f"FlashCard")
window.minsize(900,726)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Card images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

# Card setup at first
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card.create_image(400,263,image=card_front_img)
card.grid(column=0,row=0, columnspan=2, rowspan=3)

# Title -- the course used canvas.create_text() instead
title_label = Label(text="French", font=FONT1, bg=FRONTCARD_COLOR)
title_label.grid(column=0,row=0,  columnspan=2)

# Word -- the course used canvas.create_text() instead
word_label = Label(text="Word", font=FONT2, bg=FRONTCARD_COLOR)
word_label.grid(column=0,row=1, columnspan=2)

# Right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightcolor=HIGHLIGHT_COLOR, bg=BACKGROUND_COLOR, command=next_word)
right_button.grid(column=1, row=3)

# Wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightcolor=HIGHLIGHT_COLOR, bg=BACKGROUND_COLOR, command=show_answer)
wrong_button.grid(column=0, row=3)

#------------------------------- UX -------------------------------#
# by default after 3 seconds it should show the answer
# countdown()

window.mainloop()