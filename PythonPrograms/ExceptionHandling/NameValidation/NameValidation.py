from NameExecpt import InvalidNameError,ZerolenError, SpaceError
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
           
 
 