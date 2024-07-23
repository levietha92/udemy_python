def my_function():
  result = 3*2
  return result

def my_function1():
  return 3*2
  

output = my_function()
print(output)

output1 = my_function1()
print(output1)

#Functions with outputs

def format_name(f_name, l_name):
  print(f_name.title())
  print(l_name.title())

print(format_name("hihi","gogo"))