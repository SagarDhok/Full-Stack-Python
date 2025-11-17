# ^---------------------------------------------------------------------------------------------------
#! Create a program that checks for negative numbers in subtraction:
# * Write a Python program that performs subtraction between two numbers. If the second number is larger than the first, raise a custom exception called NegativeResultError.

# class NegativeResultError(Exception):
#     pass
# def Subop():
#     try:
#         a = int(input("Enter First Number : "))
#         b = int(input("Enter Second Number : "))

#         if b > a:
#             raise NegativeResultError
#         else:
#             print(f"Substracition : {a-b}")
#     except NegativeResultError:
#         print("Second Value is Greater than first - So Result is Negative")
#     except ValueError:
#         print("Dont Enter Alnums,Alphabets , Symbols ")
# Subop()

# ^---------------------------------------------------------------------------------------------------
#!Handle invalid inputs for multiplication:
# *Create a program that takes two inputs for multiplication. If either input is not a number, raise a ValueError and handle it by displaying an appropriate message.

# class InvalidValueError(BaseException):pass
# def Mulop():
#    try :
#      a = input("Enter First Value : ")
#      b= input("Enter Second Value : ")

#      if not a.isdigit() or not b.isdigit():
#         raise InvalidValueError
#      else:
#       a = int(a)
#       b = int(b)
#      print(f"Multiplication : ({a},{b}) = {a*b} ")

#    except InvalidValueError:
#       print("Dont Enter Alnums,Alphabets , Symbols")
# Mulop()
# ^---------------------------------------------------------------------------------------------------
#!Division with multiple custom errors:
# * Write a program that performs division and raises:
# * ZeroNumError if the divisor is zero.
# * NegativeNumberError if either of the numbers is negative.

# class ZeroNumError (Exception):pass
# class  NegativeNumberError (BaseException):pass
# def divop():
#    try :
#      a = int(input("Enter First Value : "))
#      b= int(cinput("Enter Second Value : "))

#      if b==0:
#        raise ZeroNumError
#      elif a<0 or b<0:
#        raise NegativeNumberError

#    except ZeroNumError:
#           print("Dont Enter Zero as Denominator ")
#    except NegativeNumberError:
#       print("Dont Enter Negative Number ")
#    except ValueError:
#         print("Dont Enter Alnums,Alphabets , Symbols ")


# divop()
# ^---------------------------------------------------------------------------------------------------
#! Square root calculation with custom exceptions:
# * Create a program that calculates the square root of a number. Raise a NegativeNumberError if the user inputs a negative number

# class NegativeNumberError(BaseException):
#     pass
# def sqrt():
#     try:
#         a = int(input("Enter First Value : "))

#         if a < 0:
#             raise NegativeNumberError
#         else:
#             print(f"Square root : {a}={a**0}")

#     except NegativeNumberError:
#         print("Dont Enter Negative Number ")
#     except ValueError:
#         print("Dont Enter Alnums,Alphabets , Symbols ")
# sqrt()
# ^---------------------------------------------------------------------------------------------------
#! Custom exceptions for age validation:
# * Write a program to validate user age input:
# * If the input is not a number, raise a ValueError.
# * If the age is below 18, raise an UnderageError.
# * If the age is above 100, raise an OverageError.

# class UnderageError(Exception):pass
# class OverageError(Exception):pass
# try:
#  age = int(input("Enter Age : "))
#  if age<18:
#       raise UnderageError
#  elif age>100:
#       raise OverageError
#  else:
#       print(f"{age} is Valid ")
# except UnderageError:
#      print("age is Below 18")
# except OverageError:
#      print("Age is More than 100")
# except ValueError:
#      print("Dont Enter Alnumls,ALphabets , Symbols ")
# ^---------------------------------------------------------------------------------------------------
#! Custom exception for division using floating-point numbers:
# * Write a program that only allows division with integer numbers. If the user inputs a floating-point number, raise a FloatNumError and handle it appropriately.


# class FloatingPointError(BaseException):
#     pass


# try:
#     a = input("Enter A Number :")
#     b = input("Enter Second Number : ")

#     if "." in a or "." in b:
#         raise FloatingPointError
#     else:
#         a = int(a)
#         b = int(b)
#         c = a / b
#         print(f"Division : {c}")
# except FloatingPointError:
#     print("Dont Enter Float Values (Enter Only Integer Values )")
# except ValueError:
#     print("Please Enter Valid Input (No letters, alnums, symbols)")
# except ZeroDivisionError:
#     print("Dont Enter Zero as Denominator ")

#^--------------------------------------------------------------------------------------------------
#! ATM withdrawal system:
#* Create a program where the user enters an account balance and withdrawal amount. Raise a InsufficientFundsError if the withdrawal amount exceeds the account balance.

# class InsufficientFundsError(Exception):pass

# try:
#  bal = float(input("Enter Your Balance :  "))
#  wamt = float(input("Enter Your Withdrawl amount :"))
 
#  if wamt>bal:
#       raise InsufficientFundsError
#  else:
#       print(f"{wamt} Amount Withdraw successfully from xxxx123 ")
# except InsufficientFundsError:
#      print("Insufficient Balence in Account ")
# except ValueError:
#      print("Please Enter Valid input (Dont Enter Alphabets , Alnums, symbols )")


#^---------------------------------------------------------------------------------------------------
#! Custom exception for string concatenation:
#* Write a program that takes two inputs and concatenates them. If the user enters a number instead of a string, raise a NotAStringError.

#*syntax-1
# class NotAStringError(Exception):pass
# def checkstr():
#  try:
#   a = input("Enter first  string :").split()   # ["my","name","is"]
#   b = input("Enter Second String : ").split()  #["Anthony","Gunjalwish"]
#   l1= []
#   for i in a:
#      if not i.isalpha():
#        raise NotAStringError
#      else:
#           l1.append(i)
#   l2 = []
#   for j in b:
#    if not j.isalpha():
#      raise NotAStringError
#    else:
#     l2.append(j)

#   else:
#      print("".join(l1)+"".join(l2))
#  except NotAStringError:
#      print("Input must be string - Dont Ente any other data type input")
#  except ValueError:
#      print("Dont Enter alnums, alnums , symbols")
# checkstr()

#*syntax-2  replace alphabet rahil
# class NotAStringError(Exception):pass
# try:
#  a = input("Enter first  string :")
#  b = input("Enter Second String : ")
#  if not a.isalpha() or not b.isalpha():
#         raise NotAStringError
#  else:
#      print(a+b)
# except NotAStringError:
#      print("Input must be string - Dont Ente any other data type input")
# except ValueError:
#      print("Dont Enter alnums, alnums , symbols")




#*syntax-3
# class NotAStringError(Exception):pass
# def checkstr():
#  try:
#   a = input("Enter first  string :").split()   
#   b = input("Enter Second String : ").split() 
#   res = ""
#   for i in a+b:
#      if not i.isalpha():
#        raise NotAStringError
#      else:
#           res = res+i
#   print(res)

#  except NotAStringError:
#      print("Input must be string - Dont Ente any other data type input")
#  except ValueError:
#      print("Dont Enter alnums, alnums , symbols")
# checkstr()




#*syntax-4
# class NotAStringError(Exception):pass
# def checkstr():
#  try:
#   a = input("Enter first  string :").split()   # ["my","name","is"]
#   b = input("Enter Second String : ").split()  #["Anthony","Gunjalwish"]
#   l1 = ""
#   for i in a:
#      if not i.isalpha():
#        raise NotAStringError
#      else:
#           l1 = l1+i
#   l2 = ""
#   for j in b:
#    if not j.isalpha():
#      raise NotAStringError
#    else:
#     l2 =l2+j

#   print(l1+l2)
#  except NotAStringError:
#      print("Input must be string - Dont Ente any other data type input")
#  except ValueError:
#      print("Dont Enter alnums, alnums , symbols")

# checkstr()



# class NotAStringError(Exception):pass
# def checkstr():
#  try:
#   a = input("Enter first  string :").split()   
#   b = input("Enter Second String : ").split() 
#   res = ""
#   for i in a+b:
#      if not i.isalpha():
#        raise NotAStringError
#      else:
#           res = res+i
#   print(res)

#  except NotAStringError:
#      print("Input must be string - Dont Ente any other data type input")
#  except ValueError:
#      print("Dont Enter alnums, alnums , symbols")
# checkstr()



# s = input('Enter text  : ')
# s = s.replace(" ","")
# print(s)



#^---------------------------------------------------------------------------------------------------
