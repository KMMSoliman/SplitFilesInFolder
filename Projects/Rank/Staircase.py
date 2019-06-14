#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.

def staircase(n):
    #printer = ""
    #stai = ""
    i = 1
    j = n-1
    while i <= n:
        printer = ""
        stai = ""
        printer += ' ' * j
        stai += '#' * i
        print(printer+stai)
        j -= 1
        i += 1

    #printer += ' ' * n
    #print(printer+'x')


if __name__ == '__main__':
    n = int(input())

    staircase(n)
    input()
