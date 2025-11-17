
#! PROGRAM FOR WRITING DATA TO THE FILE
#* WRITELINES()

x = (1000,"SD",5000)   #ITERABLE OBJ
with open("stud2.data","a") as fp:
    fp.writelines(str(x)+"\n")
print("DATA WRITTEN TO THE FILE - VERIFY")