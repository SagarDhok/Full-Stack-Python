from MultiplicationExcept import ZeroError, NegNumberError
from MultiplicationTable import table
try:
 n = int(input("ENTER A NUMBER  : "))
 table(n)
except (ZeroError,NegNumberError,ValueError):
 print("DONT ENTER ZERO")
 print("DONT ENTER NEGATIVE NUMBER ")
 print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
except:
 print("SOMETHING WENT WRONG ")
finally:
 print("I AM FINALY BLOCK ")