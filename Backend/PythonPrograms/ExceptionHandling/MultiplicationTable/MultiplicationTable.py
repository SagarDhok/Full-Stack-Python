from MultiplicationExcept import ZeroError, NegNumberError

def table(n):
     if n == 0:
          raise ZeroError
     elif n<0 :
          raise NegNumberError
     else:
          for i in range(1,11):
               print(f"{n} X {i} = {n*i}")