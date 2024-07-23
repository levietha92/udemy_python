#my solution

import art

def add(a,b):
  return a+b

def substract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  if b == 0:
    return None
  else:
    return a/b

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

#the original
# print(art.logo)
# continued = True
# n1 = int(input("What's the first number? "))
# result = 0

# while continued is True:   
#   n1 = n1 if result == 0 else result
    
#   operation = input("\n+\n-\n*\n/\nPick an operation:")
#   n2 = int(input("What's the next number? "))
#   result = operations[operation](n1,n2) # hehehe
#   print(f"{n1} {operation} {n2} = {result}")
#   choice = input(f"Type 'y' to continue calculating with {result},\n or type 'n' to start a new calculation: ")
#   if choice == 'n':
#     continued = False
#     print("Bye")

#making it recursive
def calculator():
  print(art.logo)
  continued = True
  n1 = float(input("What's the first number? ")) #fixing data type
  result = 0
  
  while continued is True:   
    n1 = n1 if result == 0 else result
  
    operation = input("\n+\n-\n*\n/\nPick an operation:")
    n2 = float(input("What's the next number? "))
    result = operations[operation](n1,n2) # hehehe
    print(f"{n1} {operation} {n2} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result},\n or type 'n' to start a new calculation: ")
    if choice == 'n':
      continued = False
      calculator()

calculator()