#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesOffset = list()
    orangesOffset = list()
    nApp = 0
    nOra = 0
    for app in apples:
        applesOffset.append(app+a)

    for ora in oranges:
        orangesOffset.append(ora+b)

    for app in applesOffset:
        if app >= s and app <= t:
            nApp += 1

    for ora in orangesOffset:
        if ora >= s and ora <= t:
            nOra += 1

    print(nApp)
    print(nOra)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
