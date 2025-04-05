from AtmException import WithdrawError ,DepositeError,InsuffcientBalenceError


bal = 5000

def Deposite():
  global bal
  damt = int(input("Enter How Much Amount Do you Want to Withdraw : "))
  if damt<0:
    raise DepositeError
  else:
    bal = bal+damt
    print(f"{damt} Is Deposited In Your Account XXXX1234 ")
    print(f"Now Your Account Balence is : {bal}")


def Withdraw():
  global bal
  wamt = int(input("Enter How Much Amount Do You Want To Withdraw : "))
  if wamt+500>bal:
    raise InsuffcientBalenceError
  elif wamt<0:
    raise WithdrawError
  else:
    print(f"{wamt} Amount Is Withdraw From Your Account XXXX1234 ")
    bal = bal-wamt
    print(f"Now Your Balence is : {bal} ")


  
def Balq():
  global bal
  print(f"Your Balence is : {bal}")