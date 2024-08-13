import os

with open("./my_file.txt") as file:
    # /Users/hanna/GitHub/udemy_course/d24/filepath/my_file.txt
    print(file.read())

with open("/Users/hanna/Desktop/my_file.txt") as file:
    print(file.read()+ " with absolute path")

# relative path
with open("../../../../Downloads/my_file.txt") as file:
    print(file.read() + " with relative path")

with open("../../../../Desktop/my_file.txt") as file:
    print(file.read() + " with relative path")
"""
Python: Everything is in forward slash in both Mac and Win
Mac: forward slash, Wins: backslash
../ = going up the folder structure by 1
./ = going down the folder structure by 1
"""    