from Exception import InvalidNameError,ZeroLenghtError,SpaceError
from NameValidation import NameValidation
try:
 name = input("Enter Your Name : ")
 res = NameValidation(name)
 print(res)
 
except InvalidNameError:
     print("Please Enter Valid Name  ")
except ZeroLenghtError:
     print("Please Enter Name - Dont Leave Empty")
except SpaceError:
     print("Dont Enter SPaces ")