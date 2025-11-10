# ----------------------------------------
# Project: Marks Calculator
# Author: Lankesh Tayade
# Description: Calculates total, percentage, and pass/fail remarks
# ----------------------------------------

from functools import reduce

a = int(input("Enter your no. of subjects: "))
marks_list = []
out_off_marks = []

i = 1 
while i <= a:
    b = int(input(f"Enter subject {i} marks: "))
    marks_list.append(b)
    out_off_marks.append(100)
    i += 1

sum = lambda a,b:a+b

sum_list = reduce(sum, marks_list)
total_list = reduce(sum, out_off_marks)

percentage = (sum_list / total_list) * 100


for i in marks_list:
    if(i == 35):
        print("You Just Passed...Study More")
    elif (i < 35):
        print("You Failed in the Exam, Study Hard")

print(f"You Got {sum_list} marks out of {total_list} and my percentage is {percentage}%")





