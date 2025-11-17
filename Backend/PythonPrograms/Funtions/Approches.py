

#?  =============================================================================================
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
# def sub(a,b):
#      c = a-b
#      return c
# x = int(input("ENTER FIRST VALUE: "))
# y = int(input("ENTER SECOND VALUE : "))
# z = sub(x,y) 
# print(f"({x},{y})={z}")  
# print(x)
# print(y)
# print(z)
# print(f"({z[0]},{z[1]}) = {z[2]}")     if return a,b,c
    
#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER 
# def sub():
#      a = float(input("ENTER FIRST VALUE : "))
#      b = float(input("ENTER SECOND VALUE : "))
#      c= a-b
#      print(c)
# sub()  

#* APPROACH-3
#* FUNCTION  NO RETURN TYPE AND WITH PARAMETER
# def sub(a,b):
#      c = a-b
#      print(f"({a},{b})={c}")

# x= int(input("ENTER FIRST VALUE : "))
# y = int(input("ENTER SECOND VALUE : "))
# z = sub(x,y)


#* APPROACH-4
#* FUNCTION WITH RETURN TYPE  NO PARAMETER 
#* LOGIC-1
# def sub():     
#    x = int(input("ENTER FIRST VALUE :"))
#    y = int(input("ENTER FIRST VALUE :"))
#    z = x-y
#    return x,y,z
# a,b,c = sub()
# print(f"({a},{b})={c}")


#* LOGIC-2
# def sub():     
#    x = int(input("ENTER FIRST VALUE :"))
#    y = int(input("ENTER FIRST VALUE :"))
#    z = x-y
#    return x,y,z
# res = sub()
# print(res)
# print(f"({res[0]},{res[1]})= {res[2]}") 
##OR 
# print(f"({res[-3]},{res[-2]})= {res[-1]}")    
#?  =============================================================================================
#! PROGRM FOR CALCULATING SIMPLE INTEREST AND TOTAL AMOUNT TO PAY
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
#* The simple interest formula is:  SI = P × R × T
#* Total Amount to Pay Formula : A = P + SI
# def simpleint(p,r,t):
#      if p<0 or r<0 or t<0:
#       print("it is invalid input")
#      #  return None, None
#      else:
#        si = p*r*t/100
#        totlamt = p+si
#        return si,totlamt

# p = float(input("ENTER PRINCIPLE AMOUNT : "))
# r = float(input("ENTER RATE OF INTEREST : "))
# t = float(input("ENTER TIME : "))
# si,totlamt =  simpleint(p,r,t)
# # if si is not None and totlamt is not None:
   
#    print(f"SIMPLE INTERST IS {si}")
#    print(f"TOTAL AMOUNT TO PAY IS  {totlamt}")

#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER 
# def simpleint():
#      p = float(input("ENTER PRINCIPLE AMOUNT : "))
#      r = float(input("ENTER RATE OF INTEREST : "))
#      t = float(input("ENTER TIME : "))
#      si = p*r*t/100
#      totlamt = p+si
#      print(f"SIMPLE INTERST IS {si}")
#      print(f"TOTAL AMOUNT TO PAY IS  {totlamt}")

# simpleint()

#* APPROACH-3                                    
#* FUNCTION  NO RETURN TYPE AND WITH PARAMETER
# def simpleint(p,t,r):
#     if(p<0) or (t<0) or (r<0):
#         print("Invalid Input(s)--Try again")
#     else:
#         si=(p*t*r)/100
#         totamt=p+si
#         print("="*50)
#         print("Simple Interest={}".format(si))
#         print("Total Amount to Pay={}".format(totamt))
#         print("=" * 50)
# #Main Program
# p=float(input("Enter Principle Amount:"))
# t=float(input("Enter Time:"))
# r=float(input("Enter Rate of Interest:"))
# simpleint(p,t,r) # Function Call

#* APPROACH-4
#* FUNCTION WITH RETURN TYPE  NO PARAMETER 
# def simpleint():
#      p=float(input("Enter Principle Amount:"))
#      t=float(input("Enter Time:"))
#      r=float(input("Enter Rate of Interest:"))
#      if(p<0) or (t<0) or (r<0):
#         print("Invalid Input(s)--Try again")
#         return None, None
#      else:
#       si = p*r*t/100
#       totlamt = p+si
#       return si,totlamt
     
# si,totlamt = simpleint()
# if si is not None and totlamt is not None:
#  print(f"SIMPLE INTERST IS {si}")
#  print(f"TOTAL AMOUNT TO PAY IS  {totlamt}")


#?  =============================================================================================
#! PROGRAM FOR CALCULATING AREA AND PERIMETER OF SQUARE
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
#* FORMULA FOR AREA OF SQUARE : sides**2
#* FORMULA FOR PERIMETER OF SQUARE : 4*sides
# def area_square(side):
#           sa = side**2
#           return sa
# def perimeter_square(side):
#          sp = side*4       
#          return sp

# side = float(input("ENTER SIDE OF SQUARE : "))
# sa = area_square(side)
# print(f"AREA OF SQUARE IS {sa}")

# side = float(input("ENTER SIDE OF SQUARE : "))
# ps = perimeter_square(side)
# print(f"PERIMETER OF SQUARE IS {ps}")


#* APPROACH-2
# # *#& NO RETURN TYPE AND NO PARAMETER 
# def squarearea():
#     s=float(input("Enter Value of Side for Cal Area of Square:"))
#     sa=s**2
#     print("Area of Square={}".format(sa))

# def squareperi():
#     s = float(input("Enter Value of Side for Cal Perimeter of Square:"))
#     ps = 4*s
#     print("Perimeter of Square={}".format(ps))

# #Main Program
# squareperi()
# squarearea()

#* APPROACH-3
#* FUNCTION  NO RETURN TYPE AND WITH PARAMETER
# def area_square(side):
#      sa = side**2
#      print(sa)
#      print(f"AREA OF SQUARE {sa}")

# def perimeter_square(side):
#      ps = side*4
#      print(f"PERIMETER OF SQUARE {ps}")

# side = float(input("ENTER SIDE OF SQUARE : "))
# sa = area_square(side)
# side = float(input("ENTER SIDE OF SQUARE : "))
# sa = perimeter_square(side)

#* APPROACH-4
#* FUNCTION WITH RETURN TYPE  NO PARAMETER 
# def area_square():
#      side = float(input("ENTER SIDE OF SQUARE : "))
#      sa = side**2
#      return sa     
# def perimeter_square():
#      side = float(input("ENTER SIDE OF SQUARE :"))
#      ps = side *4
#      return ps

# sa = area_square()
# print(sa)
# ps = perimeter_square()
# print(ps)
#?  =============================================================================================
#! PROGRAM FOR CALCULATING AREA OF RECTANGLE USING FUNCTION 
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
#*AREA OF RECTANGLE = LENGTH * BREADTH 
# def area_rectagle(length,breadth):
#          ar = length*breadth
#          return ar

# length = float(input("ENTER LENGHT OF RECTANGLE : "))
# breadth = float(input("ENTER BREADTH OF RECTANGLE : "))
# ar = area_rectagle(length,breadth)
# print(f"AREA OF RECTANGEL IS {ar}")

#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER 
# def area_rectangle():
#      length = float(input("ENTER LENGHT OF RECTANGLE : "))
#      breadth = float(input("ENTER BREADTH OF RECTANGLE : "))
#      ar = length*breadth
#      print("area of rectangle",ar)
# area_rectangle()

#* APPROACH-3
#* FUNCTION  NO RETURN TYPE AND WITH PARAMETER
# def area_rectangle(length,breadth):
#      ar = length*breadth
#      print("area of rectangle",ar)

# length = float(input("enter lenght of rectangle : "))
# breadth = float(input("enter breadth of rectangle : "))
# area_rectangle(length,breadth)


#* APPROACH-4
#* FUNCTION  WITH RETURN TYPE AND NO PARAMETER
# def area_square():
#      ln= float(input("enter length of rectangle "))
#      b= float(input("enter length of breadth "))
#      ar = ln*b
#      return ar

# ar = area_square()
# print(ar)
#?  =============================================================================================
#! PROGRAM FOR CALCULATING AREA OF CIRCLE WITH FUNCTIONS
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
#* AREA OF CIRCLE = 3.14*r*r
# def  area_circle(r):
#       ac = 3.14*r*r
#       return ac
# r = float(input("ENTER RADIUS OF CIRCLE : "))
# ac = area_circle(r)
# print("area circle ",ac)

#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER 
# def area_circle():
#      r = float(input("enter radius of circle : "))
#      ac = 3.14*r*r
#      print("area of circle ",ac)
# area_circle()

#* APPROACH-3
#* FUNCTION  NO RETURN TYPE AND WITH PARAMETER
# def area_circle(r):
#      ac = 3.14*r*r
#      print("area of circle",ac)
# r = float(input("enter radius of circle : "))
# ac = area_circle(r)

#* APPROACH-4
#* FUNCTION  WITH RETURN TYPE AND NO PARAMETER
# def area_circle():
#      r = float(input("enter radius of circle : "))
#      ac = 3.14*r*r
#      return ac 
# ac= area_circle()
# print(ac)
#?  =============================================================================================
#! PROGRAM FOR CALCULATING AREA AND PERIMETER OF TRIANGLE
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
#* FORMULA FOR AREA OF TRIANGLE : 1/2*base*height
#* FORMULA FOR PERIMETER OF TRIANG : Perimeter=a+b+c
# def area_triangle(b,h):
#            at= 1/2*b*h
#            return at
# def perimeter_triangle(a,b,c):
#         pt = a+b+c
#         return pt

# b = float(input("ENTER BASE OF TRIANGLE : "))
# h= float(input("ENTER HEIGHT OF TRIANGLE : "))
# at = area_triangle(b,h)
# print("area of triangle",at)
# a = float(input("ENTER FIRST SIDE1 OF TRIANGLE  : "))
# b = float(input("ENTER FIRST SIDE2 OF TRIANGLE  : "))
# c = float(input("ENTER FIRST SIDE3 OF TRIANGLE  : "))
# pt = perimeter_triangle(a,b,c)
# print("perimeter of tringel  ",pt)


#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER 
# def area_triangle():
#       b = float(input("ENTER BASE OF TRIANGLE : "))
#       h= float(input("ENTER HEIGHT OF TRIANGLE : "))
#       at= 1/2*b*h
#       print("area of triangle",at)


# def perimeter_triangle():
#    a = float(input("ENTER FIRST SIDE1 OF TRIANGLE  : "))
#    b = float(input("ENTER FIRST SIDE2 OF TRIANGLE  : "))
#    c = float(input("ENTER FIRST SIDE3 OF TRIANGLE  : "))
#    pt = a+b+c
#    print("perimeter of tringel  ",pt)

# area_triangle()
# perimeter_triangle()


#* APPROACH-3
#* FUNCTION NO RETURN TYPE AND WITH PARAMETER
# def area_triangle(b,h):
#       at= 1/2*b*h
#       print("area of triangle",at)
# def perimeter_triangle(a,b,c):
#       pt = a+b+c
#       print("perimeter of tringel  ",pt)

# b = float(input("ENTER BASE OF TRIANGLE : "))
# h= float(input("ENTER HEIGHT OF TRIANGLE : "))
# at = area_triangle(b,h)
# a = float(input("ENTER FIRST SIDE1 OF TRIANGLE  : "))
# b = float(input("ENTER FIRST SIDE2 OF TRIANGLE  : "))
# c = float(input("ENTER FIRST SIDE3 OF TRIANGLE  : "))
# pt = perimeter_triangle(a,b,c)

#* APPROACH-4
#* FUNCTION WITH RETURN TYPE NO WITH PARAMETER
# def area_triangle():
#       b = float(input("ENTER BASE OF TRIANGLE : "))
#       h= float(input("ENTER HEIGHT OF TRIANGLE : "))
#       at= 1/2*b*h
#       return at
# def perimeter_triangle():
#       a = float(input("ENTER FIRST SIDE1 OF TRIANGLE  : "))
#       b = float(input("ENTER FIRST SIDE2 OF TRIANGLE  : "))
#       c = float(input("ENTER FIRST SIDE3 OF TRIANGLE  : "))
#       pt = a+b+c
#       return pt
     
# at = area_triangle()
# print("area of traingle ",at)
# pt = perimeter_triangle()
# print("perimeter of triangle",pt)
#?  =============================================================================================
#! PROGRAM WHICH WILL ACCEPT WORD AND FIND IT IS PALINDROM OR NOT
#* APPROACH-1 
#* WITH RETURN TYPE AND WITH PARAMETER  
# def pal(word):
#      if word == word[::-1]:
#             return "It is palindrome"
#      else:
#          return  "Is is not palindrome"

# word = input("ENTER A WORD : ")
# res = pal(word)
# print(res)

#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER
# def pal():
#      word = input("ENTER A WORD : ")
#      if word == word[::-1]:
#              print("It is palindrome")
#      else:
#           print("Is is not palindrome")
# pal()

#* APPROACH-3
#* FUNCTION NO RETURN TYPE AND WITH PARAMETER
# def pal(word):
#      if word == word[::-1]:
#           print("it is palindrome")
#      else:
#           print("it is not palindrome")

# word = input("enter a word : ")
# pal(word)

#* APPROACH-4
#* FUNCTION WITH RETURN TYPE NO WITH PARAMETER
# def pal():
#      word = input("enter a word : ")
#      if word == word[::-1]:
#           return "it is palindrome"
#      else:
#           return "it is not palindrome"
# res = pal()
# print(res)
#?  =============================================================================================
#! PROGRAM FOR FINDING SUM AND AVERAGE OF LIST VALUES TAKING FROM USER USING FUNCTIONS
#* APPROACH-1
#* WITH RETURN TYPE AND WITH PARAMETER
# def sum(lst):
#     s = 0
#     for val in lst:
#       s = s+val
#     else:
#       return s
# def avg(s, lst):
#     avg = s/len(lst)
#     return avg
# n = int(input("enter how many numbers you want to enter : "))
# if n <= 0:
#     print("INVALID INPUT ! PLEASE ENTER AGAIN ")
# else:
#     lst = [] 
#     for i in range(1, n+1):
#               v = int(input(f"ENTER {i} VALUES : "))
#               lst.append(v)
                
#               s = sum(lst)
#               avg = avg(s, lst)
#               print("SUM = ", s)
#               print("AVG = ", avg)
                
#* APPROACH-2
# *#& NO RETURN TYPE AND NO PARAMETER
# def findsumavg():
#     n=int(input("Enter How Many Values u want to Enter:"))
#     if(n<=0):
#         print("{} is Invalid Input".format(n))
#     else:
#         lst=[]
#         for i in range(1,n+1):
#             value=float(input("Enter {} Value:".format(i)))
#             lst.append(value)
#         else:
#             print("-------------------------------")
#             print("\nList of Values:")
#             print(lst) 
#             s=0
#             for val in lst:
#                 s=s+val
#             else:
#                 print("Sum={}".format(s))
#                 print("Avg={}".format(s/len(lst)))
#                 print("-------------------------------")
# findsumavg() 

#* APPROACH-3
#* FUNCTION NO RETURN TYPE AND WITH PARAMETER
# def lst_sum(lst):
#      s = 0
#      for val in lst:
#        s= s+val
#      else:
#        print(s)
#      a = s / len(lst)
#      print(a)
# n = int(input("ENTER HOW MANY VALUES YOU WANT TO ENTER : "))
# if n<=0:
#      print("INVALID INPUT ")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = int(input(f"ENTER {i} VALUE :"))
#           lst.append(val)
#      s =  lst_sum(lst)

#* APPROACH-4
#* FUNCTION WITH RETURN TYPE NO WITH PARAMETER
# def findsumavg():
#     n=int(input("Enter How Many Values u want to Enter:"))
#     if(n<=0):
#         return("{} is Invalid Input".format(n))
#     else:
#         lst=[]
#         for i in range(1,n+1):
#             value=float(input("Enter {} Value:".format(i)))
#             lst.append(value)
#         else:
#             s=0
#             for val in lst:
#                 s=s+val
#             else:
#                 return lst,s,s/len(lst)
# res=findsumavg() # Function call returns either str type or tuple type
# if type(res) is str:
#     print(res)
# else:
#     print("List of Values:{}".format(res[0]))
#     print("Sum={}".format(res[1]))
#     print("Avg={}".format(res[2]))
#?  =============================================================================================
#!Program for Finding Length of each word and also find Highest length word
#* APPROACH-1
#* WITH RETURN TYPE AND WITH PARAMETER
# def read_values(lst):
#       return lst   
# def len_word(lst):
#      dict ={}
#      for j in lst:
#           dict[j] = len(j)
#      return dict
# def min_lenword(dict):
#      mv = max(dict.values())
#      for keys,value in dict.items():
#           if value == mv:
#            print(keys,value)

# n = int(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER : "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN ")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = input(f"ENTER {i} VALUE ")
#           lst.append(val)

#      lst_res = read_values(lst) 
#      dict_res = len_word(lst_res)
#      min_lenword(dict_res)

#* APPROACH-2
#* NO RETURN TYPE AND NO PARAMETER
# lst =  []
# dict = {}
# def readvalues():
#      n = int(input("enter how many number you want to enter "))
#      if n<=0:
#           print("invalid input ! enter again ")
#      else:
#           for i in range(1,n+1):
#                val = input(f"enter {i} value : ")
#                lst.append(val)

#      # print(lst)
# def len_word(lst):
#      for j in lst:
#       dict[j]= len(j)
#      print(dict)

# def min_lenword(dict):
#     mv = max(dict.values())
#     for k,v in dict.items():
#       if v == mv:
#           print(k,v)

# readvalues()
# len_word(lst)
# min_lenword(dict)
          
     
#* APPROACH_
#Program for Finding Length of each word and also find Highest length word
#WordsLengthFunEx1.py
# def readvalues():
#     nov=int(input("Enter How Many Words u have:"))
#     if(nov<=0):
#         return ("{} is invalid input".format(nov))
#     else:
#         lst=[]
#         for i in range(1,nov+1):
#             word=input("Enter {} Word:".format(i))
#             lst.append(word)
#         else:
#              return lst

# def findlengthwords(lst): 
#     wordlen=dict() 
#     for j in lst:
#         wordlen[j]=len(j)
#     else:
#      return wordlen

# def minlengthword(wordlen):
    
#     mv=max(wordlen.values()) 
#     for key,value in wordlen.items():
#         if(value==mv):
#             print(f"{key} {value}")
# lst=readvalues()    
# if (type(lst) is str):
#     print(lst)
# else:
#     wordlen=findlengthwords(lst) # Function call sending list of lst
#     minlengthword(wordlen) # Function call sending Dict Object
#?  =============================================================================================
#!Program for Finding Length of each word and also find least length word
#* APPROACH-1
#* WITH RETURN TYPE AND WITH PARAMETER
# def read_values(lst):
#       return lst   
# def len_word(lst):
#      dict ={}
#      for j in lst:
#           dict[j] = len(j)
#      return dict
# def min_lenword(dict):
#      mv = min(dict.values())
#      for keys,value in dict.items():
#           if value == mv:
#            print(keys,value)

# n = int(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER : "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN ")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = input(f"ENTER {i} VALUE ")
#           lst.append(val)

#      lst_res = read_values(lst) 
#      dict_res = len_word(lst_res)
#      min_lenword(dict_res)

#* APPROACH-2
#* NO RETURN TYPE AND NO PARAMETER
# lst =  []
# dict = {}
# def readvalues():
#      n = int(input("enter how many number you want to enter "))
#      if n<=0:
#           print("invalid input ! enter again ")
#      else:
#           for i in range(1,n+1):
#                val = input(f"enter {i} value : ")
#                lst.append(val)

#      # print(lst)
# def len_word(lst):
#      for j in lst:
#       dict[j]= len(j)
#      print(dict)

# def min_lenword(dict):
#     mv = min(dict.values())
#     for k,v in dict.items():
#       if v == mv:
#           print(k,v)

# readvalues()
# len_word(lst)
# min_lenword(dict)
          
     
#* APPROACH_
# def readvalues():
#     nov=int(input("Enter How Many Words u have:"))
#     if(nov<=0):
#         return ("{} is invalid input".format(nov))
#     else:
#         lst=[]
#         for i in range(1,nov+1):
#             word=input("Enter {} Word:".format(i))
#             lst.append(word)
#         else:
#              return lst

# def findlengthwords(lst): 
#     wordlen=dict() 
#     for j in lst:
#         wordlen[j]=len(j)
#     else:
#      return wordlen

# def minlengthword(wordlen):
    
#     mv=min(wordlen.values()) 
#     for key,value in wordlen.items():
#         if(value==mv):
#             print(f"{key} {value}")
# lst=readvalues()    
# if (type(lst) is str):
#     print(lst)
# else:
#     wordlen=findlengthwords(lst) # Function call sending list of lst
#     minlengthword(wordlen) # Function call sending Dict Object
#?  =============================================================================================
#! PROGRAM FOR REVERSING WORD AT SAME PLACE
# def reverseWords(s):
#     x= s.split()
#     lst = []
#     for i in x:
#          lst.append(i[::-1])
    
#     s = " ".join(lst)
#     return s

# n = input("enter a line of text : ")
# s = reverseWords(n)
# print(s)
#?  ============================================================================================
#!PROGRAM FOR DECIDING GIVEN VALUE IS MAGIC NUMBER OR NOT
# def magic_no(n):
#   square = n*n
#   sn = str(n)
#   ssquare = str(square)
#   if ssquare.endswith(sn):
#       return (f"{n} = {square}  it is magic number")
#   else:
#       return (f"{n} = {square}  it is not magic number")

# n = int(input("enter a value : "))
# res = magic_no(n)
# print(res)


#?  ============================================================================================
#! Program for calculating Roots of Quadratic Equation
# a = int(input("Enter value of a : "))
# b = int(input("Enter value of b : "))
# c = int(input("Enter value of c : "))
# if a==0:
#      print("It is invalid input")
# else:
#      D= b**2+4*a*c
#      if D>0:
#           print("Roots are Real and Distinct ")
#           r1=(-b+D**0.5)/(2*a)          #*Formula
#           r2=(-b-D**0.5)/(2*a)          #*Formula
#           print(f"Root 1 : {r1}")
#           print(f"Root 2 : {r2}")
#      elif D==0:
#           print("Roots are Real and Equal ")
#           r1 = -b  / (2 * a)          #*Formula
#           r2 = -b  / (2 * a)          #*Formula
#           print(f"Root 1 : {r1}")
#           print(f"Root 2 : {r2}")
#      else:
#           print("Roots are Real and Imaginary")
#           r1=(-b+D**0.5)/(2*a)          #*Formula
#           r2=(-b-D**0.5)/(2*a)          #*Formula
#           print(f"Root 1 : {r1}")
#           print(f"Root 2 : {r2}")


    