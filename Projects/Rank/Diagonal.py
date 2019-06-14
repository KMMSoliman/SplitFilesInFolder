#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    while i < len(arr):
        sum1 = sum1 + arr[i][j]
        j = j + 1
        i = i + 1
    x = 0
    y = len(arr) - 1
    while x < len(arr):
        sum2 = sum2 + arr[x][y]
        y = y - 1
        x = x + 1

    totalSum = abs(sum1-sum2)
    return(totalSum)

arrTest = [[11,2,4],[4,5,6],[10,8,-12]]
#print(len(arrTest[0]))
#print(arrTest[0][0],arrTest[1][1],arrTest[2][2],arrTest[0][2],arrTest[1][1],arrTest[2][0])
result = diagonalDifference(arrTest)
print(result)
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
