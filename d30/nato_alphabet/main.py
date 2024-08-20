#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import os
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data

data_dict = {row.letter:row.code for index, row in data.iterrows()}
data_dict

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def ask_user():
    user_input = input("What is your name?")
    return user_input

game_is_on = True

while game_is_on:
    try:
        user_input_list = [letter.upper() for letter in ask_user()]
        nato = [data_dict[letter] for letter in user_input_list]
        print(nato)
    except:
        print(f"That is not a letter. Try again")
        ask_user()
    finally:
        if ask_user() == "":
            game_is_on = False