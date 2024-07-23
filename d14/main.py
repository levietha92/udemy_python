from game_data import data
import art
from replit import clear
import random
import pandas as pd

length = len(data)

# Prepare the lists
name = []
follower_count = []
description = []
country = []

for i in range(0,length):
  name.append(data[i]['name'])
  follower_count.append(data[i]['follower_count'])
  description.append(data[i]['description'])
  country.append(data[i]['country'])

    
# FUNCTIONS
def randomize():
    random_index = []
  
    for i in [0,1]:
      random_index.append(random.randrange(0,length))
    return random_index


def generate_pair():
  random_index = randomize()
  random_name = []
  random_follower_count = []
  random_description = []
  random_country = []
  
  for i in [0,1]:
    random_name.append(name[random_index[i]])
    random_follower_count.append(follower_count[random_index[i]])
    random_description.append(description[random_index[i]])
    random_country.append(country[random_index[i]])
    
  
  print(f""" ---------------------------------------------
    Compare A: {random_name[0]}, a {random_description[0]}, from {random_country[0]}\n
          {art.vs}\n
          Against B: {random_name[1]}, a {random_description[1]}, from {random_country[1]}
  """)
  return random_follower_count

def play():
  random_follower_count = generate_pair()
  count_a = random_follower_count[0]
  count_b = random_follower_count[1]

  global user_score, correct_answer
  
  user_answer = input("Who has more followers? Type A or B: ")

  if count_a > count_b:
    correct_answer = "A"
  elif count_a < count_b:
    correct_answer = "B"

  if user_answer == correct_answer:
    user_score +=1
    print(f"You are correct! Score = {user_score}")
  else:
    print(f"You are wrong. Game over. Final score = {user_score}")
    user_score = -1
  return user_score
  

# PLAY SCRIPT
print(art.logo)
user_score = 0
correct_answer = ""

while user_score >= 0:
  play()
  





