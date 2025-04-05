from NameValidation import validation
from NameExecpt import InvalidNameError, ZerolenError,SpaceError
name  = input("ENTET YOUR NAME : ")
try :
 res = validation(name)
except InvalidNameError:
 print("INVALID NAME - PLEASE ENTER VALID NAME ")
except ZerolenError:
 print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
except SpaceError:
 print("DONT ENTER SPACE")
else:
 print(f"valid name is : {res}")
finally :
 print("I AM FROM FINNALY BLOCK ")