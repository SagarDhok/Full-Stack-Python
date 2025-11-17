
#^-------------------------------------------------------------------------------------------- 
#! 1  Program for creating a folder 
#*Mkdir("Single folder ")
# import os 
# try:
#  os.mkdir("Sa\n j - ")
#  print("Folder created successfully - verify ")
# except FileExistsError:
#  print("File already exist")
# except FileNotFoundError:
#  print("root File does not exist ")
# except OSError as e:
#  print(e)

# import os
# try:
#  os.mkdir("C:\\World\\India\\Akola")
#  print("Folder created successfully - verify ")
# except FileExistsError:
#  print("File already exist")
# except FileNotFoundError:
#  print("File does not exist ")
# except OSError as e:
#  print(e)



#^-------------------------------------------------------------------------------------------- 
#! 2  Program for creating hierarachy of folder  or directory
# * makedirs()
# import os
# try:
#  os.makedirs("Course\\Subjects\\Python")
#  print("File Hierarchy created successfully ")
# except FileExistsError :
#  print("File Already Exist ")
#  except OSError as e:
#  print(e)


# import os 
# try:
#  os.makedirs("C:\\Fruit\\Mangoes")
#  print("File Created Successfully ")
# except FileExistsError:
#  print("File Already exist ")
#  except OSError as e:
#  print(e)


#* Can create one folder also 
# import os
# os.makedirs("SGR")
# print("File Hierarchy created successfully ")
#  except OSError as e:
#  print(e)
#^-------------------------------------------------------------------------------------------- 
#! 3  Program for removing folder or directory
#* Folder must be empty
#* rmdir()

# import os 
# try:
#  os.rmdir("python.py")
#  print("Folder removed Successfully -  verify ")
# except FileNotFoundError:
#  print("FIle does not exist ")
# except OSError:
#     print("Ensore Ur Folder Must be Empty")

#^-------------------------------------------------------------------------------------------- 
#! 4  Program for removing folder or directory  hierarachy  
#* removedirs()
# import os 
# try:  
#  os.removedirs("Course\\Subjects")
#  print("File Hierararchy removed successfully - verify ")
# except FileNotFoundError:
#  print("File does not found ")
# except OSError:
#     print("Ensore Ur Folder Must be Empty")


#* can also remove one folder 
# import os 
# try:
#  os.removedirs("fajk")
#  print("Folder hierarchy removed Successfully ")
# except FileNotFoundError:
#  print("File Does not exist ")
# except OSError:
#     print("Ensore Ur Folder Must be Empty")
#^--------------------------------------------------------------------------------------------
#! 5 Renaming folder  - same funtion in file
#* rename()
# import os
# try:
#  os.rename("KVR","SGR") 
#  print("File renamed succesfully ")
# except FileNotFoundError:
#  print("FIle does not exist ")
# # except OSError as e :
# #  print(e)
# except FileExistsError:
#  print("FIle already exist ")

#^--------------------------------------------------------------------------------------------