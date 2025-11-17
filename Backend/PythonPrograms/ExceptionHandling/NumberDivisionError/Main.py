# from Division import divop
# from NumberDivisionError import NumberDivisionError
# try:

#  a = int(input("ENTER FIRST VALUE : "))
#  b = int(input("ENTER SECOND VALUE : "))
#  res = divop(a,b)
# except NumberDivisionError:
#    print("DONT ENTER ZEROS FOR DENOMINATOR")
# except ValueError:
#    print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
# else:
#    print(f"DIVISION = {res}")
# finally:
#    print("I AM FROM FINALLY BLOCK  ")
   
from Division import divop
from NumberDivisionError import NumberDivisionError
try:
 a = int(input("ENTER FIRST VALUE : "))
 b = int(input("ENTER SECOND VALUE : "))
 try:
  res = divop(a,b)
 except NumberDivisionError:
    print("DONT ENTER ZEROS FOR DENOMINATOR")
 
 else:
    print(f"DIVISION = {res}")
except ValueError:
    print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
finally:
    print("I AM FROM FINALLY BLOCK  ")