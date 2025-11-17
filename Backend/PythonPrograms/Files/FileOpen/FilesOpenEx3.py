
#! PROGRAM FOR OPENING FILE IN READ MODE - with open() as 
try:
 with open("stud.data","r") as fp:
      print("INSIDE IN BLOCK OF INDENTATION with open()")
      print("FILE IS OPNED IN READ MODE SUCCESFULLY")
      print("FILE IS CLOSED = ",fp.closed) # attribute
      print("FILE NAME = ",fp.name)  # attribute
      print("FILE OPENING MODE = ",fp.mode)  # attribute
      print("CAN WE READ THE DATA FROM FILE= ",fp.readable())  # function
      print("CAN WE WRITE THE DATA TO THE FILE= ",fp.writable())  # function

 print("--------------------------------------------------------------")
 print("OUT OF BLOCK OF INDETAION OF with open()")
 print("FILE IS CLOSED = ",fp.closed)   # attribute
except FileNotFoundError:
   print("FILE DOES NOT EXIST") 


#^----------------------------------------------------------------------------------------

with open("stud2.data","w+") as fp:
      print("INSIDE IN BLOCK OF INDENTATION with open()")
      print("FILE IS OPNED IN READ MODE SUCCESFULLY")
      print("FILE IS CLOSED = ",fp.closed) # attribute
      print("FILE NAME = ",fp.name)  # attribute
      print("FILE OPENING MODE = ",fp.mode)  # attribute
      print("CAN WE READ THE DATA FROM FILE= ",fp.readable())  # function
      print("CAN WE WRITE THE DATA TO THE FILE= ",fp.writable())  # function

# print("--------------------------------------------------------------")
# print("OUT OF BLOCK OF INDETAION OF with open()")
# print("FILE IS CLOSED = ",fp.closed)   # attribute
