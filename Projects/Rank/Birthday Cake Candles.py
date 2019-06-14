#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort()
    maxN = max(ar)
    i = 0
    for j in ar:
        if j == maxN:
            i += 1

    return(i)

arrTest = [3,2,1,3]

print(birthdayCakeCandles(arrTest))
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
