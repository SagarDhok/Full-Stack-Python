#StudentAdd.py<---File Name and Module Name
import pickle
#development of exceptions
class InvalidNameError(Exception):pass
class ZeroLengthError(BaseException):pass
class SpaceNameError(Exception):pass
#Code for Validation of Name
def validation(name):
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
            words = name.split()  # words=["Guido","Van","Rossum"]
            res = True
            for word in words:
                if (not word.isalpha()):
                    res = False
                    break
            if (res):
               return name
            else:
               raise InvalidNameError
def savestuddata():
    with open("NIT.data","ab") as fp:
        try:
            #Read the student Data from KBD
            print("----------------------------------")
            sno=int(input("Enter Student Number:"))
            sname=validation(input("Enter Student Name:"))
            marks=float(input("Enter Student Marks:"))
            print("----------------------------------")
            #create an empty list for placing student vals
            lst=[]
            lst.append(sno)
            lst.append(sname)
            lst.append(marks)
            #Save lst data to student.pick file
            pickle.dump(lst,fp)
            print("Student Data Saved in a File Sucessfully")
            print("----------------------------------")
        except ValueError:
            print("Don't Enter Alnums, strs and symbols for Stno and Marks")
        except InvalidNameError:
            print("Invalid Name--Try Again")
        except ZeroLengthError:
            print("Try to enter Ur Name")
        except SpaceNameError:
            print("Don't enter Space for Ur Name--try again:")

