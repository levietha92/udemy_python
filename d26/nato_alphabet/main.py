#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import os
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data

data_dict = {row.letter:row.code for index, row in data.iterrows()}
data_dict

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("What is your name?")
user_input_list = [letter.upper() for letter in user_input]


nato = [data_dict[letter] for letter in user_input_list]    
nato