# The error will block subsequent steps from being executed
# Type of errors

## FileNotFoundError
with open("file.txt") as file:
    file.read()

## KeyError
a_dict = {"key":"value"}
value = a_dict["non_existing_key"]

## IndexError
fruit_list = ["apple",'banana']
fruit_list[2]

## TypeError
text = "abc"
print(text + 5)


# We need to catch Exception

try:
    file = open("file.txt")
    a_dict = {"key":"value"}
    # value = a_dict["non_existing_key"]
    value = a_dict["key"]
except FileNotFoundError as error_message:
    file = open("file.txt", mode="w")
    print(f"There was {error_message}")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
    print("This will only run if no exception block occurs")
finally:
    # print("This will run no matter what happens above")
    # file.close()
    # print("File is closed, because we didnt' use with block")
    raise TypeError("an error i made up")

# Try out
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Are you human?")

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except:
        if index > len(fruits):
            print("Fruit pie")

make_pie(4)


# Catch the exception and make sure the code runs without crashing.
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            total_likes += 0
    return total_likes
    print(total_likes)


count_likes(facebook_posts)




