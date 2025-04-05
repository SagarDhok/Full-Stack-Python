#! Question : Nested Multiplication with Multiple Returns
# *Write a program where:
# * getval accepts three integers.
# * A nested function calculates:
# * Their product.
# * Their sum.
# * Their average.
# * Return and print all three results


# def getval():
#     return (
#         int(input("Enter first value : ")),
#         int(input("Enter second value : ")),
#         int(input("Enter third value : ")),
#     )


# def calculation():
#     def innercal():
#         a, b, c = getval()
#         product = a * b * c
#         sum = a + b + c
#         avg = sum / 3
#         return a, b, c, product, sum, avg

#     return innercal


# a, b, c, product, sum, avg = calculation()()
# print(f"Product of ({a},{b},{c}) = {product}")
# print(f"sum of ({a},{b},{c}) = {sum}")
# print(f"average of ({a},{b},{c}) = {avg}")

# ^----------------------------------------------------------------------------------------------
#! Question : Combining Two Lists
#* Modify the original code to accept two lists of integers and return their concatenated result.

# def getlst ():
#      l1 = [int(i) for i in input("Enter first list of values : ").split()] 
#      l2 = [int(i) for i in input("Enter Second list of values : ").split()]
#      return  l1 ,l2

# def conclst():
#      def concatop():
#           l1 ,l2 = getlst()
#           res= l1+l2
#           return l1,l2,res
#      return concatop
# l1,l2,res = conclst()()
# print(f"First list : {l1}")
# print(f"Second list : {l2}")
# print(f"Concaneted list : {res} ")


# def getlst ():
#      l1 = [int(i) for i in input("Enter first list of values : ").split()] 
#      l2 = [int(i) for i in input("Enter Second list of values : ").split()]
#      return  l1 ,l2

# def conclst():
#      def concatop():
#           l1 ,l2 = getlst()
#           l1.extend(l2)
#           return l1,l2,
#      return concatop
# l1,l2 = conclst()()
# print(f"First list concanete : {l1}")
# print(f"Second list unchanged : {l2}")

# ^----------------------------------------------------------------------------------------------
#! Challenge Exercise: Calculator with Nested Functions
#* Build a basic calculator program that allows the user to choose an operation (+, -, *, /) and input two numbers. Use nested functions to perform the calculations.

# def getval():
#      a = int(input("Enter First value : "))
#      b = int(input("Enter second value : "))
#      op = input("choose an operation (+, -, *, /) : ")
#      return a,b ,op

# def calculation():
#      def calcop():
#           a,b,op = getval()
#           if op == "+":
#                res = a+b
#           elif op == "-":
#                res = a-b
#           elif op == "*":
#                res =  a*b
#           elif op == "/":
#                res =  a/b
#           return a,b,op,res
#      return calcop

# a,b,op,res=calculation()()
# print(f"({a}{op}{b}) = {res}")
# ^----------------------------------------------------------------------------------------------
#! . Multi-level Calculation with Decorators
#* Write a program with three decorators:
#* One to calculate the square of a number.
#* One to calculate the cube of the number.
#* One to calculate the fourth power of the number.
#* Use these decorators on a function that gets a number from the user and returns the results for all three calculations


# def fourthpower(func3):
#      def calfourthpower():
#       n,sqr,cb = func3()
#       frtp = n**4
#       return n,sqr,cb,frtp
#      return calfourthpower


# def cube(func2):
#      def cbcal():
#           n,sqr = func2()
#           cb = n**3
#           return n,sqr,cb
#      return cbcal

# def square(func1):
#      def sqcal():
#           n = func1()
#           sqr = n*n
#           return n,sqr
#      return sqcal
# @fourthpower
# @cube
# @square
# def getval():
#      return int(input("Enter A Value : "))

# n,sqr,cb,frtp= getval()
# print("-"*50)
# print("Number\tSquare\tCube\tFourth Power")
# print(f"{n}\t{sqr}\t{cb}\t{frtp}")
# print("-"*50)

#* another way in one decorator 
# def power_calculator(func):
#     def wrapper():
#         num = func()
#         square = num ** 2
#         cube = num ** 3
#         fourth_power = num ** 4
#         print(f"Number: {num}\nSquare: {square}\nCube: {cube}\nFourth Power: {fourth_power}")
#     return wrapper

# @power_calculator
# def get_number():
#     return int(input("Enter a number: "))

# get_number()

# ^----------------------------------------------------------------------------------------------
#! Multi-Level String Transformation with Decorators
#* Write a program with three decorators:
#* One to reverse a string.
#* One to convert the string to uppercase.
#* One to add a prefix and suffix to the string (e.g., prefix: Start_, suffix: _End).

# def PrefixSuffix(func3):
#      def wrapper():
#           s,upr,rvs= func3()
#           pfxsfx = "Start_"+s+"_End"
#           return s,upr,rvs,pfxsfx
#      return wrapper

# def reverse(func2):
#      def wrapper():
#           s,upr= func2()
#           rvs = s[::-1]
#           return s,upr,rvs
#      return wrapper

# def uppercase(func1):
#      def wrapper():
#           s = func1()
#           upr = s.upper()
#           return s,upr
#      return wrapper

# @PrefixSuffix
# @reverse
# @uppercase
# def string():
#      return input("Enter Text : ")

# s,upr,rvs,PrefixSuffix=  string()
# print("Text : ",s)
# print("Uppercase : ",upr)
# print("Reverse : ",rvs)
# print("prefix and suffix : ",PrefixSuffix)