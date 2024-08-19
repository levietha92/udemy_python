# Origin: /Users/hanna/GitHub/udemy_course/d06/pwd_gen.py
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    print("Welcome to the Password Generator!")
    nr_letters= random.randint(7,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password = []

    # replaced for loops with list comprehension

    password = ([random.choice(letters) for index in range(0, nr_letters)]
    + [random.choice(numbers) for index in range(0, nr_numbers)]
    + [random.choice(symbols) for index in range(0, nr_symbols)])

    random.shuffle(password)

    password_str_new = ""
    for i in range(0,len(password)):
      password_str_new += password[i]
    
    print("Password generation completed")
    return password_str_new 
