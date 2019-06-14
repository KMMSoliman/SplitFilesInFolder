import os
import pandas as pd
#import csv
file = "C:/Users/09009/Desktop/Interview/housing.csv"
firstColumn = "State"
secondCoumn = "Ratio"
#First Task: Combine 2 Columns in 1
HousingData = pd.read_csv(file)
HousingData(10)
#text_file = open(file, "r")
#print (text_file)
"""
def combineTwoCol (file, firstColumn, secondCoumn):
    f1 = pd.read_csv(file, usecols=[colnames])

    reader = csv.reader(f)
    for row in reader:
        print (row)
"""


#combineTwoCol (file, firstColumn, secondCoumn)
