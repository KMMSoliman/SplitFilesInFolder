import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    Maxsum = 0
    Minsum = 0
    i = 1
    j = len(arr) - 2
    while i < len(arr):
        Maxsum = Maxsum + arr[i]
        Minsum = Minsum + arr[j]
        j -= 1
        i += 1

    print(Minsum,Maxsum)

arrTest = [1,2,3,4,5]
#arrTest.sort()
#print(arrTest)
miniMaxSum(arrTest)
"""
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
"""
