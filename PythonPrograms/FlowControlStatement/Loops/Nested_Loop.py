# ? ================================================================================================
# * Ex-1
# for i in range(1,5):
#      print("outer loop : ",i)
#      for j in range(1,4):
#           print(j)
#      else:
#           print("else block of inner loop")
# else:
#      print("else block of outer loop")

# ? ===============================================================================================
# * Ex-2
# i = 1
# while(i<=5):
#      print("outer loop : ",i)
#      j = 1
#      while(j<=4):
#       print(j)
#       j= j+1
#      else:
#        print("it is else block of inner loop")
#      i = i+1
# else:
#      print("it is else block of outer loop")
# ? ===============================================================================================
# * Ex-3
# i = 5
# while(i>=1):
#      print("outer loop : ",i)
#      for j in range(4,0,-1):
#           print(j)
#      else:
#           print("it is else block of inner for loop ")
#      i = i-1
# else:
#      print("it is else block of outer while loop ")
# ? ===============================================================================================
# * Ex-4
# for i in range(5,0,-1):
#      print("outer loop : ",i)
#      j = 1
#      while(j<=5):
#           print(j)
#           j = j+1
#      else:
#           print("it is else block of inner while loop ")
# else:
#      print("it is else block of outer for loop ")

# ? ===============================================================================================
#! PROGRAM FOR GENRATING MULTIPLICATION TABLE FROM 2 TO N
# * FOR_LOOP:
# n = int(input("ENTER A NUMBER UPTO WHERE YOU WANT TO GENERATE MULTIPLICATION TABLE : "))
# if n<=0:
#      print("it is invalid input")
# else:
#      for i in range(2,n+1):
#          print("------------")
#          for j in range(1,11):
#            print(f"{i} X {j} = {i*j}")

# * WHILE_LOOP:
# n = int(input("ENTER A NUMBER UPTO WHERE YOU WANT TO GENERATE MULTIPLICATION TABLE : "))
# if n<=0:
#      print("it is invalid input")
# else:
#      i = 2
#      while i<=n:
#           print("______________")
#           j=1
#           while j<=10:
#                print(f"{i} X {j} = {i*j}")
#                j = j+1
#           i +=1


# ? ===============================================================================================
#! PROGRAM FOR GENRATING MULTIPLICATION TABLE FROM RANDOM NUMBERS
# * WHILE_LOOP:
# n = int(input("ENTER A NUMBER YOU WANT TO GENERATE MULTIPLICATION TABLE : "))
# i = 1
# lst = []
# while i <= n:
#     val = int(input(f"enter {i} value : "))
#     lst.append(val)
#     i = i + 1
# print("GIVEN lst ", lst)
# i = 0
# while i < len(lst):
#     if lst[i] <= 0:
#         print("invalid input")
#     else:
#         print(lst[i])
#         print("MULTIPLICATION TABLE : ")
#         j = 1
#         while j <= 10:
#             print(f"{lst[i]} X {j} = {lst[i]*j}")
#             j = j + 1
#     i = i + 1

# * FOR_LOOP:
# n = int(input("enter how many values you want :  "))
# if n<=0:
#      print("it is invalid input ")
# else:
#      lst = list()
#      for i in range(1,n+1):
#         val = int(input(f"eneter {i} value : "))
#         lst.append(val)
#      print(lst)

#      for j in lst:
#          if j<=0:
#              print("invalid input : ")
#          else:
#              print("MULTIPLICATION TABLE FOR : ",j)
#              for k in range(1,11):
#                  print(f"{j} X {k} = {j*k}")

# ? ===============================================================================================
#! PROGRAM FOR CHECKING PRIME NUMBER BETWEEN GIVEN RANGE
# * FOR_LOOP:
# num = int(input("ENTER UPTO HOW MANY NUMBER YOU WANT TO GENRATE PRIME NUMBER : "))
# for i in range(2,num+1):
#      res = "PRIME"
#      for j in range(2,i):
#           if i%j == 0:
#            res = "NOT PRIME"
#            break                 # it increase the performance
#      if res =="PRIME":
#       print(i,"is",res)


# * WHILE_LOOP:
# num = int(input("ENTER UPTO HOW MANY NUMBER YOU WANT TO GENRATE PRIME NUMBER : "))
# i = 2
# nop =0
# while i <= num:  #10
#     j = 2 
#     res = True              
#     while j < i:               
#         if i % j == 0:         
#             res = False
#             break
#         j = j + 1
#     if res:
#         print(i)
#         nop = nop+1
#     i = i + 1
# print(f"Number of Primes within {num}={nop}")


# ? ===============================================================================================
