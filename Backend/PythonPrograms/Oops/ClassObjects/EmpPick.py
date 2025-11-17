import pickle
from Employee import Employee

class EmpPick:
     def savedata(self):
      with open("Empdata.Pick","ab") as fp:
        
       while True:
          try:
            eno = int(input("Enter Employee Number : "))
            name = input("Enter Employee Name : ")
            sal = float(input("Enter Employee Salary : "))
            
            eo = Employee()
            eo.readvalues(eno,name,sal)
 
            pickle.dump(eo,fp)
            print("Employee Record Saved Successfully - Verify")
            ch = input("Enter Do you want to Insert Another Record - (yes/no) : ").lower()
            if ch == "no":
               print("Thanks For Using This Program")
               break
            
          except ValueError:
                     print("\tDon't Enter alnums,strs and symbols for eno and sal-try again")

emo = EmpPick()
emo.savedata()
 