# lst = [7,2,4,5,8,6]
# for i in range(len(lst)):
#      mv = i
#      for j in range(i+1,len(lst)):
#           if lst[j]<lst[mv]:
#            mv =j
#      lst[i],lst[mv]=lst[mv],lst[i]
 
# print(lst)

# lst = [7,2,4,5,8,6]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j] = lst[j],lst[i]
# print(lst)



# s = "sssssssddddddddkkkkkkk"
# d = {}
# for val in s:
#      if val not in d:
#         d[val]= 1
#      else:
#          d[val]=d[val]+1

# mv = max(d.values())
# for k,v in d.items():
#     if v == mv:
#         print(k,"-",v)
    

# # 72
# def fl(lst):

#  nl = []
#  for i in lst:
#       if type(i)==list:
#            nl.extend(fl(i))
#       else:
#            nl.append(i)
 
#  return nl
 
# lst =  [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# res =fl(lst)
# print(res)

# n = int(input("Enter a number : "))
# if n<=1:
#      print(f"{n} is not a prime number ")
# res = True
# for val in range(2,n):
#      if n%val ==0:
#           res = False
#           break
# if res :
#  print(f"{n} is Prime Number ")
# else:
#  print(f"{n} is Not a Prime Number ")

# n = int(input("Enter a number : "))
# if n<=1:
#  print(f"{n} is not a prime number ")
# else:
#  res  = True
#  i = 2
#  while i<=n//2:
#     if n%i ==0:
#        res  =  False
#     i = i+1
#  if res :
#   print(f"{n} is Prime Number ")
#  else:
#   print(f"{n} is Not a Prime Number ")



#*32 Check if sublist exists in lst
# found = False
# for i in range(len(lst) - len(sublist) + 1):
#     if lst[i:i+len(sublist)] == sublist:
#         found = True
#         break

# print(found)



# lst = [1,2,4,5,1,6,7,8,4,4,5,]
# for val in lst:
#      if lst.count(val)>=2:
#           print(val)
4

# try:
#  ch = int(input("ENter your choice :  "))
#  match(ch):
#       case 1 | "A":
#            print("You have chooosen case 1 or A")
 
#       case 2 | "B":
#            print("You have choosen case 2 or B")
#       case 3 | "C":
#            print("you Have choosen case 3 or 'C' ")
#       case _:
#            print("Your choice of selection is wrong please try again")
# except ValueError:
#      print("Dont ENter alnums symbols , alphabets")


# n = int(input("Enter a number :  "))
# i = 1
# while i<=n:
#      print(i)
#      i = i+1
# else:
#      print("Program execution is done ")

# n = int(input("Enter a number from where you want to genrate number : "))
# while n>0:
#      print(n)
#      n= n-1

# n = int(input("Enter a number : "))
# i = n
# while i>0:
#      print("Val : ",i)
#      i = i-1
# else:
#      print("Program execution is done ")


# n = int(input("Enter a number : "))
# s = 0
# temp_var = n
# while n>0:
#     d = n%10
#     s = s+d
#     n = n//10

# num = int(input("Enter Number Which you want to add  : "))
# p = 1
# temp = num
# while num>0:
#     d = num%10
#     p = p*d
#     num = num//10
# print("Product of {} = {}  ".format(temp,p))


# n = input("enter a number : ")
# x = n.split()
# for i in x[0]:
#      print(i)


# num = int(input("Enter a number :  "))
# count = 0
# while num >0:
#      num = num//10
#      count = count+1
# print(f"Count of given number is : ",count)

