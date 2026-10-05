# Worksheet 1.2: Task 1 Solution

import sys

grade = input("Please enter grade: ")

try:
    assert (int(grade) >= 0 and int(grade) <= 100)
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade)

if (grade < 40):
    print(f"{grade} is a Fail")
elif (grade < 70):
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")