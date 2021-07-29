import os
import shutil
srcPath = "EX_01\\MNIST_persian"
targetPath = "EX_01\\Organaized"
allFolders = os.listdir(srcPath)

for folder in allFolders:
    newFolderPath = srcPath + "\\" + folder
    allFiles = os.listdir(newFolderPath)
    for file in allFiles:
        srcFile = newFolderPath + "\\" + file
        nameParts = file.split(".")
        saveFolder = targetPath + "\\" + nameParts[0]
        saveFile = saveFolder + "\\" + nameParts[0] + "-" + folder + ".jpg"
        if os.path.isdir(saveFolder) == False:
            os.mkdir(saveFolder)
        shutil.copy2(srcFile, saveFile)