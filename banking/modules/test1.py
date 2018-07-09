#!/usr/bin/env python
record = int(input("Enter the student record need to add :"))

stud_data={}

for i in range(0,record):
    Name = input("Enter the student name :").split()
    Age = input("Enter the {} age :".format(Name))
    Grade = input("Enter the {} grade :".format(Name)).split()
    Nam_key =  Name[0]
    Age_value = Age[0]
    Grade_value = Grade[0]
    stud_data[Nam_key] = {Age_value,Grade_value}

print(stud_data)
