
#^-------------------------------------------------------------------------------------------
#! #Program Listing the Files in Folder
#*listdir()
# import os
# FilesList = os.listdir("E:\FULL STACK PYTHON\!NOTES\CORE_PYTHON\Class Notes on 20th NOV 2024-20240812T114336Z-001")
# # print(FilesList,type(FilesList)) =  #it gives files list in list <class 'list'>
# for list in FilesList:
#      print(list)
#^-------------------------------------------------------------------------------------------
#* . current working folder 
# import os
# FilesList  = os.listdir(".")
# print(FilesList)

#* .. parent folder 
# import os
# FilesList  = os.listdir("..")
# print(FilesList)
#^-------------------------------------------------------------------------------------------
# * printing only python file 
# import os
# filelst = os.listdir("E:\FULL STACK PYTHON\PythonPrograms\Files\OsModule")
# nopf = 0
# for list in filelst:
#     if list.endswith(".py"):
#         print(list)
#         nopf+= 1
# print(f"Number of data Files :  {nopf}")


# import os
# filelst = os.listdir("E:\FULL STACK PYTHON\PythonPrograms\Files\OsModule")
# nodf = 0
# for list in filelst:
#     if list.startswith("F"):
#         print(list)
#         nodf+= 1
# print(f"Number of data Files :  {nodf}")

#^-------------------------------------------------------------------------------------------
# * printing only data file
# import os
# filelst = os.listdir(".")
# df = list(filter(lambda filename : filename.endswith(".data"),filelst))
# # print(df)
# for files in df:
#      print(files)
# print(f"Number of data files : {len(df)}")