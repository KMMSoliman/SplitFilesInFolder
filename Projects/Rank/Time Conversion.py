#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    tempArr = []
    tempArr.append(s[0:2])
    tempArr.append(s[3:5])
    tempArr.append(s[6:8])
    tempArr.append(s[8:10])
    if tempArr[3] == "PM" and int(tempArr[0]) < 12:
        tempArr[0] = str(int(tempArr[0]) + 12)

    elif tempArr[3] == "AM" and tempArr[0] == "12":
        tempArr[0] = "00"

    elif tempArr[3] == "PM" and tempArr[0] == "12":
        tempArr[0] = "12"

    print(tempArr[0]+":"+tempArr[1]+":"+tempArr[2])
    #print(tempArr)
    """
    strArr = s.split(":")
    FinalTime = []
    tempArr = []
    i = 0
    while i < len(strArr):
        if i == 2:
            tempArr.append(strArr[i][0:2])
            tempArr.append(strArr[i][2:4])
            FinalTime.append(tempArr[0])

        else:
            FinalTime.append(strArr[i])
        i += 1

    if tempArr[1] == "PM":
        FinalTime[0] = int(FinalTime[0]) + 12

    print(str(FinalTime[0])+":"+FinalTime[1]+":"+FinalTime[2])
    """
st = "12:45:54PM"
#st = "12:40:22AM"
#st = "07:05:45PM"
timeConversion(st)
"""
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
"""
