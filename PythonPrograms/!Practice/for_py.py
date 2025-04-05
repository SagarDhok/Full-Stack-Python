# Write a Python program to print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#      print(i)

# Create a program to find the sum of all numbers from 1 to 100 using a for loop.
# n = 0
# for i in range(1,101):
#   n= n+i
#   print(f"sum of {i} is {n}")


# word = input("ENTER A WORD : " )
# for ch in range(len(word)):
#      print(word[ch])



# word = "sagar"
# for ch in word[::-1]:
#      print(ch)


# word = "python"
# for i in range(len(word)-1,-1,-1):
#     print("\t{}".format(word[i]))


# n= int(input("ENTER A NUMBER : "))
# s = 0
# ss = 0
# for i in range(0,n+1):
#      print(i)
#      s = s+i
#      ss= s+i*i
# else:
#      print(f"sum = {s}, and square = {ss}")



# n= int(input("ENTER A NUMBER : "))
# s=0 # here s is called Aditive Identity
# ss=0 # here s is called Aditive Identity
# for i in range(1,n+1):
#         print("\t{}\t\t{}".format(i,i*i))
#         s=s+i
#         ss=ss+i*i
# else:
#         print("---------------------------")
#         print("---------------------------")
#         print("\t{}\t\t{}".format(s,ss))

# s=1 # here s is called Multiplicative Identity
# for i in range(1,n+1):
#         print("\t{}".format(i))
#         s=s*i
# else:
#         print("Product={}".format(s))
# #         print("---------------------------")

# s=1
# i = 1
# while(i<=n):
#    print(i)
#    s =s *i
#    i = i+1
# else:
#    print(f"product = {s}")


# #cube

# s=0 # here s is called Aditive Identity
# sc=0 # here s is called Aditive Identity
# for i in range(1,n+1):
#         print("\t{}\t\t{}".format(i,i*i*i))
#         s=s+i
#         sc=sc+i*i*i
# else:
#         print("---------------------------")
#         print("---------------------------")
#         print("\t{}\t\t{}".format(s,sc))
    #---------------------------------------


# s=0
# sc=0
# i=1
# while(i<=n):
#         print("\t{}\t\t\t{}".format(i,i**3))
#         s=s+i
#         sc=sc+i**3
#         i=i+1
# else:
#         print(f"{s},{sc}")

# Sn = n(n+1)/2

# n= int(input("enter a number : "))
# sn = n*(n+1)//2
# print(sn)


#using formula
# n = int(input("Enter a number: "))  # Ensure input is an integer
# sn = n * (n + 1) // 2  # Use integer division to avoid float result
# print(f"The sum of the first {n} natural numbers is: {sn}")



# n= int(input("ENTER A NUMBER : "))
# s = 0
# for i in range(1,101):
#     if i %2 ==0:
#      print(i)
#      s = s+i
# else:
#      print(f"sum = {s}")
     
 

s = 0
i = 1
while(i<=101):
    if i%2 == 0:
     print(i)
     s = s + i
    i= i + 1

else:
    print(f"sum = {s}")



print(f"sum = {s}")  # Print the sum of even numbers



# List Manipulation: Given a list of numbers, use a while loop to remove all elements from the list one by one.
