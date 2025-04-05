
#&  read()
#^----------------------------------------------------------------------------------------------
#! PROGRAM FOR READING THE DATA OF THE FILE 
# try:
#  with open("stud1.data","r") as fp:
#       filedata = fp.read()
#       print(type(filedata))        #<class 'str'>
#       print("Content of the file")
#       print(filedata)
# except FileNotFoundError:
#    print("File does not exits")

#! PROGRAM FOR READING THE DATA OF THE FILE 
#*DYNAMIC FILE NAME
# def displaydata():
#  try:
#   filname= input("ENTER FILE NAME : ")
#   with open(filname,"r") as fp:
#        filedata = fp.read()
#        print(type(filedata))        #<class 'str'>

#        print("Content of the file")
#        print(filedata)
#  except FileNotFoundError:
#     print("File does not exist")
# displaydata()
#^----------------------------------------------------------------------------------------------
#&  readlines()
# try:
#  with open("stud1.data","r") as fp:
#       filedata = fp.readlines() 
#       print(type(filedata))  # <class 'list'>
#       print("Content of the file")
#       print(filedata)
# except FileNotFoundError:
#    print("File does not exits")



#*DYNAMIC FILE NAME
# def displaydata():
#    try:
#     filname= input("ENTER FILE NAME : ")
#     with open(filname,"r") as fp:
#          filedata = fp.readlines()
#          print(type(filedata))        #<class 'lst'>
   
#          print("Content of the file")
#        #   print(filedata)   ['{33, 11, 44, 22}\n', '{33, 11, 44, 22}\n', '[1, 2, 3, 4]\n', '(100, 200, 300, 400)\n']
#          for val in filedata:
#             print(val,end="")
   
#    except FileNotFoundError:
#       print("File does not exist")
# displaydata()
#^----------------------------------------------------------------------------------------------
#! WPP WHICH WILL WRITE DATA CONTINUOSLY TO THE FILE DYNAMICALLY BY READING IT FROM THE KEYBOARD
# filname= input("Enter your filaname : ")
# print("Enter your filedata to write into file (Press @ to stop) :" )
# with open(filname, "a") as fp:
#     while True:
#         filedata = input()
#         if filedata != "@":
#           fp.write(filedata+"\n")

#         else:
#           print("Data is written to the file - verify ")
#           break
#^----------------------------------------------------------------------------------------------
#!PROGARM WHICH WILL READ NUMBER OF LINES ,WORDS,CHARS
# def readfile():
#  filename= input("Enter your file name : ")
#  with open(filename,"r") as fp:
#       filedata = fp.readlines()
#       print(filedata)
#       # print("Lines in file data = " ,len(filedata))
 
#       nl = 0
#       nw = 0
#       nc = 0
#       for line in filedata:
#           #   print(line)
#             nl = nl+1
#           #   print(line.split())
#             nw = nw + len(line.split())
#             nc = nc+len(line)    #includes all 
 
#            #FOR ONLY ALPHABETS
#            #  for char in line:
#            #      if char.isalpha():
#            #        nc = nc+1
 
 
#       print(f"Number of lines = {nl}")      
#       print(f"Number of words = {nw}")      
#       print(f"Number of words = {nc}")      
# readfile() 



#^----------------------------------------------------------------------------------------------
#!WRITE A PROGARM TO COPY THE CONTENT OF ONE FILE TO ANOTHER FILE 
# def copyfile():
#     try:
#       sf = input("Enter source file name : ")
#       with open(sf,"r") as rp:
#            filedata = rp.read()
#            df = input("Enter destination file name : ")
#            with open(df, "w") as fp:
#              fp.writelines(filedata)
#            print("File copied succesfully - verify ")
#     except FileNotFoundError:
#           print("Source file does not exist")

# copyfile()
#^----------------------------------------------------------------------------------------------