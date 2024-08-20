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
    print("This will run no matter what happens above")
    file.close()
    print("File is closed, because we didnt' use with block")    