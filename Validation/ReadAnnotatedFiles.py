# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:48:57 2019

@author: 09009
"""

path = "Test/"
FileName = "869510024184382_30024832_31230563_20170105080720_0_M_6face3db-ad79-423e-8cc6-180057c67b06"
fileType = ".txt"

file = open(path+FileName+fileType, 'r')
print(file.readlines())
print(file.read())
file.close()
