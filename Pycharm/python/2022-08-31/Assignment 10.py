import os
import shutil


def findcopy(extension, source, destination):
#    os.makedirs(destination)
    os.chdir(source)
    files = os.listdir()
    for i in range(len(files)):
        print(i, files[i])
        if extension in files[i]:
            print('found', extension, 'in', files[i])
            shutil.copy(files[i], destination)
    return None


findcopy('.docx', 'D:\Ajay\Education\iNeuron\FSDS\Assignments\Python Basics', 'd:/trial/new/python')
