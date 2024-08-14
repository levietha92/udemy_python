# My way: this change the order of appearance and failed the test
with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

listall = [int(str_item) for str_item in list1 + list2]
listall.sort()


overlap = [listall[index] for index in range(0, len(listall)) if listall[index] == listall[index - 1]]
# print(overlap)

result = [overlap[index] for index in range(0, len(overlap)) if overlap[index] != overlap[index - 1]]
print(result)


# Second try
with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]
print(list1)
print(list2)

result = [int(num) for num in list1 if num in list2]

print(result)