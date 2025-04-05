import pickle
def getallrecords():
 try:
  with open("Nit.data", "rb") as fp:
       print("\tStudent Details")
       while True:
        try:
         filedata = pickle.load(fp)
         for record in filedata:
            print(f"\t{record}",end="\t")
         print()
        except EOFError:
           break
 except FileNotFoundError:
   print("File Does not exist ")

def getrecord():
 try:
  with open("Nit.data", "rb") as fp:
       records = []
       while True:
        try:
         filedata = pickle.load(fp)
         records.append(filedata)
        except EOFError:
           break
       try:
        sno = int(input("Enter student Number : "))
        res= False
        for val in records:
          if sno == val[0]:
            res = True
            break
        if res:
         print(f"Student name = {val[0]}")
         print(f"Student name = {val[1]}")
         print(f"Student name = {val[2]}")
        else:
          print("Student record does not exits")
       except ValueError:
         print("Dont Enter Alphabets , Alnums, Sumbols")
 except FileNotFoundError:
   print("File Does not exist ") 