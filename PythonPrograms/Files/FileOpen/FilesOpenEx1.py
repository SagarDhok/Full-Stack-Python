
#! PROGRAM FOR OPENING FILE IN READ MODE -  open()  
# try:
#  fp = open("stud.data","r")
# except FileNotFoundError:
#  print("FILE DOES NOT EXIST")
# else:
#  print("TYPE OF POINTET = ",type(fp))
#  print("FILE OPENED IN READ MODE")

#^----------------------------------------------------------------------------------------
#!NameError
# try:
#  fp = open("C:\\Users\\sdhok\\!PACKAGES\\stud1.data","r")
# except FileNotFoundError:
#  print("FILE DOES NOT EXIST")
# else:
#  print("TYPE OF POINTET = ",type(fp))
#  print("FILE OPENED IN READ MODE")
#  print("IS FILE IS CLOSED = ",fp.closed)
# finally:
#  print("I AM FROM FINALLY BLOCK")
#  print("IS FILE IS CLOSED - FINALLY BLOCK =  ",fp.closed)
#  fp.close()
#  print("IS FILE IS CLOSED - FINALLY BLOCK AFTER close() FUNCTION =   ",fp.closed)
 
#^----------------------------------------------------------------------------------------
# try:
#  fp = open("stud4.data","r")
# except FileNotFoundError:
#  print("FILE DOES NOT EXIST")
# else:
#  print("TYPE OF POINTET = ",type(fp))
#  print("FILE OPENED IN READ MODE")
#  print("IS FILE IS CLOSED = ",fp.closed)  # ELSE BLOCK OP SATHI EXECUTE HOT ASTE
# finally:
#  print("I AM FROM FINALLY BLOCK")
# try:
#  print("IS FILE IS CLOSED - FINALLY BLOCK =  ",fp.closed)
#  fp.close()  #MANUAL CLOSING
#  print("IS FILE IS CLOSED - FINALLY BLOCK AFTER close() FUNCTION =   ",fp.closed)
# except NameError:
#  print("UNABLE TO OPEN - THERE IS NO NEED TO CLOSE")