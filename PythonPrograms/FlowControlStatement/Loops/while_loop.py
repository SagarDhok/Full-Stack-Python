
# * LEVEL_1
#! printing 1 to n number
# n = int(input("ENTER A NUMBER : "))
# if(n<=0):
#  print(f"{n} is invalid input")
# else:
#  i = 1
#  while(i<=n):
#      print(i)
#      i=i+1
#  else:
#      print("it is else block")
# ------------------------------------------------------------------------------------------------------------
#!printing n to 1 number
# n = int(input("ENTER A NUMBER : "))
# if(n<=0):
#  print(f"{n} is invalid input")
# else:
#  i = n
#  while(i>=1):
#   print(i)
#   i=i-1
#  else:
#      print("it is else block")

# ? ============================================================================================================
#!printing multiplication table
# n = int(input("ENTER A NUMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = 1
# while(i<=10):
#      print(f'{n}X {i} = {n*i}')
#      i=i+1

# ------------------------------------------------------------------------------------------------------------
#!printing multiplication table upto which you mulplication
# n = int(input("ENTER NUNBER FOR WHICH YOU WANT MULTIPLICATION TABLE : "))
# m = int(input("ENTER NUMBER UPTO WHICH YOU WANT MULTIPLICATION "))
# i = 1
# while(i<=m):
#      print(f" {n} X {i} = {n*i}")
#      i=i+1
# else:
#      print("it is else block")

# ------------------------------------------------------------------------------------------------------------
#!printing multiplication table from which to upto which you mulplication
# n = int(input("ENTER NUNBER FOR WHICH YOU WANT MULTIPLICATION TABLE : "))
# i = int(input("ENTER FROM WHERE YOU WANT TO START MULTIPLICATION  : "))
# m = int(input("ENTER NUMBER UPTO WHICH YOU WANT MULTIPLICATION :  "))
# while(i<=m):
#      print(f" {n} X {i} = {n*i}")
#      i=i+1
# else:
#      print("it is else block")

# ------------------------------------------------------------------------------------------------------------
#!reverse multiplication table
# n = int(input("ENTER A NUMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = int(input("where to start "))
# m = int(input("where to end"))
# while(i>=m):
#      print(f'{n}X {i} = {n*i}')
#      i=i-1

# ------------------------------------------------------------------------------------------------------------
# !reverse multiplication table by taking starting and ending from user
# n = int(input("ENTER A NUMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = int(input("where to start "))
# m = int(input("where to end"))
# while(i>=m):
#      print(f'{n}X {i} = {n*i}')
#      i=i-1

# ? ========================================================================================================
#!program for accepting a word a printing its char by char
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5


# *logic1
# word = input("ENTER A WORD :")
# i = 0
# while(i<len(word)):
#      print(word[i])
#      i = i+1

# ? or

# word = input("ENTER A WORD :")
# i = int(input("from where you want "))
# while(i<=(len(word)-1)):
#      print(word[i])
#      i = i+1


# *logic2
# word= input("enter a word : ")
# i = -len(word)
# while(i<0):  #OR i<=-1
#      print(word[i])
#      i = i + 1

# ----------------------------------------------------------------------------------------------------------
#! PROGRAM FOR ACCEPTING A WORD A PRINTING ITS CHAR BY CHAR IN REVERSE ORDER
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5

# * logic1
# word = input("ENTER A WORD : ")
# i = -1
# while(i>=-len(word)):
#      print(word[i])
#      i = i-1
# else:
#      print("it is else block")

# * logic2
# word = input("ENTER A WORD : ")
# i = (len(word)-1)
# while(i>=0):  #OR i>-1
#      print(word[i])
#      i=i-1

# ? =========================================================================================================
# ! PROGRAM FOR PRINTING EVEN NUMBERS WITHIN N
# * logic1
# n = int(input("HOW MANY NUMBER YOU WANT TO GENRATE : "))
# i = 0
# while(i<=n):
#      print(i)
#      i = i+2
# else:
#      print("IT IS ELSE BLOCK")

# * logic2
# n = int(input("ENTER A NUMBER : "))
# i = 0
# while(i<=n):
#    if (i%2==0):
#     print(i)
#    i= i+1


# *LOGIC_3:
# n = int(input("Enter a number: "))
# i = 0
# while i <= n:
#     if i % 2 != 0:
#         pass
#     else:
#         print(i)
#     i += 1


# ? =========================================================================================================
#!PROGRAM FOR PRINTING ODD NUMBER UPTO N
# *LOGIC_1:
# n = int(input("enter a number : "))
# i = 1
# while(i<=n):
#    print(i)
#    i=i+2
# else:
#    print("it is else block")

# *LOGIC_2:
# n = int(input("enter a number : "))
# i = 1             #OR 0
# while(i<=n):
#     if i%2!=0:
#       print(i)
#     i=i+1
# else:
#    print("it is else block")

# *LOGIC_3:
# n = int(input("Enter a number: "))
# i = 0                   #OR i = 1
# while i <= n:
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)
#     i += 1              #OR i = i + 2

# ? =========================================================================================================
#!PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBER UPTO N
# #*LOGIC_1:
# n= int(input("enter a  number "))
# i = 0
# while(i<=n):
#      if i%2 ==0:
#       print("even",i)
#      else:
#           print("odd",i)
#      i=i+1


# ? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBERS IN DECREASING ORDER
# *LOGIC_1:
# n = int(input("ENTER A NUMBER : "))
# i = n
# while(i>=0):
#      if i%2==0:
#       print("even",i)


# #*LOGIC_2:
# n= int(input("ENTER A NUMBER : "))
# i = n
# while(i>=0):
#      if i%2!=0:
#           pass
#      else:
#           print("even",i)
#      i=i-1
# ? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBERS IN DECREASING ORDER


# #*LOGIC_1:
# n= int(input("ENTER A VALUE : "))
# i = n
# while(i>=1):
#      if i%2!=0:
#       print(i)
#      i -=1
# else:
#      print("it is else block ")

# #*LOGIC_2:
# n= int(input("ENTER A VALUE : "))
# i = n
# while(i>=1):
#      if i%2==0:
#           pass
#      else:
#           print(i)
#      i-=1
# else:
#      print("it is else block ")
# ? =========================================================================================================
#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBERS IN DECREASING ORDER
# n = int(input("ENTER A NUMBER : "))
# i = n
# while(i>=0):
#      if i%2==0:
#       print("even",i)
#      else:
#        print("odd",i)
#      i=i-1

#! SUBSTRACTION BY -2
# n = int(input("ENTER A NUMBER: "))
# i = n

# while i >= 0:
#     print( i)
#     i -= 2

# ? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF NATURAL NUMBERS
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("invalid input please enter valid input ! ")
# else:
#      i = 0             #OR YOU CAN START FROM 0 ALSO
#      sum = 0
#      while(i<=n):
#           sum= sum+i
#           print(f"{i}")
#           i=i+1

#      else:
#           print(f"sum of {n} natural number {sum} ")


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

# *LOGIC_1:
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("invalid input please enter valid input ! ")
# else:
#      i = 1
#      sum = 0
#      sum_squares = 0
#      while(i<=n):
#           sum= sum+i
#           sum_squares=sum_squares+i*i
#           print(f"{i}")
#           i=i+1

#      else:
#           print(f"sum of {n} natural number {sum} and theire square is {sum_squares}")


# #*LOGIC_2:
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("invalid input please enter valid input ! ")
# else:
#      i = 0             #OR YOU CAN START FROM 0 ALSO
#      sum = 0
#      sum_squares = 0
#      while(i<=n):
#           sum= sum+i
#           sum_squares=sum_squares+i**2
#           print(f"{i}, sum= {sum},sum_squares={sum_squares}")
#           i=i+1

#      else:
#           print(f"sum of {n} natural number {sum} and theire square is {sum_squares}")


# ? =========================================================================================================
#!  PROGRAM FOR FINDING PRODUCT OF NATURAL
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("it is invalid input  ")
# else:
#   i = 1
#   sum_product = 1
#   while(i<=n):
#      sum_product = sum_product*i
#      print(i)
#      i+=1
#   else:
#      print(f"product of {n} natural number is {sum_product}")

# ? =========================================================================================================
#!  PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL
# n= int(input("ENTER A NUMBER : "))
# i = 1
# sum_product = 1
# product_square  = 1
# while(i<=n):
#      sum_product = sum_product*i
#      product_square = product_square*i**2
#      print(i)
#      i+=1
# else:
#      print(f"product of {n} natural number is {sum_product} and square of product is {product_square} ")
# ? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF CUBE OF NATURAL NUMBERS UPTO N

# *LOGIC_1:
# n = int(input("enter a number : "))
# i = 1
# sum = 0
# sum_cubes= 0
# while(i<=n):
#      sum = sum+i
#      sum_cubes = sum_cubes+i**3
#      print(i)
#      i = i+1
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")

# *LOGIC_2:
# n = int(input("enter a number : "))
# i = 1
# sum = 0
# sum_cubes= 0
# while(i<=n):
#      sum = sum+i
#      sum_cubes = sum_cubes+i*i*i
#      print(i)
#      i = i+1
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")

# ? =========================================================================================================
#!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF SQUARE CUBE OF NATURAL UMBERS UPTO N
# n = int(input("ENTER A NUMBER "))
# i = 1
# sum=0
# sum_square= 0
# sum_cube = 0
# while(i<=n):
#      sum = sum + i
#      sum_square = sum_square + i**2
#      sum_cube = sum_cube + i**3
#      print(i)
#      i=i+1
# else:
#      print(f"sum of {n} is {sum} and sum of squares {sum_square} and sum of cube is {sum_cube}")
# ? =========================================================================================================
#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT
# num = int(input("ENTER A DIGIT WHOSE SUM YOU WANT : "))
# if (num<=0):
#      print("You have entered invalid input ! please enter valid input ")
# else:
#  sum = 0
#  temp_num = num
# while(num>0):
#       r = num%10
#       sum = sum + r
#       num = num//10
# else:
#  print(f"sum of {temp_num} is {sum}")

# ? =========================================================================================================
#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING
# s = "python"
# i =0
# while(i<len(s)):
#      if s[i]=="o":
#           break
#      print(s[i])
#      i = i+1
# else:
#      print("it is else block")


# ? =========================================================================================================
#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER
# 5 = 1*2*3*4*5
# 5 = 5*4*3*2*1

# *LOGIC_1:
# n = int(input("enter a number : "))
# fact = 1
# i = 1
# while(i<=n):
#         fact= fact*i
#    # print(i,fact)
#         i= i+1
# count = len(str(fact))
# print(f"factorial of {n} is {fact} ")
# print(f"factorial of {n} is {count} ")


# *LOGIC_2:
# n  = int(input("enter a number : "))
# i = n
# fact = 1
# while(i>0):
#      fact = fact*i
#      # print(i,fact)
#      i = i-1
# else:
#      print(f"factorial of {n} is {fact}")
# ? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE
# * LOGIC_1
# ? IN REVERSE ORDER CAUSE DIVDING RIGHT
# num = int(input("ENTER A NUMBER  : "))
# while(num>0):
#       d = num%10
#       if d%2==0:
#        print(d)
#       num = num//10

# #* LOGIC_2
# num = int(input("ENTER A NUMBER  : "))
# list = []
# while(num>0):
#       d = num%10
#       if d%2==0:
#        list.append(d)
#       num = num//10
# else:
#      list.reverse()
#      print(list)


# ? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE


# * LOGIC_1
# ? IN REVERSE ORDER CAUSE DIVDING RIGHT
# num = int(input("ENTER A DIGIT : "))
# while(num>1):
#      r = num%10
#      if r%2!=0:
#        print(r)
#      num = num//10

# #* LOGIC_2
# ? Print the even digits in reverse order (original order in number)
# num = int(input("ENTER A NUMBER  : "))
# list = []
# while(num>1):
#       d = num%10
#       if d%2!=0:
#        list.append(d)
#       num = num//10
# else:
#      list.reverse()
#      print(list)
# ? =========================================================================================================
# s = "my name is anthony gunajlwsih  "
# x = s.split()
# print(x)
# i = 0
# while(i<len(x)):
#      print(x[i] ,"=",len(x[i]))
#      i= i+1
# s = " ".join(x)
# ? =========================================================================================================
#! PROGRAM WHICH WILL PRINT REVERSE A VALUE WITHOUT USING EXTEND AND SLICING
# num = int(input("enter a value : "))
# onum = num
# rn = 0
# while num > 0:
#     digit = num % 10
#     rn = rn * 10 +digit
#     num = num // 10
# print(f"reverse of {onum} is {rn}")

# ? =========================================================================================================
#! WRITE A PYTHON PROGRAM WHICH WILL GET UPPERCASE AND LOWERCASE LETTERS SEPERATELY
# ? =========================================================================================================
#! 08-10-2024
# s = "  PYTHON IS OOP LANG "
# x = s.split()
# # print(x)
# i = 0
# while i < len(x):
#       print(x[i])
#       j = 0
#       while j < len(x[i]):
#        print(x[i][j])
#        j = j + 1
#       i = i + 1
# ? =========================================================================================================
# #! WRITE A PROGRAM WHICH WILL GET UPPERCASE AND LOWERCASE LATTERS SEPERATELY
# word = input("ENTER TEXT : ")
# uppercase = []
# lowercase = []
# i = 0
# while(i<len(word)):     
#      if word[i].isupper():
#       uppercase.append(word[i])
#      else:
#        lowercase.append(word[i])
#      i = i+1
# print("Uppercase Letters:"," ".join(uppercase).strip())
# print("Lowercase Letters:"," ".join(lowercase).strip())
# ? =========================================================================================================
#! CHECK WHETHER GIVEN NUMBER IS PRIME OR NOT
# n = int(input("ENTER A NUMBER  : "))
# if n <= 1:
#  print(f"{n} is invalid input ")
# else:
#   i = 2
#   res = "PRIME"
#   while i <= n//2:
#       if n % i == 0:
#        res = "NOT PRIME"
#        break
#       i = i + 1
# if "PRIME" in res:
#   print(f"{n} is {res}")
# else:
#   print(f"{n} is {res}")
 #   res = "PRIME" if res else "NOT PRIME"
#   print(f"{n} is {res}")
# ? =========================================================================================================
# #! PROGRAM FOR READING INPUT FROM KEYBOARD
# n= int(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER : "))
# if n<=0:
#      print("INVALID INPUT ! PLEASE ENTER VALID INPUT !!")
# else:
#      i = 1
#      lst  = []
#      while i<=n:
#           value = int(input(f"ENTER {i} VALUE : "))
#           lst.append(value)
#           i = i+1
#      print(lst) 
# ? =========================================================================================================
#! PROGRAM WHICH WILL ACCEPT ANY WORD AND DECIDE WHETHER IT IS VOWEL OR NOT 
# word = input("ENTER A WORD : ").lower()
# for i in word:
#      if i in "aeiou" :
#       print("it is vowel" )
#       break
# else:
#     print(" it is not vowel ")
# ? =========================================================================================================
#! WRITE A PYTHON PROGRAM WHICH WILL ACCEPT LINE OF TEXT AND DISPLAY ONLY VOWELS
#*LOGIC-1
# text = input("enter  a line of text : ").lower()
# vowels = []
# for ch in text:
#     if ch in "aeiou":
#      vowels.append(ch)
# print(vowels)

#*LOGIC-2
# text = input("enter  a line of text : ").lower()
# for ch in text:
#     if ch not in "aeiou":
#      continue
#     else:
#      print(ch,end= " ")
# ? =========================================================================================================
#! PRPOGRAM WHICH WILL ACCEPT LINE OF TEXT WITH DIGITS AND PRINT ONLY ITS DIGITS
#*LOGIC-1
# line = input("ENTER ALPHA NUMERICAL VALUE : ")
# for i in line:
#     if i.isdigit():
#       print(i)
    
#*LOGIC-2
# line = input("ENTER ALPHA NUMERICAL VALUE : ")
# for i in line:
#     if not i.isdigit():
#       continue
#     else:
#         print(i)
    
# ? ================================================================================================
#! PROGRAM WHICH WILL ACCEPT LINE OF TEXT AND DISPLAY ONLY SPECAIL SYMBOL
# line = input("ENTER LINE OF TEXT : ")
# for i in line:
#     if i.isalnum():
#         continue
#     else:
#         print(i,end=" ")
# ? ================================================================================================
#! PROGRAM WHICH WILL ACCEPT LINE OF TEXT AND DISPLAY ONLY ALPHABETS
#*LOGIC-1
# line = input("ENTER LINE OF TEXT : ")
# for i in line:
#     if not i.isalpha():
#         continue
#     else:
#         print(i,end=" ")

# line = input("ENTER LINE OF TEXT : ")
# for i in line:
#     if  i.isalpha():
#      print(i,end=" ")
#? ================================================================================================
#! PROGRAM WHICH WILL ACCEPT LINE OF TEXT AND GET WORDS WHOESE LENGHT RANGE BETWEEN 2 TO 3
# #*LOGIC-1
# line = input("ENTER LINE OF TEXT : ")
# x   = line.split()
# # print(x)
# for i in x:
#     if len(i)==2 or len(i)==3:
#      print(i,len(i))

#*LOGIC-2
# line = input("ENTER LINE OF TEXT : ")
# x   = line.split()
# # print(x)
# for i in range(len(x)):
#     if len(x[i])==2 or len(x[i])==3:
#        print(x[i],len(x[i]))
# ? ================================================================================================
