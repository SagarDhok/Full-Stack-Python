
#*SYNTAX - 1: 
# class NumberDivisionError(BaseException):pass

# def divop():
#      try:
#       a = int(input("ENTER FIRST VALUE : "))
#       b = int(input("ENTER FIRST VALUE : "))
#       if b == 0:
#             raise NumberDivisionError
            
#      except NumberDivisionError:
#                 print("DONT ENTER ZEROS AS DENOMINATOR ")
#      except ValueError:
#                 print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
#      else:
#              print(f"DIVISION = {a/b}")
#      finally:
#                 print("I AM FROM FINALLY BLOCK ")
            
    
# divop()

#^---------------------------------------------------------------------------------------------
#*SYNTAX - 1: 
#*LOGIC - 1: 

# class NumberDivError(Exception):pass
# def divop(a,b):
#  if b == 0:
#   raise NumberDivError
#  else:
#   return a/b

# try:
#  a = int(input("ENTER FIRST VALUE : "))
#  b = int(input("ENTER SECOND VALUE :  "))
#  res = divop(a,b)
# except NumberDivError:
#        print("DONT ENTER ZEROS AS DENOMINATOR ")
# except ValueError:
#            print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
# else:
#            print(f"DIVISION = {res}")
# finally:
#            print("I AM FROM FINALLY BLOCK ")



#*LOGIC - 2: 
# class NumberDivError(Exception):pass
# def divop(a,b):
#  if b == 0:
#   raise NumberDivError
#  else:
#   return a/b

# try:
#  a = int(input("ENTER FIRST VALUE : "))
#  b = int(input("ENTER SECOND VALUE :  "))
#  try:
#   res = divop(a,b)
#  except NumberDivError:
#         print("DONT ENTER ZEROS AS DENOMINATOR ")

#  else:
#             print(f"DIVISION = {res}")

# except ValueError:
#             print("DONT ENTER ALPHABETS , ALNUMS , SYMBOLS ")
# finally:
#             print("I AM FROM FINALLY BLOCK ")
#^---------------------------------------------------------------------------------------------