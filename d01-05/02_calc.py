print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Go ahead and ride the rollercoaster!")
else:
  print("Uh oh, you cannot join the ride")
  



#1. Create a greeting for your program.
print("hola alien")
#2. Ask the user for the city that they grew up in.
answer1 = input("whats yo name peasant?")
#3. Ask the user for the name of a pet.
answer2 = input("whats yo pet name?")
#4. Combine the name of their city and pet and show them their band name.
print("your band name is " + answer1 + answer2)
#5. Make sure the input cursor shows on a new line:
input()
# Solution: https://replit.com/@appbrewery/band-name-generator-end





# #Data Types = string
# print("holamahuuahhaa"[-1])
# print("123" + "123")

# for item in 'Zero to Mastery':
#   print(item)

# len("alsdkslakdj")

# # Integers
# print(123 + 123)
# for item in 123:
#   print(item)
# len(123312)
# # Float
# print(123.89 + 123.11)

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# print(type(124))

# Math 
## PEMDAS 
## Continuous operation
score = 1
score += 5 #similarly: -=, *=, /=
print(score)
## Other operations
print(8/3) #getting float
print(8//3) #getting int part

## f string to mix data types
print("your score is " + str(score))
print(f"your score is {score}")
print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(type(a))









#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total = float(input("What was the total bill?"))
tips = int(input("What was the tip amount?"))
persons = int(input("How many people to split the bill?"))
bill_with_tips = total + (total * (tips / 100))
print(f"Each person should pay: {round(bill_with_tips / persons, 2)}")