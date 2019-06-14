#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def roundFun (n, base = 5):
    return (base * round(n/base))

def gradingStudents(grades):
    #
    # Write your code here.
    #
    FinalGrades = []
    for grade in grades:
        newGrade = roundFun (grade)
        if newGrade - grade < 3 and newGrade - grade > 0 and grade > 35:
            FinalGrades.append(newGrade)
        else:
            FinalGrades.append(grade)

    return(FinalGrades)
gradesArr = [73, 67, 38, 33]
print(gradingStudents(gradesArr))
"""
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
"""
