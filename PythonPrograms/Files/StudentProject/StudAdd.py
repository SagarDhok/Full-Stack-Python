import pickle 
class InvalidNameError(Exception):pass
class  ZerolenError(Exception):pass
class  SpaceError(Exception):pass

def validation(name:str):
 if len(name)==0:
     raise ZerolenError
 elif name.isspace():
     raise SpaceError
 else:
  words =  name.split()
  res= True
  for word in words:  #["my","name","is"]
       if not word.isalpha():
        res = False
        break
  if res:
       return name
  else:
          raise InvalidNameError
           
 

def StudAdd():
 with open("Nit.data","ab") as fp:
  try:
   sno = int(input("Enter Student Number : "))
   sname = validation(input("Enter Student Name : "))
   Smarks = int(input("Enter Student Marks : "))
 
   lst = []
   lst.append(sno)
   lst.append(sname)
   lst.append(Smarks)
   pickle.dump(lst,fp)
   print("Student Data Added in file successfully ")
  except ValueError:
   print("Dont Enter Alphabests,Alnums, Symbols...")
  except InvalidNameError:
   print("Invalid name please enter valid name  ")
  except ZerolenError:
   print("Please Enter Something")
  except SpaceError :
   print("Dont Enter Spaces ")
