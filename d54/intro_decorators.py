import time
# https://replit.com/@appbrewery/python-decorators#main.py


# initially --> add time.sleep to say_hello --> replicate for other functions
def decorator_function(function):
  def wrapper_function():
    function()
  return wrapper_function #without ()

def say_hello():
  time.sleep(2)
  print("Hello")
  
def say_bye():
  print("Bye")

def say_greeting():
  print("Greetings")  
  
  
# there is a better way --> using decorator  

def delay_decorator(function):
  def wrapper_function():
    time.sleep(2)
    function()
  return wrapper_function #without ()

@delay_decorator
def say_hello():
  print("Hello")
  
@delay_decorator  
def say_bye():
  print("Bye")

def say_greeting():
  print("Greetings")  
  
say_hello()
say_greeting()  

# which is the equivalent of using
something = delay_decorator(say_hello)
something()