# List comprehension

## Instead of this
numbers = [1,2,3]
new_list = []
for item in numbers:
    item +=1
    new_list.append(item)
print(new_list)

## We do this
better_new_list = [n+1 for n in numbers]
print(better_new_list)

## Also works with string (or any types of sequence)
name = "bewhahaa"
new_name = [letter for letter in name]
print(new_name)

calc = [n*2 for n in range(1,5)]
print(calc)

# Conditional list comprehension

## Syntax = [new_value for value in list if test]
names = ["Harry", "Hermione", "Ron", "Snape", "Dumblydore"]
names_length = [len(name) for name in names]
short_name = [name for name in names if len(name) < 5]
print(names_length)
print(short_name)