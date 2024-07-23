rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = [rock, paper, scissors]
choices_str = ["rock","paper","scissors"]

for item in range(0,15):
    # User choice --> print out user choice --> assign number to it
    your_choice_str = input("Your turn -->: ")
    print(f"You chose {your_choice_str}")
    your_choice_num = choices_str.index(your_choice_str)
    your_choice = choices[your_choice_num]
    print(your_choice)
    
    # Computer choice --> convert from number to actual RPS choice
    computer_choice_num = random.randint(0,2)
    computer_choice_str = choices_str[computer_choice_num]
    computer_choice = choices[computer_choice_num]
    print(f"Compute chose --> {computer_choice_str}\n{computer_choice}")
    
    # RSA logic
    
    if your_choice_num == computer_choice_num:
        print("It's a draw")
    elif your_choice_num == 0 and computer_choice_num == 2:
        print("you won!")
    elif your_choice_num == 2 and computer_choice_num == 0:
        print("you lost :(")
    elif your_choice_num != 0 or your_choice_num != 2:
        if your_choice_num > computer_choice_num:
            print("you won!")
        elif your_choice_num == computer_choice_num:
            print("its a draw")
        elif your_choice_num < computer_choice_num:
            print("you lost :(")
    else:
        print("huh??")