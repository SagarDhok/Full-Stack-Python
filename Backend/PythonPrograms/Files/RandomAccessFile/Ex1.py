with open("Ex1.data","r") as fp:
 print("Initial position pointed by pointer = ",fp.tell()) #0
 filedata= fp.read(2)
 print(filedata)
 print("Now position pointed by pointer = ",fp.tell()) #2
 filedata= fp.read(8)               #letter kiti read karayche tell chya index pasun
 print(filedata)
 print("Now position pointed by pointer = ",fp.tell()) #10
 filedata= fp.read(9)
 print(filedata)
  
 filedata= fp.read()
 print(filedata)
 print("Now position pointed by pointer = ",fp.tell()) 

#  print("----------------------------")
#  filedata= fp.read()
#  print(filedata)

#Reset the file pointer 
 print("-------------")
 fp.seek(10)
 filedata = fp.read(9)
 print(filedata)
 print("-------------")
 fp.seek(0)
 filedata = fp.read(35)
 print(filedata)


