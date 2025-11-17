from PrimeExcept import NonPrimeError
def prime(n):
          if n<=1 :
           raise NonPrimeError
          else:
           res = True
           for i in range(2,n):
                if n%i==0:
                     res = False
                     break
           if res :
            print(f"{n} is a Prime Number ")
           else:
            print(f"{n} is Not a Prime Number")

