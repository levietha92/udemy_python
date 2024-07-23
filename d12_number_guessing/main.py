#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
from replit import clear

## SET CONSTANT
ATTEMPTS = 2
another = 'y'

## FUNCTIONS
def set_difficulty():
  difficulty = input("Choose level: 'easy' or 'hard'? ")
  if difficulty == 'easy':
    attempts = ATTEMPTS * 2
  else:
    attempts = ATTEMPTS
  print(f"You will have {attempts} attemps to guess")
  return attempts

def play():
  clear()
  print(art.logo)
  print("Welcome to the number guessing game!\n I'm thinking of a number between 1 and 100.")
  number = random.randint(1,101)
  print(f"Psst, the correct answer is {number}")
  
  attempts = set_difficulty()
  
  while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    else:
      print(f"You got it! The answer is {number}")
      attempts = 0
    attempts -= 1
    
    if attempts == 0 and guess != number:
      print("You ran out of attempts. You lost")

## GAME BEGIN
while another == 'y':
  play()
  another = input("another round? y/n ")
else:
  print("Bye")