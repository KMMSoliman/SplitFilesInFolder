# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:28:50 2019

@author: 09009
"""

dict = [[0,0,0,0],[1,1,1,1],[2,2,2,2]]
annotationNameList = ["k","l","m","n"]
annotationDictionary = {}
annotationArrayTotalDict = []
i = 0
y = 0
while i < len(dict):
    while y < len(dict[i]):
        
        annotationDictionary.update({annotationNameList[y]: dict[i][y]})
        y += 1
    annotationArrayTotalDict.append(annotationDictionary)
    
    i += 1

print(annotationArrayTotalDict)