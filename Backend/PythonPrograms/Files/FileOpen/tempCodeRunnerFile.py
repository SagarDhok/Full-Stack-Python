try:
 fp = open("stud.data","r")
except FileNotFoundError:
 print("FILE DOES NOT EXIST")
else:
 print("TYPE OF POINTET = ",type(fp))
 print("FILE OPENED IN READ MODE")