from AtmMenu import menu
from AtmOperation import deposite,withdraw,balenq
from AtmExcept import DepositeError, InsufficientFundError,WithdrawError

while(True):
 menu()              # only showing menu 
 try:
   ch= int(input("ENTER YOUR CHOICE : "))
   match(ch):
    case 1 :
     try:
      deposite()
     except DepositeError:
      print("PLEASE ENTER VALID AMOUNT ")
     except ValueError:
      print("DONT ENTER ALPHABETS ,ALNUMS, SYMBOLS ")
      
    case 2 :
     try:
      withdraw()
     except WithdrawError:
      print("PLEASE ENTER VALID AMOUNT ")
     except ValueError:
      print("DONT ENTER ALPHABETS ,ALNUMS, SYMBOLS ")
     except InsufficientFundError:
      print("YOUR ACCOUNT HAS INSUFICIENT BALENCE ")
     
    case 3 :
     balenq()
    case 4 : 
     print("THANKS FOR USING THIS PROGRAM")
     break
    case _ :
     print("YOUR SELECTION OF OPERATION IS WRONG PLEASE - TRY AGAIN")
 except ValueError:
   print("DONT ENTER ALNUMS , ALPHABETS , SYMBOLS CHOICE - PLEASE TRY AGAIN")