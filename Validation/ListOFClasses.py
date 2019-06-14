# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:24:18 2019

@author: 09009
"""
import pandas as pd
#object1 = "car"
#######################################################
#Function to get classes from classes.txt file in array originalClasses
#and put it in dictionary called classesWithIndex
#and make capitalize first letter in each word from class name and remove space
#between words to make dynamic creation classes from them later
def readClassesFile (fileName):
    global originalClasses
    global modefiedClasses
    global classesWithIndex
    modefiedClasses = []
    classesWithIndex = {}
    text_file = open(fileName+".txt", "r")
    originalClasses = text_file.read().splitlines()
    for n in originalClasses:
        classesWithIndex.update({n:originalClasses.index(n)})
        title = n.title()
        modefied = title.replace(" ", "")
        modefiedClasses.append(modefied)
    return classesWithIndex
#End of readClassesFiles function
#######################################################

#######################################################
#Function to extract classes and attributes from annotation file.
annotationNameList = ["ClassID", "originX", "originY", "h", "w", "RotationAngle"]

def readAnnotatedFile (fileName):
    global annotationArray
    #global annotationDictionary
    #global annotationNameList
    #global annotationArrayTotalDict
    annotationArray = []

    #annotationDictionary = {}
    #annotationArrayTotalDict = []
    text_file = open(fileName+".txt", "r")
    for line in text_file:
        annotationArray = [[float(num) for num in line.split()] for line in text_file]
    """
    i = 0
    y = 0
    while i < len(annotationArray):
        while y < len(annotationArray[i]):

            annotationDictionary.update({annotationNameList[y]: annotationArray[i][y]})
            y = y + 1
        annotationArrayTotalDict.append(annotationDictionary)

        i = i + 1
    """

    """
    for x in annotationArray:
        for y in x:
            annotationDictionary.update({annotationNameList[x.index(y)]: y})
    """
    #annotationDictionary = dict(itertools.zip_longest(*[iter(annotationArray)] * 2, fillvalue=""))
    return (annotationArray)
#End of readAnnotatedFile function
#######################################################

#######################################################
#function to count classes in file
def countClasses(fileAnnotated):
    data = readAnnotatedFile(fileAnnotated)
    data = pd.DataFrame(data)
    data.columns = annotationNameList
    data.replace({"ClassID":classesWithIndex})
    classesSize = data.groupby('ClassID').size()
    #classesSize = pd.DataFrame(classesSize)
    #classesSize.columns = ['Count']
    return classesSize
#End of countClasses function
#######################################################

#######################################################
#function
def createDataFrameMainStructure(Path, classesFile, fileAnnotated):
    classesDict = readClassesFile (Path+classesFile)
    df = pd.DataFrame(columns = classesDict)
    df['fileName'] = ""
    df['Path'] = ""
    #df['Index'] = ""
    countedClasses = countClasses(Path+fileAnnotated)
    df.loc[-1]=countedClasses
    #df.index += 1
    #df = df.sort_index()
    return df


#End of ----------- function
#######################################################

Path = "Test/"
FileName = "869510024184382_30028124_31227039_20170105081012_0_M_6face3db-ad79-423e-8cc6-180057c67b06"
FileNameValidation = "869510024184382_30028124_31227039_20170105081012_0_M_6face3db-ad79-423e-8cc6-180057c67b06 - Copy"
fileType = ".txt"
#ColumnData = createDataFrameMainStructure(Path, 'classes', FileName)
print (ColumnData)
#classFileNames = readClassesFile (Path + "/classes")
#annotatedFileData = readAnnotatedFile(Path+FileName)
#annotatedFileDataValidate = readAnnotatedFile(Path+FileNameValidation)

annotatedFileData = countClasses(Path+FileName)
#annotatedFileDataValidate = countClasses(Path+FileNameValidation)

#data = pd.DataFrame(annotatedFileData)
#dataVlaidation = pd.DataFrame(annotatedFileDataValidate)
#validation = {annotatedFileData: data, annotatedFileDataValidate: data}
#print  (pd.concat(validation))
#data = data.transpose()
#data.columns = annotationNameList
#dataVlaidation.columns = annotationNameList
#data = pd.DataFrame(annotatedFileData)
#df = data.groupby('ClassName').size()
#print(annotatedFileData)
#print(annotatedFileDataValidate)
#print(len(annotationArray[1]))
#print(annotationArrayTotalDict)
print(annotatedFileData)
#print(classFileNames)

class object:
    def __init__(self, name, classID):
        self.name = name
        self.classID = classID
        #print(name)


#objects = object(originalClasses, 0)
#print(objects.name)

"""
for x in modefiedClasses:
    x = object(originalClasses[x], originalClasses[x].index())
    print(x.name)
"""

TrafficSign = object("traffic sign", 0)
Marking     = object("marking", 1)
RightBarriers = object("right barriers", 2)
LeftBarriers = object("left barriers", 3)
LightPole = object("light pole", 4)
RightCurb = object("right curb", 5)
LeftCurb = object("left curb", 6)
Fence = object("fence", 7)
Building = object("building", 8)
Billboard = object("billboard", 9)
Pedestrian = object("pedestrian", 10)
Car = object("car", 11)
Bus = object("bus", 12)
Motorcycle = object("motorcycle", 13)
TukTuk = object("tuk tuk", 14)
HeavyVehicle = object("heavy vehicle", 15)
Tricycle = object("tricycle", 16)
PublicTransportation = object("public transportation", 17)
Adv = object("ADV", 18)
Tree = object("tree", 19)


#car = object(object1)

#print (Car.name)
#print (Car.classID)
