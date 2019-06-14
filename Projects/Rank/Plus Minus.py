#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = []
    negative = []
    zerros = []
    for i in arr:
        if i == 0 :
            zerros.append(i)
        elif i > 0 :
            positive.append(i)
        else:
            negative.append(i)
        i = i + 1
    posi = len(positive)/len(arr)
    nega = len(negative)/len(arr)
    zer = len(zerros)/len(arr)

    print('%.6f' % posi)
    print('%.6f' % nega)
    print('%.6f' % zer)

arrTest= [-4, 3, -9, 0, 4, 1]
plusMinus(arrTest)
"""
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
"""
