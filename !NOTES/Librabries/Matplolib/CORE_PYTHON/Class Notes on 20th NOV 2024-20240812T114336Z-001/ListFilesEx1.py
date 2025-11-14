#Program Listing the Files in Folder
#ListFilesEx1.py
import os
# <class 'list'>
FilesList=os.listdir("C:\\Users\\KVR\\PycharmProjects\\9AMFilesExamples")
# print(FilesList,type(FilesList)) =  #it gives files list in list <class 'list'>
print("-----------------------------------")
for filename in FilesList:
    print("\t{}".format(filename))
print("-----------------------------------")
