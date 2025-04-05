

# & 1.filter():
# ^ --------------------------------------------------------------------------------------------
# *NORAMAL FUNCTION
# def pos(val):
#      if val>0:
#           return True
#      else:
#           return False

# n = input("ENTER COMMA SEPRATED VALUES : ").split()
# lst = [float(i) for i  in n]   # [10 -2,9,-20,30,40,-5,8]
# obj1 = filter(pos,lst)

# poslst = list(obj1)
# print(poslst)

# #print(obj1)                  #  <filter object at 0x0000026140676050>
# # print(type(obj1))           #  <class 'filter'>

# ^ --------------------------------------------------------------------------------------------
# *ANONYMOUS FUNCTION

# pos = lambda val : val>0

# n = input("ENTER VALUES :").split()
# lst = [float(i) for i in n]
# poslist = list(filter(pos,lst))
# print(poslist)

# ^ --------------------------------------------------------------------------------------------
#! PRINTING POSITIVE AND NEGATIVE VALUES USING FILTER()
# n = input("ENTER SPACE SPACE SEPRATED VALUES : ").split()
# lst = [float(i) for i in n]
# poslist = list(filter(lambda val : val>0,lst))
# neglist = tuple(filter (lambda val: val<0,lst ))
# print("POSTIVE  VALUES  : ", poslist)
# print("NEGATIVE VALUES : ",neglist)

# ^ --------------------------------------------------------------------------------------------
#! ACCEPTING LIST OF VALUES AND FINDING WHETHER IT IS PALINDROM OR NOT USING FILTER()
# n = input("ENTER LIST VALUES SEPRATED BY SPACE : ").split()
# lst = [i for i in n]
# pwords = list(filter(lambda word : word==word[::-1] ,lst))
# print("GIVEN LIST : ",lst)
# print("LIST OF PALINDROM : ",pwords)

# ^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR ACCEPTING LIST OF WORDS AND FIND VOWEL WORDS

# words = input("ENTER LIST VALUE SEPRATED BY SPACE : ").split()
# lst = [i.lower() for i in words]
# vwords = list(filter(lambda word :"a" in word or "e" in word or "i" in word or "o" in word or "u" in word ,lst))
# print("GIVEN LIST : ",lst)
# print("VOWEL WORDS : ",vwords)
# ^ --------------------------------------------------------------------------------------------
#!Program  implementaing the Following
# *Given Line of Text:      S8tRi4@n%GVa&L2uE
# *		Obtaing Alphabets: StRinGValuE
# *		Obtaing Digits: 842
# *		Obtain Special Symbols: @%&

# n  = input("ENTER YOUR LINE OF TEXT :")
# print(n)
# lst = [i for i in n]
# alist = list(filter(lambda val : val.isalpha() ,lst))
# dgtlist = list(filter(lambda val : val.isdigit(),lst))
# spslist = list(filter(lambda val: val.isalnum() and not val.isspace() ,lst))
# print("ALPHABETS: ",alist)
# print("DIGITS : ", dgtlist)
# print("SPECIAL SYMBOLS: ", spslist)

# * IN REVERSE ORDER

# n  = input("ENTER YOUR LINE OF TEXT :")
# print(n)
# lst = [i for i in n]
# alist = list(filter(lambda val : val.isalpha() ,lst))
# print(alist.sort())
# dgtlist = list(filter(lambda val : val.isdigit(),lst))
# print(dgtlist.sort())
# spslist = list(filter(lambda val: not val.isalnum() and not val.isspace() ,lst))
# print(spslist.sort())
# print("ALPHABETS: ",alist)
# print("DIGITS : ", dgtlist)
# print("SPECIAL SYMBOLS: ", spslist)
# ^ --------------------------------------------------------------------------------------------
#! PROGRAM WHICH WILL GET THOSE WORDS WHOSE LENGHT RANGES BETWEEN 3 AND FOUR

# n  = input("ENTER YOUR LINE OF TEXT :").split()
# lst = [i for i in n]
# words = list(filter(lambda val :len(val)<=4 and  len(val)>=3,lst))
# print(words)en

# n  = input("ENTER YOUR LINE OF TEXT :").split()
# lst = [i for i in n]
# words = list(filter(lambda val : 4>=len(val)>=3,lst))
# print(words)
# ^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING THOSE WORDS WHOSE FIRST LETTER AND LAST LETTER IS SAME BUT IT IS NOT PALINDROM

# n = input("ENTER WORDS SEPRATED BY SPACE :  ").split()
# lst= [i for i in n]
# words = list(filter(lambda val: val[0] == val[-1] and val!=val[::-1],lst))
# print(words)

# ^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR PRINTING EVEN AND ODD USING FILTER  FUNTION
# def odval(val):
#      if val%2!=0:
#           return True
#      else:
#           return False

# n = input("ENTER LIST OF VALUES SEPRATED BY COMMAS : ").split()
# lst = [float(i) for i in n]
# evnlst= list(filter(lambda val : val%2==0,lst))
# odlst = list(filter(odval, lst))
# print(evnlst)
# print(odlst)



# ^ --------------------------------------------------------------------------------------------
#* None is funtion and filter false and empyt iterable objects zeros 
# list1=[1,2,False,3,"sagar",{},4,5,6,7,0,0,0,0]
# list2=list(filter(None,list1))
# print(list1)
# print(list2)


# ^ --------------------------------------------------------------------------------------------
# & map function()
# ^ --------------------------------------------------------------------------------------------
# def hike(val):
#      return val +val*50/100

# hike = lambda val : val+val*50/100

# n= input("ENTER LIST OF VALUES SEPRATED BY COMMAS : ").split()
# oldsal= [float(i) for i in n]
# newsal = list(map(hike, oldsal))
# print(oldsal)
# print(newsal)
# print("\toldsal   newsal")
# for k , v in zip(oldsal,newsal):
#      print(f"\t{k}  -> {v}")
# Print(map)   <map object at 0x000001F0BE9F5F30>
# ^ --------------------------------------------------------------------------------------------
# n= input("ENTER LIST OF VALUES SEPRATED BY SPACE : ").split()
# oldsal= [float(i) for i in n]
# newsal = list(map( lambda val : val+val*50/100, oldsal))
# print(oldsal)
# print(newsal)
# print("\toldsal   newsal")
# for k , v in zip(oldsal,newsal):
#      print(f"\t{k}  -> {v}")
# ^ --------------------------------------------------------------------------------------------
#! PROGAM FOR ADDING TWO LIST ELIMENTS
# lst1  = [float(i) for i in input("ENTER LIST OF VALUES : ").split() ]
# lst2  = [float(i) for i in input("ENTER LIST OF VALUES : ").split() ]
# if len(lst2)>len(lst1):
#  for i  in range(len(lst2)-len(lst1)):
#   lst1.append(0)
# elif len(lst1)>len(lst2) :
#  for i in range(len(lst1)-len(lst2)):
#   lst2.append(0)

# listadd = list(map(lambda val1, val2: val1+val2,lst1,lst2))
# for l1, l2 ,l3 in zip(lst1,lst2,listadd):
#      print(l1,l2,"-->",l3)

# ^ --------------------------------------------------------------------------------------------
#! PROGARM FOR FINDING SQUAREROOT
# n = input("ENTER LIST OF VALUES : ").split()
# val = [float(i) for i in n]
# sqrt = list(map(lambda v: v**0.5,val))
# print("VAL  SQUAREROOT ")
# for v,s in zip(val, sqrt ):
#      print(v,s)
# ^ --------------------------------------------------------------------------------------------
#! PROGARM FOR FINDING SQUARE
# n = input("ENTER LIST OF VALUES : ").split()
# val = [float(i) for i in n]
# sqrt = list(map(lambda v: v**2,val))
# print("VAL  SQUARE  ")
# for v,s in zip(val, sqrt ):
#      print(v,s)
# ^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR MULTIPLICATION OF THRREE LIST

# lst1= [float(i) for i in input("ENTER LIST OF VALUES : ").split()]
# lst2= [float(i) for i in input("ENTER LIST OF VALUES : ").split()]
# lst3= [float(i) for i in input("ENTER LIST OF VALUES : ").split()]
# if len(lst2)<len(lst1)>len(lst3):
#      for i in range(len(lst1)-len(lst2)-len(lst3)):
#       lst2.append(1)
#       lst3.append(1)
# elif len(lst1)<len(lst2)>len(lst3):
#      for i in range(len(lst2)-len(lst1)-len(lst3)):
#       lst1.append(1)
#       lst3.append(1)
# elif len(lst1)<len(lst3)>len(lst2):
#      for i in range(len(lst1)-len(lst3)-len(lst2)):
#       lst1.append(1)
#       lst2.append(1)
# mullist = list(map(lambda v1,v2 ,v3 : v1*v2*v3,lst1,lst2,lst3))
# print(mullist)
# ^ --------------------------------------------------------------------------------------------
# lst1= [i for i in input("ENTER LIST OF VALUES : ").split()]
# lst2= [i for i in input("ENTER LIST OF VALUES : ").split()]
# lst3 = list(map(lambda val1,val2:val1+"-"+val2,lst1,lst2))
# print(lst3)
# ^ --------------------------------------------------------------------------------------------

# & MAP CAN ACCEPTS TWO OR MORE ARGUMENTS AT ONCE BUT FILTER CAN'T
# ^ --------------------------------------------------------------------------------------------
#!  GIVING 10% HIKE TO THE DICT VALUES :
# olddict = {}
# while True:
#     key = input("ENTER EMP NAME : ")
#     val = int(input("ENTER EMP SALARY  : "))
#     olddict[key] = val

#     ch = input("Do you want to insert another entry - (yes / no ) : ")
#     if ch.lower() == "no":
#         break
#     elif ch.lower() not in ["yes", "no"]:
#         print("INVALID INPUT PLEASE ENTER VALID INPUT ! ")
#         while True:
#             ch = input("Do you want to insert another entry - (yes / no ) : ")
#             if ch.lower() == "yes":
#                 break
#             elif ch.lower() == "no":
#                 break
#             elif ch.lower() not in ["yes", "no"]:
#                 print("INVALID INPUT PLEASE ENTER VALID INPUT ! ")

# print(f"Old salary of emp : {olddict} ")
# print("EMP \t OLD SALARY ")
# for k, v in olddict.items():
#     print(f"{k}  {v}")

# modict = list(map(lambda k: olddict[k]+olddict[k]*50/100, olddict))
# for k, v in zip(olddict, modict):
#     olddict[k] = v

# print(f"Modified salary after giving hike : {olddict} ")
# print("EMP \t NEW SALARY ")
# for k, v in olddict.items():
#     print(f"{k}  {v}")
# ^ --------------------------------------------------------------------------------------------
#* modify or updates the values  # satish gupta
# names=["My","name","is","anthony gunjalwish"]
# names1=list(map(str.upper,names))
# print(names)
# print(names1)


# list1=["10","20","30","40"]
# list2=list(map(int,list1))
# print(list1)
# print(list2)



# ^ --------------------------------------------------------------------------------------------
#& reduce
# ^ --------------------------------------------------------------------------------------------
#! Salary progarm 

# import functools
# sals = [int(sal) for sal in input("Enter salaries : ").split() if int(sal) in range(0,1001) ]
# print("Given salary : ")
# print(sals)
# print("---------------------------------------------------")
# #*Filter the sal ranges between 0 to 500
# sal0_500 = list(filter(lambda sal : sal in range(0,501),sals))

# #* Filter the sal ranges between  501 to 1000
# sal501_1000 = list(filter(lambda sal  :sal in range(501,1001),sals))

# #*Give Hike 10% to those emp whose sal ranges from 0 to 500
# hike0_500 = list(map(lambda sal: sal+sal*10/100,sals))
# #*Give Hike 20% to those emp whose sal ranges from 501 to 1000
# hike501_1000 = list(map(lambda sal:sal+sal*20,sals))

# #*Find the total sal of those emp whose sal ranges between 0 to 500 before and after hike
# totalsal0_500 = functools.reduce(lambda a,b:a+b,sal0_500)
# totalhikesal0_500  = functools.reduce(lambda a,b:a+b,hike0_500)

# #*Find the total sal of those emp whose sal ranges between 501 to 1000 before and after hike
# totalsal501_1000 = functools.reduce(lambda x,y: x+y,sal501_1000)
# totalhikesal501_1000 = functools.reduce(lambda x,y: x+y,hike501_1000)

# print("="*50)
# print("Sal0-500\t\tHike0-500")
# print("-"*50)
# for ol,nl in zip(sal0_500,hike0_500):
#     print("\t{}\t\t{}".format(ol,nl))
# print("*"*40)
# print("\t{}\t\t{}".format(totalsal0_500,totalhikesal0_500))
# print("-"*50)
# print("Sal501-1000\t\tHike501-1000")
# print("-"*50)
# for ol,nl in zip(sal501_1000,hike501_1000):
#     print("\t{}\t\t{}".format(ol,nl))
# print("*"*40)
# print("\t{}\t\t{}".format(totalsal501_1000,totalhikesal501_1000))
# print("-"*50)
# GTSal0_1000=totalsal0_500+totalsal501_1000
# GTHikesal0_1000=totalhikesal0_500+totalhikesal501_1000
# print("\t{}\t\t{}".format(GTSal0_1000,GTHikesal0_1000))
# print("="*50)
# ^ --------------------------------------------------------------------------------------------
#! sum of list valuse through reduce funtion

# def sumop(a,b):
#      return a+b

# import functools
# lst = [10,20,30,40,50]
# sm = functools.reduce(sumop,lst)
# print(sm)

# ^ --------------------------------------------------------------------------------------------
#! Finding minimux and maximum value through reduce funtion
# import functools
# lst = [10,20,30,40,50]
# sm = functools.reduce(lambda a,b:a+b,lst)
# print(sm)

# import functools
# def maxval(a,b):
#      if a>b:
#        return a
#      else:
#       return b


# lst = [int(i) for i in input("Enter values septated by commas : ").split()]
# mx = functools.reduce(maxval,lst)
# mn = functools.reduce(lambda a,b:a if a<b else b  ,lst)
# print(f"Max : {lst} = {mx}")
# print(f"Min : {lst} = {mn}")

# ^ --------------------------------------------------------------------------------------------
#! PRINTING A LINE OF TEXT THROUGH REDUCE FUNTION WITHOUT JOIN
# import functools
# lst = [word for word in input("Enter a line of text : ").split(",")]
# line = functools.reduce(lambda k,v:k+v,lst)
# print("Line : ",line)

# ^ --------------------------------------------------------------------------------------------

# list1=[1,2,3,-1,-3,-4,-5,4,5,-6,-7,6,7,8,-10]
# a=filter(lambda num:num>0,list1)
# for value in a:
#  print(value,end=" ")
# print()
# b=filter(lambda num:num<0,list1)
# for value in b:
#  print(value,end=" ")

#  grade_list=[["Naresh","A"],
# ["Ramesh","B"],
# ["Sures","C"],
# ["Paa","K"],
# ["Ganesh","D"]]

# grade_listA=list(filter(lambda a:a[1]=="A",grade_list))
# grade_listB=list(filter(lambda a:a[1]=="B",grade_list))
# grade_listC=list(filter(lambda a:a[1]=="C",grade_list))
# print(grade_listA)
# print(grade_listB)
# print(grade_listC)
# ^ --------------------------------------------------------------------------------------------
#*satish gupta
# import functools
# list1=[10,20,30,40,50]
# b=functools.reduce(lambda x,y:x+y,list1,100)
# print(b)
# c=functools.reduce(lambda x,y:str(x)+str(y),list1)
# print(c)

