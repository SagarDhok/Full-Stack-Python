from AtmExcept import DepositeError, InsufficientFundError,WithdrawError
bal = 5000
def deposite():
     damt = int(input("ENTER HOW MUCH AMOUNT YOU WANT TO DEPOSITE : "))
     global bal
     if damt<=0:
          raise DepositeError
     else:
          bal = bal + damt
          print(f"YOUR ACCOUNT xxxx123 IS DEPOSITED WITH INR {damt}")
          print(f"NOW YOUR ACCOUNT xxxx123   BALANCE IS INR {bal}")

def withdraw():
     global bal
     wamt = int(input("ENTER HOW MUCH AMOUNT YOU WANT TO WITHDRAW :  "))
     if wamt<=0:
         raise WithdrawError

     elif wamt+500>bal:
          raise InsufficientFundError
     else:
           bal = bal - wamt
           print(f"YOUR ACCOUNT xxxx123 IS DEBITED WITH INR {wamt}")
           print(f"NOW YOUR ACCOUNT xxxx123   BALANCE IS INR {bal}")

def balenq():
 print(f" YOUR ACCOUNT xxxx123   BALANCE IS INR {bal}")