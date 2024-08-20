from tkinter import *
from tkinter import messagebox
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
HIGHLIGHT_COLOR = "#FF5733"
FRONTCARD_COLOR = "#FFFFFF"
LANG = "fr"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")

#------------------------------- SETUP DATA -------------------------------#
data = pd.read_csv("data/french_words.csv")
random_index = random.randint(0, len(data))
fr_word = data.iloc[random_index]['French']
en_word = data.iloc[random_index]['English']

#------------------------------- SETUP UI -------------------------------#
# Window
window = Tk()
window.title(f"FlashCard {LANG.upper()} <> EN")
window.minsize(900,726)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Card images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

# Card setup at first
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card.create_image(400,263,image=card_front_img)
card.grid(column=0,row=0, columnspan=2, rowspan=3)

# Title
title_label = Label(text=f"{LANG.upper()}", font=FONT1, bg=FRONTCARD_COLOR)
title_label.grid(column=0,row=0,  columnspan=2)

# Word
word_label = Label(text=fr_word, font=FONT2, bg=FRONTCARD_COLOR)
word_label.grid(column=0,row=1, columnspan=2)

# Right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightcolor=HIGHLIGHT_COLOR, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=3)

# Wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightcolor=HIGHLIGHT_COLOR, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=3)



window.mainloop()