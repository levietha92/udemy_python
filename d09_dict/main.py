programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving
print(programming_dictionary["Bug"])
# print(programming_dictionary[Bug]) #wrong data type
# print(programming_dictionary["doesn't exist"]) #doesn't exist

#Adding new items to dict
programming_dictionary["Loop"] = "blabla"
print(programming_dictionary)

#Creating empty dict
dict = {}

#Edit item in dict
programming_dictionary["Bug"] = "hihi"
print(programming_dictionary)

#Loop through dict:
for key in programming_dictionary: #only use key here
  print(key)
  print(programming_dictionary[key])



