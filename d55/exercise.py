# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)  # Unpack args and store the result
        print(f"You called {function.__name__}{(args)}\nIt returned: {result}")
    return wrapper  # Return the wrapper function


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)