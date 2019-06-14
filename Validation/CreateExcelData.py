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
Path = "C:/Users/09009/Desktop/Validation/meta_before/"
for file in files:
    print(file)
