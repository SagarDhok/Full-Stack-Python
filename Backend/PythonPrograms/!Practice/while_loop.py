
# i=1
# while(i<=10): 
#      print(i)
#      i+=1

# i=10
# while(i>=1):   #10 #9 #8 #7 #6 #5 #4 #3 #2 #1
#      print(i)
#      i-=1

 
# n = int(input("ENTER A VALUE : "))
# if (n>100):
#      print("INVALID INPUT ENTER BELOW 100")
# else:
          
#  i = 100  
# while(i>=1):
#      print(i)
#      i = i-1


# n = int(input("ENTER A NUMBER : "))
 
# if (n<=0):
#      print("invalid input please enter valid input")

# else:
#      i=0
#      while(i<=n):
#       print(i)
#       i+=1

#      else:
#          print("it is while else block") 

# n = int(input("ENTER A VALUE : "))
# i=0
# while(i<=n):
#       print(i)
#       i+=1

# else:
#          print("it is while else block") 





#Program for Generating 1 to N Numebrs where N is +VE
#WhileLoopEx1.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     print("--------------------------------")
#     print("Numbers within :{}".format(n))
#     print("--------------------------------")
#     i=1 # InitLization Part
#     while(i<=n): # Conditional Part
#         print("{}".format(i),end=" ")
#         i=i+1 # OR i+=1  Updation part
#     else:
#         print()
#         print("--------------------------------")



# #Program for Generating 1 to N Numebrs where N is +VE
# #WhileLoopEx1.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     print("--------------------------------")
#     print("Numbers within :{}".format(n))
#     print("--------------------------------")
#     i=1 # InitLization Part
#     while(i<=n): # Conditional Part
#         print("\t\t{}".format(i))
#         i=i+1 # OR i+=1  Updation part
#     else:
#         print()
#         print("--------------------------------")




# word = input("ENTER A WORD:")
# i = 0
# while(i<=len(word)-1):
#  print(word[i])
#  i =  i+1



# n = int(input("enter a number:"))
# if (n<=0):
#      print(f"{n} is invalid input ")
# else:
#      i = n
#      while(i>=1):
#           print(i)
#           i -= 1
#      else:
#           print("it is else block")


# n = int(input("enter a number:"))
# if (n<=0):
#      print(f"{n} is invalid input ")
# else:
#      i = 0
#      while(i<=n):
#           print(i,end=" ")
#           i += 2
#      else:
#           print()
#           print("it is else block")















#odd number
# n = int(input("enter a number:"))
# if (n<=0):
#      print(f"{n} is invalid input ")
# else:
#      i = 1
#      while(i<=n):
#           print(i,end=" ")
#           i += 2
#      else:
#           print()
#           print("it is else block")




# n = int(input("enter a number:"))
# if (n<=0):
#      print(f"{n} is invalid input ")
# else:
#      i = n
#      while(i>=1):
#       if n%2 == 0:
#           print(i,end=" ")
#           i -= 0
#      else:
#           print()
#           print("it is else block")


# n = int(input("ENTER A NUMBER : "))
# i = 0 
# while(i<=n):
#      if n%2==0:
#           print(i)
#      i = i+2




# Create a program to find the sum of all numbers from 1 to 100 using a while loop.
# n = int(input("ENTER A NUMBER UPTO WHICH YOU WANT TO SUM : "))
# s = 0
# i= 0
# while(i<=n):
#   s = s+i
#   i=i+1
#   print(i,"==>",s)
# else:
#  print(f"sum of  {n} is {s}")


# n = int(input("ENTER A NUMBER : "))
# for i in range(0,n+1):
#      if i %2==0:
#        print(i)

# n = int(input("ENTER A NUMBER : "))
# i = 0
# while(i<=n):
#      if i%2==0: 
#       print(i)
#      i = i+2


# n = int(input("ENTER A NUMBER : "))
# for i in range(n,-1,-1):
#      if i%2==0:
#           print(i)

# n = int(input("ENTER A NUMBER : "))
# i=n #10
# while(i>=0):
#      if i%2==0:
#           print(i)
#      i=i-1

# n = int(input("ENTER A NUMBER : " ))
# for i in range(n,1,-1):
#      if i%2!=0:
#           print(i)
 
# n = int(input("ENTER A NUMBER : " ))
# i = n
# while(i>=1):
#      if(i%2!=0):
#           print(i)
#      i=i-1

# while(True):
#     n=  int(input("GUESS THE NUMBER "))
     
#      if(n=10):
#         print("YOU GUESS RIGHT NUMBER ")


# import sys
# while(True):
#  number =  int(input("ENTER A NUMBER : " ))
#  if(number==22):
#   print("YOU GUESSED WRITE NUMBBER ")
#   sys.exit()


