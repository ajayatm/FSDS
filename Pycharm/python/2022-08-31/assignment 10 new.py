import os
import shutil


def findcopy(extension, source, destination):
    os.makedirs(destination)
    for folderName, subfolders, filenames in os.walk(source):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
            if extension in filename:
                src_file = folderName + '\\' + filename
                dst_file = destination + '\\' + filename
                print('found', extension, 'in', filename)
                shutil.copyfile(src_file, dst_file)
    return None


findcopy('.pdf', 'D:\\Ajay\\Health', 'd:\\trial\\new\\python')
