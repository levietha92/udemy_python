import os

with open("./my_file.txt") as file:
    print(file.read())

with open("/Users/hanna/Desktop/my_file.txt") as file:
    print(file.read())