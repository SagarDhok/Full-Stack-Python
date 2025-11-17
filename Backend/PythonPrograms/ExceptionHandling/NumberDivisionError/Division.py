from NumberDivisionError import NumberDivisionError

def divop(a,b):
      if b == 0:
            raise NumberDivisionError
      else: 
           return a/b