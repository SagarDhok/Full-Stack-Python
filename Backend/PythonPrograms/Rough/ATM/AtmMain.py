from AtmException import WithdrawError ,DepositeError,InsuffcientBalenceError
from AtmOperation import Withdraw ,Deposite,Balq
from AtmMenu import Menu

Menu()
while True:
 try:
   ch = int(input("Enter Your Choice : "))
   match(ch):
        case 1 : 
             try:
              Deposite()
             except DepositeError:
                 print("Please Enter Valid Amount")
             except ValueError:
                 print("Dont Enter Alnums , ALphabets , Symbols")
        case 2 :
             try:
                 Withdraw()
             except WithdrawError:
                 print("Please Enter Valid Amount")
             except InsuffcientBalenceError:
                 print("Insufficient Balence In Your Account ")
             except ValueError:
                 print("Dont Enter Alnums , ALphabets , Symbols")
        case 3:
             Balq()
        
        case 4 :
               print("Thanks For Using This Program ")
               break
        case _ :
           print("Invalid Operation Please Choose Valid Operation")
 except ValueError:
   print("Dont Enter Alnums , ALphabets , Symbols")
              
              
      