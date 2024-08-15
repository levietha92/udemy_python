# new_dict = {new_key:new_value for item in list | if test}
# new_dict = {new_key:new_value for (key,value) in dict.items() | if test}
import random


students = ["HP", "Hermione","Ron"]
scores = [10,20,30]

way1 = dict(zip(students, scores))
way2 = {student:score for (student,score) in zip(students, scores)}

print(way1)
print(way2)

# generating hocus pocus scores because you are Snape on a Friday
way3 = {student:random.randint(0,100) for student in students}
print(way3)

# who passed?
passed = {student:score for student,score in way3.items() if score >= 50}
print(passed)

########## How to iterate over pd df
import pandas as pd

student_dict = {
    "student":["arry", "hermione","ron"],
    "score":[10,20,30]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

## Usually with a dict, what we do is for loop like so:
## The result of Key = column name, Value = list of records in each "column"
for key,value in student_dict.items():
    print(key)
    print(value)

## If we apply same method on dataframe:
for key,value in student_df.items():
    print(key) #gives similar result i.e column name
    print(value) #gives the series instead, with index attached and dtype

## Better way to do this in pandas on df 
for index,row in student_df.iterrows():
    print(index)
    print(row) #--> give result by row/record, instead of column-based
    print(row.student) #--> give result by column