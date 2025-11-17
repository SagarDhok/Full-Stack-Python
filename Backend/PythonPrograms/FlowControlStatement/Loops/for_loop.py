
# * LEVEL_1
#! printing 1 to n number
# n= int(input("ENTER A NUMBER : "))
# for i in range(1,n+1):
#      print(i)
# ------------------------------------------------------------------------------------------------------------
#! printing n to 1 number
# n = int(input("ENTER A NUMBER : "))
# for i in range(1 , n+1):
#      print(i)u

# ? ============================================================================================================
#!printing multiplication table
# n= int(input("ENTER A NUMBER WHOSE MULTIPLICATION TABLE YOU WANT : "))
# S = int(input("ENTER VALUE FROM WHERE YOU WANT TO START TABLE "))
# E = int(input("ENTER VALUE FROM WHERE YOU WANT TO START TABLE "))
# for i in range(S,E+1):
#      print(f"{n}X{i}={n*i}")

# ----------------------------------------------------------------------------------------------------------

# n= int(input("ENTER A NUMBER WHOSE MULTIPLICATION TABLE YOU WANT : "))
# S = int(input("ENTER VALUE FROM WHERE YOU WANT TO start TABLE "))
# E = int(input("ENTER VALUE FROM WHERE YOU WANT TO end TABLE "))
# for i in range(S,E-1,-1):
#      print(f"{n}X{i}={n*i}")

# ? =========================================================================================================
# ! PROGRAM FOR PRINTING EVEN NUMBERS WITHIN N
# *LOGIC_1:
# n = int(input("ENTER A NUMBER WHERE YOU WANT TO GENERATE EVEN NUMBERS : "))
# for i in range(0,n+1,2):
#      print(i)

# *LOGIC_2:
# n = int(input("ENTER A NUMBER WHERE YOU WANT TO GENERATE EVEN NUMBERS : "))
# for i in range(n+1):
#  if i%2==0:
#     print(i)

# *LOGIC_3:
# n = int(input("ENTER A NUMBER WHERE YOU WANT TO GENERATE EVEN NUMBERS : "))
# for i in range(n+1):
#      if i%2!=0:
#           pass
#      else:
#           print(i)


# ? =========================================================================================================
#!  PROGRAM FOR PRINTING ODD NUMBER UPTO N
# *LOGIC_1
# n= int(input("ENTER A NUMBER : "))
# for i in range (1,n+1,2):
#      print(i)

# *LOGIC_2
# n= int(input("ENTER A NUMBER : "))
# for i in range(1,n+1):  #OR 0
#      if i%2!=0:
#           print(i)
# else:
#      print("it is else block")

# *LOGIC_3
# n= int(input("ENTER A NUMBER : "))
# for i in range(1,n+1):
#      if i%2==0:
#           pass
#      else:
#           print(i)
# ? =========================================================================================================
#! PROGRAM FOR ACCEPTING A WORD A PRINTING ITS CHAR
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5

# *LOGIC_1
# word= input("ENTER A WORD : ")
# for i in word:
#      print(i)

# *LOGIC_2
# word= input("enter a word : ")
# for i in range(0,len(word)):
#      print(word[i])

# *LOGIC_3
# word = input("ENTER A WORD : ")
# for  i in range((-len(word)),0):
#      print(word[i])
# ? =========================================================================================================
#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBER UPTO N
# n = int(input("enter a number "))
# for i in range(n+1):
#      if i%2==0:
#           print("even",i)
#      else:
#           print("odd",i)


# ? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBERS IN DECREASING ORDER
# *LOGIC_1
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2==0:
#           print(i)
#

# *LOGIC_2
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2!=0:
#           pass
#      else:
#           print(i)

# ? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBERS IN DECREASING ORDER
# *LOGIC_1
# n =  int(input("enter a number "))
# for i in range(n,1,-1):
#      if i%2!=0:
#           print(i)


# *LOGIC_2
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2==0:
#           pass
#      else:
#           print(i)
# ? =========================================================================================================
#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBERS IN DECREASING ORDER
# *LOGIC_1
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2==0:
#           print("EVEN",i)
#      else:
#           print("ODD",i)


#! SUBSTRACTION BY -2 IN DECREASING ORDER
# n = int(input("enter a number :  "))
# for i in range(n,0,-2):
#      print(i)
# ? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF NATURAL NUMBERS
# n = int(input("ENTER A NUMBER : "))
# sum = 0
# for i in range(n+1):
#      sum = sum + i
#      print(f"numbers = {i}  sum = {sum}")
# else:
#      print(f"sum of {n} natural numbers  is {sum}")

# ? =========================================================================================================
#! PRINTING SUM AND SUM SQUARES OF NATURAL NUMBERS
# 1 s sum is      1
# 2 and 1 sum is  3
# 3 and 3 sum is  6
# 4 and 6 sum is  10
# 5 and 10 sum is 15
# ---------------------
# sum of n is natural n is 15

# 1 s square is 1s
# 2 s square is 4
# 3 s square is 9
# 4 s square is 16
# 5 s square is 25
# -----------------------
# sum of squares  =  55

# *LOGIC_1
# *LOGIC_1
# n = int(input("ENTER A NUMBER UPTO WHICH YOU WANT SUM AND SUM OF THEIRE SQUARES : "))
# sum = 0
# sum_squres= 0
# for i in range (n+1):
#      sum = sum + i
#      sum_squres= sum_squres+i*i
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} and sum of squres of  natural number is {sum_squres}")

# *LOGIC_2
# n = int(input("ENTER A NUMBER UPTO WHICH YOU WANT SUM AND SUM OF THEIRE SQUARES : "))
# sum = 0
# sum_squres= 0
# for i in range (n+1):
#      sum = sum + i
#      sum_squres= sum_squres+i**2
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} and sum of squres of  natural number is {sum_squres}")

# ? =========================================================================================================
#!  PROGRAM FOR FINDING PRODUCT OF NATURAL

# n = int(input("ENTER A NUMBER UPTO WHERE YOU WANT PRODUT : "))
# sum_product = 1
# for i in range(1,n+1):
#      sum_product*= i
#      print(i)
# else:
#      print(f"product of {n} natural number is {sum_product}")

# ? =========================================================================================================
#!  PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL
# n= int(input("ENTER A NUMBER : "))
# sum_product = 1
# product_square  = 1
# for i in range(1,n+1):
#      sum_product = sum_product*i
#      product_square = product_square*i**2
#      print(i)
# else:
#      print(f"product of {n} natural number is {sum_product} and square of product is {product_square} ")
# ? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF PRODUCT OF NATURAL NUMBERS UPTO N

# *LOGIC_1:
# n = int(input("enter a number : "))
# sum = 0
# sum_cubes= 0
# for i in range(n+1):
#      sum = sum+i
#      sum_cubes = sum_cubes+i*i*i
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")


# *LOGIC_2:
# n = int(input("enter a number : "))
# sum = 0
# sum_cubes= 0
# for i in range(n+1):
#      sum = sum+i
#      sum_cubes = sum_cubes+i**3
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")
# ? =========================================================================================================
# #!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF SQUARE CUBE OF NATURAL UMBERS UPTO N
# n = int(input("ENTER A NUMBER "))
# sum=0
# sum_square= 0
# sum_cube = 0
# for i in range(1,n+1):
#      sum = sum + i
#      sum_square = sum_square + i**2
#      sum_cube = sum_cube + i**3
#      print(f"{i},sum={sum}, sum of squares = {sum_square}, sum of cubes = {sum_cube}")
# else:
#      print(f"sum of {n} is {sum} and sum of squares {sum_square} and sum of cube is {sum_cube}")
# ? =========================================================================================================\
#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT
# *LOGIC_0
# num = int(input("ENTER A DIGIT WHOSE SUM YOU WANT : "))
# if (num<=0):
#      print("You have entered invalid input ! please enter valid input ")
# else:
#  sum = 0
#  temp_num = num
# for digit in str(num):
#       r = num%10 +
#       sum = sum + r
#       num = int(num)//10
# else:
#  print(f"sum of {temp_num} is {sum}")

# *LOGIC_1
# n = input("enter a value ")
# d= n.split()
# # print(d,type(d))
# # print(d[0 ],type(d[0]))
# s = 0
# for i in d[0]:
#     s = s+int(i)
# else:
#      print(f"sum of {n} is {s} ")

# *LOGIC_2
# n = input("enter a number : ")
# list  = list(n)
# # print(list,type(list))
# sum =  0
# for i in list:
#     sum = sum+int(i)
# else:
#      print(f"sum of {n} is {sum } ")

# *LOGIC_3
# n = input("enter a number ")
# sum = 0
# for i in n:
#      sum = sum+int(i)
# else:
#      print(f"sum of {n} is {sum } ")


# ? =========================================================================================================\
#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING

# s = "python"
# for ch in s:
#      if (ch=="o"):
#           break
#      print(ch)
# else:
#      print("it is else block")
# ? =========================================================================================================\
#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER
# 5 = 1*2*3*4*5
# 5 = 5*4*3*2*1

# *LOGIC_1:
# n = int(input("enter a number : "))
# fact = 1
# for i in range(1,n+1):
#      fact= fact*i
#      # print(i,fact)
# else:
#      print(f"factorial of {n} is {fact} ")

# *LOGIC_2:
# n  = int(input("enter a number : "))
# fact = 1
# for i in range(n,0,-1):
#      fact = fact*i
#      # print(i,fact)
# else:
#      print(f"factorial of {n} is {fact}")
# ? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE
# *LOGIC_1:
# n = input("enter a number ")
# for i in n:
#      if int(i)%2==0:
#           print(i)

# *LOGIC_2:
# n = input("enter a number ")
# x = n.split()
# for i in x[0]:
#      if int(i)%2==0:
#           print(i)

# *LOGIC_3:
# n = input("enter a number ")
# list = list(n)
# for i in list:
#      if int(i)%2==0:
#           print(i)


# ? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE
# *LOGIC_1:
# n = input("enter a number ")
# for i in n:
#      if int(i)%2!=0:
#           print(i)

# *LOGIC_2:
# n = input("enter a number ")
# x = n.split()
# for i in x[0]:
#      if int(i)%2!=0:
#           print(i)

# *LOGIC_3:
# n = input("enter a number ")
# list = list(n)
# for i in list:
#     if int(i) % 2 != 0:
#         print(i)

# ? =========================================================================================================
#! 08-10-2024
# s = input(" ENTER A LINE : ")
# x = s.split()
# for i in x:
#     print(i)
#     for ch in i:
#         print(ch)
# ? =========================================================================================================
#! WRITE A PROGRAM WHICH WILL GET UPPERCASE AND LOWERCASE LATTERS SEPERATELY
# word = input("ENTER TEXT : ")
# uppercase = []
# lowercase = []

# for i in word:
#      if i.isupper():
#       uppercase.append(i)
#      else:
#        lowercase.append(i)
# print("Uppercase Letters:"," ".join(uppercase).strip())
# print("Lowercase Letters:"," ".join(lowercase).strip())
     
# ? =========================================================================================================
#! CHECK WHETHER GIVEN NUMBER IS PRIME OR NOT 
# n=  int(input("ENTER A NUMBER : "))
# res = "PRIME"
# for i in range(2,n):
#      if n%i == 0:
#           res = "NOT PRIME"
#           break

# if res == "PRIME":
#   print(f"{n} is prime number ")
# else:
#   print(f"{n} is prime Not a  number ")
    

# ? =========================================================================================================
#! PROGRAM FOR READING INPUT FROM KEYBOARD
# n= int(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER : "))
# if n<=0:
#      print("INVALID INPUT ! PLEASE ENTER VALID INPUT !!")
# else:
#      lst  = []
#      for i in range(1,n+1):
#           value = int(input(f"ENTER {i} VALUE : "))
#           lst.append(value)
#      print(lst) 

# ? =========================================================================================================
#! PROGRAM WHICH WILL ACCEPT ANY WORD AND DECIDE WHETHER IT IS VOWEL OR NOT  
# word = input("enter a word : ").lower()
# i = 0
# while(i<len(word)):
#      if word[i] in "aeiou":
#           print(f"{word[i]} is vowel")
#      else:
#         print(f"{word[i]} is not vowel")
#      i +=1
#?  =========================================================================================================
