
# ^----------------------------------------------------------------------------------------------
# * LEVEL-1:
# * SYNTAX-1
# def getval():
#      return int(input("ENTER A NUMERICAL VALUE : "))

# def calculation(val):
#      def square():
#           n = val()
#           res = n**2
#           return n,res
#      return square

# result = calculation(getval)
# n, res = result()
# print(f"Square of {n} = {res}")
# def getval():
#      return int(input("ENTER A NUMERICAL VALUE : "))

# * SYNTAX-2
# def getval():
#      return int(input("ENTER A NUMERICAL VALUE : "))

# def calculation(val):
#      def square():
#           n = val()
#           res = n**2
#           return n,res
#      return square

# result = calculation(getval)()
# # print(f"Square of {result[0]} = {result[1]}")
# #print(f"Square of {result}")           #& ANSWER IN TUPLE (n,n**2)
# ^----------------------------------------------------------------------------------------------
#! WRITE A DECORATOR THAT CONVERTS THE OUTPUT OF A FUNCTION TO UPPERCASE AND LOWERCASE  LETTERS  IF THE OUTPUT IS A STRING  .

# * LEVEL-1:
# * SYNTAX-1
# def gettext():
#      return input("ENTER A LINE OF TEXT : ")

# def Ucase(gettext):
#      def operation():
#         n = gettext()
#         res = n.upper()
#         return n , res
#      return operation

# def Lcase(gettext):
#     def operation():
#         n = gettext()
#         res =n.lower()
#         return n, res
#     return operation

# result1= Ucase(gettext)
# result2= Lcase(gettext)
# n1,res1 = result1()
# n2,res2 = result2()
# print(f"{n1} = {res1}")
# print(f"{n2} = {res2}")


# * SYNTAX-2
# def gettext():
#      return input("ENTER A LINE OF TEXT : ")

# def Ucase(gettext):
#      def operation():
#         n = gettext()
#         res = n.upper()
#         return n , res
#      return operation

# def Lcase(gettext):
#     def operation():
#         n = gettext()
#         res =n.lower()
#         return n, res
#     return operation

# result1= Ucase(gettext)()
# print(f"{result1[0]} = {result1[1]}")
# result2= Lcase(gettext)()
# print(f"{result2[0]} = {result2[1]}")
# ^----------------------------------------------------------------------------------------------
# * LEVEL-2
# * SYNTAX-1
# def square(getval):
#      def operation():
#           n = getval()
#           res = n**2
#           return n , res
#      return operation

# @square
# def getval():
#      return int(input("ENTER A NUMERICAL VALUE : "))

# res = getval()
# print(f" {res[0]} = {res[1]}")


# * LEVEL-2
# * SYNTAX-2
# def square(getval):
#      def operation():
#           n = getval()
#           res = n**2
#           return n , res
#      return operation

# @square
# def getval():
#      return int(input("ENTER A NUMERICAL VALUE : "))

# n, res = getval()
# print(f" {n} = {res}")

# ^----------------------------------------------------------------------------------------------
# * LEVEL-2
# * SYNTAX-1


# def cube(getval):
#     def sqrtop():
#         n,square_res ,sqrt_res = getval()
#         cube_res = n**3
#         return n, square_res ,sqrt_res,cube_res
#     return sqrtop

# def sqrt(getval):
#     def sqrtop():
#         n,square_res = getval()
#         sqrt_res = n**0.5
#         return n, square_res ,sqrt_res
#     return sqrtop


# def square(getval):
#      def squareop():
#       n = getval()
#       square_res = n **2
#       return n , square_res
#      return squareop

# @cube
# @sqrt
# @square
# def getval():
#      return int(input("ENTER A  NUMERICAL VALUE : "))

# n,square_res, sqrt_res,cube_res=getval()
# print(f"SQAURE {n} = {square_res}")
# print(f"SQAURE ROOT {n} = {sqrt_res}")
# print(f"CUBE {n} = {cube_res}")


# * SYNTAX-2
# def cube(getval):
#     def sqrtop():
#         n,square_res ,sqrt_res = getval()
#         cube_res = n**3
#         return n, square_res ,sqrt_res,cube_res
#     return sqrtop

# def sqrt(getval):
#     def sqrtop():
#         n,square_res = getval()
#         sqrt_res = n**0.5
#         return n, square_res ,sqrt_res
#     return sqrtop


# def square(getval):
#      def squareop():
#       n = getval()
#       square_res = n **2
#       return n , square_res
#      return squareop

# @cube
# @sqrt
# @square
# def getval():
#      return int(input("ENTER A  NUMERICAL VALUE : "))

# res= getval()
# print(f"SQAURE {res[0]} = {res[1]}")
# print(f"SQAURE ROOT {res[0]} = {res[2]}")
# print(f"CUBE {res[0]} = {res[3]}")

# ^----------------------------------------------------------------------------------------------
# ! CONVRTING SENTENCE INTO UPPERCASE AND LOWERCASE

# def lcase(gettext):
#      def loperation():
#           text , u_res =  gettext()
#           l_res = text.lower()
#           return text,u_res,l_res
#      return loperation


# def ucase(gettext):
#      def uoperation():
#           text = gettext()
#           u_res = text.upper()
#           return text ,u_res
#      return uoperation

# @lcase
# @ucase
# def gettext():
#      return input("Enter a line of text : ")


# text,u_res,l_res = gettext()
# print(f"{text} = {u_res}")
# print(f"{text} = {l_res}")
# ^----------------------------------------------------------------------------------------------

# ^----------------------------------------------------------------------------------------------
