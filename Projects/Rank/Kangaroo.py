#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return("NO")

    #elif (x2 < x1 or v2 < v1)
    else:
        jump = 1
        x1End = x1
        x2End = x2
        while x1End <= 100000000 and x2End <= 100000000:

            if x1End == x2End and x1End < 100000000 and x2End < 100000000:
                return("YES")
                break
            else:
                x1End = x1End + v1
                x2End = x2End + v2
                if  x1End > 100000000 or x2End > 100000000 or jump < 200000:
                    return("NO")
                    break
                else:
                    jump += 1

"""
    else:
        print("NO")
112 9563 8625 244
"""
print(kangaroo(2081, 8403, 9107, 8400))
print(kangaroo(4523, 8092, 9419, 8076))
print(kangaroo(21, 6, 47, 3))
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
"""
