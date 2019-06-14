import os
import shutil

Path = "J:/Cairo-Alex Disert Road - devide/"
FileType = ".jpg"
"""
os.rename(source, destin)
os.makedirs(newpath)
shutil.move(source, destin)
"""
def CopyFileTOFolder(Path):
    #files = os.listdir(Path)
    i = 1
    #FolderName = str(i)

    """
    os.makedirs(Path+FolderName)
    for file in files[FirstI: SecondI]:
        shutil.copy2(Path+file, Path+FolderName)
    """

    while i < 173:
        shutil.copy2(Path+"classes.txt", Path+str(i))
        i = i + 1
    print("Finished")
    #files = os.walk(Path).next()
    #print(files[FirstI: SecondI])





def SelectTheFirstNItems(Path, N):
    files = os.listdir(Path)
    i = 1
    FolderName = str(i)
    FirstI = 0
    SecondI = 10
    """
    os.makedirs(Path+FolderName)
    for file in files[FirstI: SecondI]:
        shutil.copy2(Path+file, Path+FolderName)
    """

    while FirstI < len(files):
        os.makedirs(Path+str(i))
        for file in files[FirstI: SecondI]:
            shutil.move(Path+file, Path+str(i))
        i = i + 1
        SecondI = SecondI + 10
        FirstI = FirstI + 10
    print("Finished")
    #files = os.walk(Path).next()
    #print(files[FirstI: SecondI])

#SelectTheFirstNItems(Path, 10)
CopyFileTOFolder(Path)
