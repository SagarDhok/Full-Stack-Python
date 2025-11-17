from PrimeExcept import NonPrimeError
from PrimeValidation import prime
try:
 n = int(input("ENTER A NUMBER "))
 prime(n)
except NonPrimeError :
  print("DONT ENTER 1 AND NEGATIVE NUMBRES")
except ValueError:
 print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
finally:
 print("I AM FROM FINALLY BLOCK ")

