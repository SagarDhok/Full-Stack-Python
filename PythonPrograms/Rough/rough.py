# n = int(input("Enter a number : "))
# i = 0
# while i<=n:
#    print(i)
#    i = i+1


# n = int(input("Enter a number : "))
# i = n
# while i >=0:
#    print(i)
#    i = i-1

# n = int(input("Enter a number upto you want : "))
# i = 1
# while i<=n:
#      if i %2==0:
#           print(i)
#      i= i+1

# n = int(input("Enter a number upto you want : "))
# i = 1
# while i<=n:
#      if i %2!=0:
#           print(i)
#      i= i+1

# n = int(input("Enter a number from where you want : "))
# i = n
# while i>=0:
#      if i%2==0:
#           print(i)
#      i = i-1

# n = int(input("Enter a number from where you want : "))
# i = n
# while i>=0:
#      if i%2!=0:
#           print(i)
#      i = i-1

# n = int(input("Enter a number from where you want : "))
# i = 0
# s = 0
# while i<=n:
#      print(i)
#      s = s+i
#      i = i+1
# print("sum =",s)

# n = int(input("Enter a number from where you want : "))
# i = 1
# s = 1
# while i<=n:
#      print(i)
#      s = s*i
#      i = i+1
# print("multiplication =",s)


# n = int(input("Enter a number upto where you want to genrate : "))
# for i in range(2,n+1):
#      for j in range(1,11):
#           print(f" {i} X {j} = {i*j}")
#      print()


# n = int(input("Enter a number upto where you want to genrate :"))
# if n < 2:
#      print(f"{n} is not a prime number ")
# for i in range(2,n+1):
#      res = True
#      for j in range(2,i//2+1):
#           if i%j == 0:
#                res = False
#                break
#      if res:
#          print(f"{i} is Prime Number  ")
#      else:
#           print(f"{i} is not a prime Number ")


# n = int(input("Enter a number : "))
# res = True
# for i in range(2,n):
#      if n%i == 0:
#           res = False
#           break
# if res:
#          print(f"{i} is Prime Number  ")
# else:
#           print(f"{i} is not a prime Number ")

# n = int(input("Enter a number upto you want to genrate prime numbers : "))
# if n < 2:
#     print(f"{n} is not a Prime Number ")
# else:
#     i = 2
#     while i <= n:
#         j = 2
#         res = True
#         while j <= i // 2:
#             if i % j == 0:
#                 res = False
#                 break
#             j = j + 1

#         if res:
#             print(f"{i} is Prime Number ")
#         else:
#             print(f"{i} is not Prime Number ")
#         i = i + 1


# n = int(input("Enter number upto where you want to genrate : "))
# if n <2:
#      print(f"{n} is Prime Number : ")
# else:
#      i = 2
#      while i<=n:
#           j = 2
#           res = True
#           while j<=i//2:
#            if i%j== 0:
#                res = False
#                break
#            j = j+1
#           if res :
#              print(f"{i} is Prime Number ")
#           else:
#              print(f"{i} is Not Prime Number ")
#           i = i+1


# n = input("Enter a lIne of text :")
# x = n.split()
# for i in x:
#    print(i)
#    for j in i:
#       print(j)


# while True:
#  n = input("Enter a number : ")
#  if int(n) in range(100,201) and n.isdigit():
#        break
#  else:
#   print("Please enter valid input")
# print(n)

# while True:
#  n = input("Enter a student name : ")
#  x = n.split()
#  res = True
#  for i in x:
#       if not i.isalpha():
#        res = False
#  if res :
#       break
#  else:
#      print("Please enter valid input")
# print(n)


# dict = {}
# for val in list:
#      dict[val]=len(val)
# print(dict)


# def readvalues():
#      n = int(input("Enter how many numbers do you want to enter : "))
#      if n<=0:
#           return ("It is invalid input ")
#      else:
#           lst = []
#           for i in  range(1,n+1):
#             val = input(f"Enter {i} value : ")
#             lst.append(val)
#      return lst
# def wordlen(lst):
#  dict = {}
#  for val in lst:
#      dict[val]=len(val)
#      return dict

# def highestlen(dict):
#  mv = max(dict.values())
#  for k,v in dict.items():
#      if v == mv:
#           print(k,"->",v)


# lst= readvalues()
# if type(lst)==str:
#      print(lst)
# else:
#  wl = wordlen(lst)
#  highestlen(wl)


# def readvalues():
#     n = int(input("Enter how many numbers do you want to enter : "))
#     if n <= 0:
#         print("It is invalid input ")
#     else:
#         lst = []
#         for i in range(1, n + 1):
#             val = input(f"Enter {i} value : ")
#             lst.append(val)
#         print("you have entere : ", lst)


# def wordlen(readvalues):
#     dict = {}
#     for val in readvalues():
#         dict[val] = len(val)
#         return dict


# def highestlen(wordlen):
#     mv = max(wordlen.values())
#     for k, v in wordlen.items():
#         if v == mv:
#             print(k, "->", v)
# readvalues()
# wordlen()
# highestlen()


# n = input("Enter a line of text ")
# x = n.split()
# lst = []
# for i in x:
#      lst.append(i[::-1])
# print(" ".join(lst))


# def decideprime(val):
#      if val <=1:
#           res = False
#      else :
#           res = True
#           for i in range(2,val):
#                if val%i==0:
#                     res = False
#                     break
#      return res
# lst = [int(i) for i in input("Enter values seprated by space : ").split()]
# dict = {val:"Prime" if decideprime(val) else "Not Prime" for val in lst}
# for k,v in dict.items():
#      print(f"{k}-->{v}")

# addop = lambda a,b :a+b
# res =addop{10,20)
# print(}es)
# print(type(addop))


# print("""

#         1.Addition
#         2.Substraction
#         3.multiplication
#         4.division
#         5.floordivion
#         6.ModuloDivision
#         7.Exponention

#         8.Exit
# """)
# sumop = lambda a,b : a+b
# subop= lambda a,b : a-b
# mulop = lambda a,b:a*b
# division = lambda a,b:a/b
# floordv = lambda a,b:a//b
# modulodv = lambda a,b:a%b
# expon = lambda a,b : a**b

# while True:
#  ch = int(input("Enter your choice : "))
#  match(ch):
#       case 1 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = sumop(a,b)
#            print(f"sum : {res}")
#       case 2 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = subop(a,b)
#            print(f"sub : {res}")
#       case 3 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = mulop(a,b)
#            print(f"multiplication : {res}")
#       case 4 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = division(a,b)
#            print(f"division : {res}")
#       case 5 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = floordv(a,b)
#            print(f"floordiv : {res}")
#       case 6 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = modulodv(a,b)
#            print(f"modulo division : {res}")
#       case 7 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = expon(a,b)
#            print(f"Exponention : {res}")
#       case 8 :
#               print("Thanks for using this progrm ")
#               break
#       case _ :
#              print("Invalid input please enter valid input ")


# biggest = lambda a,b,c : a if b<=a>c else b if a<b>=c else c if a<=c>b else "All values are same"
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# c = int(input("Enter third value : "))
# res = biggest(a,b,c)
# print(res)


# bigv =lambda a,b : a if a>b else b if b>a else " Both Values are same "
# smlv = lambda a,b : a if a<b else b if b<a else "Both values are same "

# a =int(input("Enter first value : "))
# b = int(input("Enter Second Value : "))
# res_bigv = bigv(a,b)
# res_smlv = smlv(a,b)
# print(f"biggest value : {res_bigv}")
# print(f"smallest value  : {res_smlv}")


# def sgrmax(lst):
#      mv = lst[0]
#      for i in lst:
#           if i>mv:
#                mv = i
#      return mv
# def sgrmin(lst):
#      mnv = lst[0]
#      for j in lst:
#           if j<mnv:
#                mnv = j
#      return mnv

# findmax = lambda lst : sgrmax(lst)
# findmin = lambda lst: sgrmin(lst)

# lst = [int(i) for i in input("Enter values seprated by commas : ").split()]
# res_findmax = findmax(lst)
# res_findmin = findmin(lst)
# print(f"Maximum value is : {res_findmax}")
# print(f"SMallest value is : {res_findmin}")


# def findpos(val):
#           if val>0:
#             return False
#           if val<0:
#                return True


# lst= [int(i) for i in input("Enter space seprated values : ").split()]
# pos  = filter(findpos,lst)
# # print(type(pos))
# obj = list(pos)
# print(obj,type(obj))


# def findpos(val):
#           if val>0:
#             return False
#           if val<0:
#                return True


# n = int(input("Enter how many do you want : "))
# lst = []
# for i in range(1,n+1):
#       val = int(input(f"Enter {i} value : "))
#       lst.append(val)

# pos  = filter(findpos,lst)
# # print(type(pos))
# obj = list(pos)
# print(obj,type(obj))

# findpos = lambda val :  val>0

# lst= [int(i) for i in input("Enter Space Seprated values : ").split()]
# pos = tuple(filter(findpos,lst))
# print(pos,type(pos))


# lst = [int(i) for i in input("Enter Space Seprated values : ").split()]
# pos = tuple(filter(lambda val : val<0,lst))
# print(pos,type(pos))


# lst = [i for i in input("Enter a word : ")]
# vowels = list(filter(lambda word:  "a" in word or "e" in word or "i" in word or "o" in word or "u" in word ,lst))
# print(vowels)


# lst = [int(i) for i in input("Enter space seprated values : ").split()]
# pos = list(filter(lambda val : val>0,lst))
# nl = list(filter(lambda val: val<0 ,lst))
# print(pos)
# print(nl)

# lst = [i for i in input("Enter a word : ").split()]
# plst = list(filter(lambda word : word== word[::-1],lst))
# print(plst)


# lst = [i for i in input("Enter a line of text : ").split()]
# nl = list(filter(lambda word:4>=len(word)>=3,lst ))
# print(nl)

# lst = [i for i in input("Enter a line of text : ").split()]
# nl = list(filter(lambda word:word[0]==word[-1] and word!=word[::-1],lst ))
# print(nl)
# def evenval(val):
#      if val %2==0:
#           return True
#      else:
#           return False

# lst = [int(i) for i in input("Enter values  : ").split()]
# el  =  list(filter(evenval,lst ))
# ol = list(filter(lambda val : val%2!=0,lst ))
# print(f"Even list : {el}")
# print(f"odd list : {ol} ")

# def hike(sal):
#      return sal +sal*50/100


# lst = [int(i) for i in input("Enter salary fo employee : ").split()]
# newsal = list(map(hike , lst))
# # print(newsal,type(newsal))
# print("OLD SALARY \t NEW SAL")
# for os ,ns in zip(lst,newsal):
#      print(os,"\t\t",ns)


# lst = [int(i) for i in input("Enter salary fo employee : ").split()]
# newsal = list(map(lambda sal :sal+sal*50/100, lst))
# # print(newsal,type(newsal))
# print("OLD SALARY \t NEW SAL")
# for os ,ns in zip(lst,newsal):
#      print(os,"\t\t",ns)


# lst = [int(i) for i in input("Enter salary fo employee : ").split()]
# newsal = list(map(lambda sal :sal<0, lst))
# # print(newsal,type(newsal))
# print("OLD SALARY \t NEW SAL")
# for os ,ns in zip(lst,newsal):
#      print(os,"\t\t",ns)

# def sumop(val1,val2):
#   return val1+val2

# l1= [int(i) for i in input("Enter values for first list : ").split()]
# l2 = [int(j) for j in input("Enter values for second list : ").split() ]
# sv = list(map(sumop, l1,l2))
# print("VAL1 VAL2 \t  SUM")
# for v1,v2 ,s in zip(l1,l2,sv):
#   print(v1,"\t",v2,"\t",s)


# l1= [int(i) for i in input("Enter values for first list : ").split()]
# l2 = [int(j) for j in input("Enter values for second list : ").split() ]
# sv = list(map(lambda v1,v2 :v1+v2, l1,l2))
# print("VAL1 VAL2 \t SUM")
# for v1,v2 ,s in zip(l1,l2,sv):
#   print(v1,"\t",v2,"\t",s)


# l1= [int(i) for i in input("Enter values for first list : ").split()]
# sv = list(map(lambda v1:v1**0.5, l1))
# print("VALUE \t SQRT")
# for v1 ,s in zip(l1,sv):
#   print(v1,"\t",s)


# l1= [int(i) for i in input("Enter values for first list : ").split()]
# sv = list(map(lambda v1:v1**2, l1))
# print("VALUE \t SQUARE")
# for v1 ,s in zip(l1,sv):
#   print(v1,"\t",s)

# empdt = {"karan":1000,"jay":2000,"sahil":3000,"paa":4000}

# upsal = list(map(lambda x :empdt[x]+empdt[x]*50/100 ,empdt))

# print("OlD SALRY NEW SALRY")
# for os,ns in zip(empdt,upsal):
#      print(os,ns)


# n = int(input("Enter values : "))
# dict = {input(f"Enter {i} value : "): input(f"Enter {i} value : ") for i in range(1,n+1)}
# print(dict)


# n =  int(input("Enter how many do you want to enter : "))
# dict= {}
# for i in range(1,n+1):
#      key = float(input("Enter key value : "))
#      value = float(input("Enter value of key : "))
#      dict[key] = value

# import sys
# dict = {}
# while True:
#         eno = float(input("Enter Employee number : "))
#         salary = float(input("Enter Employee Salary : "))
#         dict[eno] = salary
#         ch = input("do you want to enter anothe emp data - (yes/ no): ").lower()
#         if ch == "no":
#           break
#         if ch not in ["yes","no"]:
#           sys.exit()

# print("ENO \t OLD SALARY")
# for eno,nwsal in dict.items():
#   print(eno,"\t",nwsal)


# modsal = list(map(lambda x :x+x*50/100  ,dict.values()))
# #[1500.0, 3000.0, 4500.0]
# for k,v in zip(dict,modsal):
#   dict[k]=v
# print(dict)

# print("ENO \t NEW SALARY")
# for eno,nwsal in dict.items():
#   print(eno,"\t",nwsal)


# l1= [int(i) for i in input("Enter values for first list : ").split()]
# l2 = [int(j) for j in input("Enter values for Second list : ").split()]

# if len(l1)<len(l2):
#      for i in range(len(l2)-len(l1)):
#           l1.append(0)
# if len(l1)>len(l2):
#      for i in range(len(l1)-len(l2)):
#           l2.append(0)

# else:
#   sumlist = list(map(lambda a,b : a+b,l1,l2))

#   print(sumlist)


# def getval():
#      return{10

# def squar}(getval):
#      def calculation():
#       n = getval()
#       return n,n**2
#      return calculation
# res = square(getval)
# n,square = res()
# print(n,square)


# def box(function):
#  def new_display():
#   print("*************************")
#   function()
#   print("************************")
#  return new_display

# @box
# def display():
#  print("Hello python")

# display()


# def getval():
#      return int(input("Enter value : "))

# def square(getval):
#    def sqrcalc():
#       n=  getval()
#       sqres = n**2
#       return n, sqres
#    return sqrcalc

# def cube(getval):
#     def cbcal():
#       c = getval()
#       cubres  = c**3
#       return c,cubres
#     return cbcal

# n,sqres= square(getval)()
# print(n,sqres)
# c,sqres= cube(getval)()
# print(c,sqres)


# def getval():
#      return int(input("Enter first value : ")),int(input("Enter second value : "))

# def addop(getval):
#      def addcal():
#           n1, n2 = getval()
#           res =n1+n2
#           return n1,n2,res
#      return addcal

# n1,n2,res  = addop(getval)()
# print(f"sum of ({n1},{n2})={res}")

# def getval():
#      return int(input("Enter first value :  ")),int(input())

# def getval():
#      return int(input("Enter First value : ")),int(input("Enter second value : "))

# def multable(getval):
#   def multablecal():
#       n1,n2= getval()
#       res = n1*n2
#       return n1,n2, res
#   return multablecal


# n1,n2, res= multable(getval)()
# print(f"Multiplication of : ({n1},{n2}) = {n1*n2}")


# def square(getval):
#      def sqop():
#           n = getval()
#           res = n**2
#           return n ,res
#      return sqop

# @square
# def getval():

#      return int(input("Enter a number :"))

# n,res = getval()
# print(n,res)


# try:
#      a = int(input("Enter first value : "))
#      b = int(input("Enter Second value :"))
#      c = a/b
#      print(c)
#      s = "python"
#      print(s[0])
#      print("My name is anthony gunjaliwsh ")
# except ValueError:
#      print("Dont Enter alnums ,alphabets,symbols...")
# except ZeroDivisionError:
#      print("Dont Enter Zero As Denominator")
# except IndexError:
#      print("Index is out of range()")
# except:  # noqa: E722
#      print("Ooops something went wrong - check for exception ")


# class NumberDivisonError(Exception):pass
# class NotNumberError(BaseException):pass
# try:
#  a= input("Enter first Value : ")
#  b= input("Enter Second Value : ")
#  if not a.isdigit() or not b.isdigit():
#       raise NotNumberError
#  x = int(a)
#  y = int(b)
#  if y==0:
#       raise NumberDivisonError
#  else:

#   print(x/y)
# except NumberDivisonError:
#    print("Dont Enter Zero as Denominator")
# except NotNumberError:
#    print("Dont enter alnums,alphabets , symbols")


# class InvalidNameError(Exception):pass
# class ZeroLenghtError(Exception):pass
# class SpaceError(Exception):pass
# n = input("Enter Name : ")
# try:
#   if len(n)==0:
#        raise ZeroLenghtError
#   elif n.isspace():
#        raise SpaceError
#   else:
#    lst = n.split()
#    for word in lst:
#         if not word.isalpha():
#             raise InvalidNameError
#    print(n)
# except InvalidNameError:
#     print("Please Enter Valid Name  ")
# except ZeroLenghtError:
#     print("Please Enter Name - Dont Leave Empty")
# except SpaceError:
#     print("Dont Enter SPaces ")


# class NegNumberError(Exception):pass


# def mulop():
#      try:
#       a = int(input("Enter first Number  : "))
#       b = int(input("Enter Second Number :"))

#       if a<0 or b<0:
#            raise NegNumberError
#       else:
#            c= a*b
#            print(f"Multiplication : {c}")
#      except NegNumberError:
#           print("Dont Enter Negative Number ")
#      except ValueError:
#           print("Dont Enter alums,alphabets , symbols")
# mulop()


# class NonPrimeError(Exception):pass
# n = int(input("Enter A Number : "))
# try:
#  if n<=1:
#       raise NonPrimeError
#  else:
#       res = True
#       for i in range(2,n):
#            if n%2==0:
#                res = False
#                break
#  if res :
#   print(f"{n} is Prime Number ")
#  else:
#   print(f"{n} is Not a Prime Number")

# except NonPrimeError:
#      print(f"Dont Enter 1 and Negative Number ")
# except ValueError:
#      print("Dont Enter alnums,alphabets , symbols")


# class NonPrimeError(Exception):pass
# try:
#  n = int(input("Enter A Number : "))
#  if n<=1:
#       raise NonPrimeError
#  else:
#       res = True
#       for i in range(2,n):
#            if n%2==0:
#                res = False
#                break
#  if res :
#   print(f"{n} is Prime Number ")
#  else:
#   print(f"{n} is Not a Prime Number")

# except (NonPrimeError,ValueError):
#      print(f"Dont Enter 1 and Negative Number ")
#      print("Dont Enter alnums,alphabets , symbols")


# class ZeroError(Exception):pass
# class NegNumError(BaseException):pass

# try:
#  n = int(input("Enter a number :"))

#  if n==0:
#       raise ZeroError
#  elif n<0:
#       raise NegNumError
#  else:
#     for i in range(1,11):
#        print(f"{n} X {i} = {n*i}")

# except ZeroError:
#  print("Dont Enter Zero ")
# except NegNumError:
#    print("Dont Enter Negative Number")
# except ValueError:
#    print("Dont Enter ALnums , Alphabets , Symbols")
# except :
#    print("Oooppps Something went Wrong- check for Exception")


# class ZeroError(Exception):pass
# class NegNumError(BaseException):pass
# try:
#  n = int(input("Enter a number :"))
#  if n==0:
#       raise ZeroError
#  elif n<0:
#       raise NegNumError
#  else:
#     for i in range(1,11):
#        print(f"{n} X {i} = {n*i}")
# except (ZeroError,NegNumError,ValueError):
#  print("Dont Enter Zeros As input ")
#  print("Dont Enter Negative Number ")
#  print("Dont enter alnums, alphabets, symbols ")


# def kvrrange(x):
#      s = 0
#      while s<x:
#          yield s
#          s =  s+1

# # n = int(input("Enter A Value : "))
# res = kvrrange(6)
# while True:
#      try:
#       print(next(res))
#      except StopIteration:
#            break


# def kvrrange(n):
#      s = 0
#      while s<n:
#           yield s
#           s= s+1
# r = kvrrange(6)
# print("------")
# print(next(r))
# print("--------")
# for i in r:
#      print(i)


# def getcrs():
#      yield "python","kvr"
#      yield "java"
#      yield 1234 ,"Numbers"
#      yield "data Science"
# r = getcrs()
# for val in r:
#      print(val)


# def kvrange(start,stop=0,step=1):
#      if start>stop:
#         stop= start
#         start = 0
#      else:
#       while start<=stop:
#        yield start
#        start = start+step

# print("---------first--------------------")
# r = kvrange(1{10,3)
# for val}in r:
#   print(val)

# print("-------------second----------------")
# r= kvrange(1,9)
# for val in r:
#    print(val)
# print("--------------third---------------")

# r = range(9)
# for val in r:
#    print(val)


# class student:
#     pass


# s1 = student()
# s2 = student()

# s1.sno = int(input("Enter Student Number : "))
# s1.sname = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))


# print(f"Student Number : {s1.sno}")
# print(f"Student Name  : {s1.sname}")
# print(f"Student Marks : {s1.marks} ")


# s2.sno = int(input("Enter Student Number : "))
# s2.sname = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))


# print(f"Student Number : {s2.sno}")
# print(f"Student Name  : {s2.sname}")
# print(f"Student Marks : {s2.marks} ")


# class student:pass

# s1 = student()
# s2 = student()


# print("---------------------")
# print(f"Content of s1 :{s1.__dict__}")
# print(f"Lenght :{len(s1.__dict__)}")
# print(f"Content of s1 :{s2.__dict__}")
# print(f"Lenght :{len(s2.__dict__)}")
# print("---------------------")

# s1.sno = int(input("Enter Student Number : "))
# s1.sname = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))


# print(f"Content of s1 :{s1.__dict__}")
# print(f"Lenght :{len(s1.__dict__)}")

# s2.sno = int(input("Enter Student Number : "))
# s2.sname = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))

# print(f"Content of s1 :{s2.__dict__}")
# print(f"Lenght :{len(s2.__dict__)}")


# print("-----------------")
# for k,v in s1.__dict__.items():
#      print(f"{k}-->{v}")

# print("-----------------")


# for k in s1.__dict__:
#      print(k,"--->",s1.__dict__[k])


# for k in s1.__dict__.keys():
#      print(k,"--->",s1.__dict__[k])

# print("-----------------")


# class student:
#     pass
# s1 = student()
# s2 = student()

# s1.sno = int(input("Enter Student Number : "))
# s1.sname = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))

# for dmn, dmv in s1.__dict__.items():
#     print(f"{dmn}--> {dmv}")

# s2.sno = int(input("Enter Student Number : "))
# s2.sname = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))

# for dmn in s2.__dict__.keys():
#     print(f"{dmn}--> {s2.__dict__[dmn]}")


# class student :
#      crs = input("Enter Course Name : ")
#      city = input("Enter City : ")

# s1 = student()
# s2= student()

# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)

# class student :pass

# student.crs = input("Enter Course Name  : ")
# student.city = input("Enter City Name : ")

# s1 = student()
# s2 = student()

# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)


# class student : 
#      def readstudentdata(self,objinfo):
#           print("-"*50)
#           print(f"Enter {objinfo} student Data")
#           print("-"*50)
#           self.sno = int(input("Enter Student Number : "))
#           self.sname= input("Enter Student Name : ")
#           self.marks = float(input("Enter Stuent Marks : "))
#      # def displaystudentdata(self,objinfo):
#      #      print("-"*50)
#      #      print(f"Display {objinfo} student Data")
#      #      print("-"*50)
#      #      print(self.sno)
#      #      print(self.sname)
#      #      print(self.marks)




# s1 = student()
# s1.readstudentdata("first")
# # s1.displaystudentdata("first")
# for k, v in s1.__dict__.items():
#      print(k,"-->",v)
# s2 = student()
# s2.readstudentdata("second")
# # s2.displaystudentdata("second")
# for k, v in s2.__dict__.items():
#      print(k,"-->",v)

# try:
#  fp = open("open.txt","r")
#  print("File opened successfully ")

# except FileNotFoundError:
#  print("File does not exist ")
# else:
#   print(f"File Mode is : {fp.mode}")
#   print(f"Type of fp : {type(fp)}")
#   print(f"Does the file is readable : {fp.readable()}")  # funtion
#   print(f"Does the file is Writale : {fp.writable()}")
#   print(f"Does the file is closed : {fp.closed}")
#   print(f"File Mode is : {fp.mode}")
# finally:
#  try :
#   print("I am from finaly block ")
#   fp.close()
#   print("after manual closing")
#   print(f"Does the file is closed : {fp.closed}")
#  except NameError:
#   print("Unable to open there is no need to close")


# with open("open.txt","+a") as fp:
#      print(f"file opened successfully in {fp.mode}")
#      print(f"Does the file is readable : {fp.readable()}")
#      print(f"Does the file is Writeble : {fp.writable()}")
#      print("before the indentation ")
#      print(f"Does The file is cloesd : {fp.closed}")
# print("After the indentation ")
# print(f"Does The file is cloesd : {fp.closed}")




# class student : 
#   def readstudentdata(self,objinfo):
#     print("-"*30)
#     print(f"Enter {objinfo} Student Data")
#     print("-"*30)
#     self.sno = int(input("Enter Student Number : "))
#     self.sname = input("Enter Student Name : ")
#     self.marks = float(input("Enter Student Marks : "))
#   def displaydata(self,objinfo):
#       print("-"*30)
#       print(f"Display {objinfo} Student Data")
#       print("-"*30)
#       for k,v in self.__dict__.items():
#          print(k,"-->",v)
         

# s1 = student()
# s1.readstudentdata("First")
# s1.displaydata("First")
# s2 = student()
# s2.readstudentdata("Second")
# s2.displaydata("Second")


# class student : 
#      def readstudentdat(self):
#           print(id(self))


# s1 = student()
# print(id(s1))
# s1.readstudentdat()
# s2 = student()
# print(id(s2))
# print(id(s2))



# with open("open.txt","a") as fp:
#      sno = int(input("Enter Student Number : "))
#      sname = input("Enter Student Name : ")
#      marks = float(input("Enter Student Marks : "))
#      fp.write(f"{sno} \t {sname}  \t {marks} \n")
#      print("Data Written Into File Successfully - verify")


# with open("open.txt","r") as fp:
#      filedata = fp.read()
#      print(filedata)

# with open("x+5.txt","x+") as fp:
#      sno = int(input("Enter Student Number : "))
#      sname = input("Enter Student Name : ")
#      marks = float(input("Enter Student Marks : "))
#      fp.write(f"{sno} \t {sname}  \t {marks} \n")
#      fp.seek(0)
#      filedata = fp.readlines()
#      for val in filedata:
#           print(val)
#           print('------fpreadlines---')
#      fp.seek(0)
#      filedata = fp.read()
#      print(filedata)
#      print('------fpreadlines---')




# print("Enter Data - Press @ to stop : ") 
# with open("rr.txt" ,"a") as fp:
#  while True:
#     filedata = input()
#     if  filedata!= "@":
#       fp.write(filedata + "\n")
#     else:
#       print("filedata Written Successfully - verify")
#       break
        
     
   
# class student : pass


# s1 = student()
# s2 = student()

# s1.sno =  int(input("Enter Student Number : "))
# s1.name = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))

# for k,v in s1.__dict__.items():
#   print(k,v)
# print(s1.sno)
# print(s1.name)
# print(s1.marks)


# s2.sno =  int(input("Enter Student Number : "))
# s2.name = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))

# for k,v in s2.__dict__.items():
#   print(k,v)
# print(s2.sno)
# print(s2.name)
# print(s2.marks)






  
# class student : 
#   def readvalues(self,objinfo):
#    print(f"Enter {objinfo} Student Data")
#    self.sno =  int(input("Enter Student Number : "))
#    self.name = input("Enter Student Name : ")
#    self.marks = float(input("Enter Student Marks : "))
  
#   def displayvalues(self,objinfo):
#     print(f"Display {objinfo} Student Data")
#     print(self.sno)
#     print(self.name)
#     print(self.marks)


# s1 = student()
# s2 = student()

# s1.readvalues("First")
# s1.displayvalues("First")


# s2.readvalues("Second")
# s2.displayvalues('Second')

# class student:
#    def readvalues(self,objinfo):
#     print(f"Enter {objinfo} Student Data")
#     self.sno =  int(input("Enter Student Number : "))
#     self.name = input("Enter Student Name : ")
#     self.marks = float(input("Enter Student Marks : "))

#    def displayvalues(self,objinfo):
#      print(f"Display {objinfo} Student Data")
#      for k,v in self.__dict__.items():
#       print(k,v)



# s1 = student()
# s2 = student()

# s1.readvalues("First")
# s1.displayvalues("First")


# s2.readvalues("Second")
# s2.displayvalues('Second')



# class student :
#   crs = "python"
#   city = "Hyd"


# s1 = student()

# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)



# class student : pass


# student.crs = "python"
# student.city = "hydrabad"

# s1= student()
# s2 = student()
# print("------s1-----")
# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)
# print("------s1-----")
# print("------s2-----")
# print(s2.crs)
# print(s2.city)

# print(student.crs)
# print(student.city)
# print("------s2-----")



# try:
#  with open("sagar.txt","x+") as fp:
#      print(f"File opened in mode : {fp.mode}")
#      print(f"Does the file is readable : {fp.readable()}")
#      print(f"Does the file is Writable : {fp.writable()}")
# except FileExistsError:
#    print("File already exist ")


# with open("open.txt","w") as fp:
#      # fp.write("sagar \t")
#      # fp.write(str(100)+"\t")
#      # fp.write(str(200000)+"\n")
#      fp.write(f" Sagar \t {10000} \t {False} \n")
#      fp.write(f" Sagar \t {10000} \t {False} \n")
#      print("data Written successfully - verify ")

# x = {10,20,30,40)
# }ith open("open.txt","a") as fp:
#      fp.writelines(f"{x} \n")
#      print("Data written successfully - verify")

# with open("open.txt","a") as fp:
#      sno = int(input("Enter Student Number : "))
#      sname = input("Enter student Name : ")
#      smarks = float(input("Enter Student Marks : "))

#      # fp.write(str(sno)+"\t")
#      # fp.write(sname+"\t")
#      # fp.write(str(smarks)+"\n")

#      fp.write(f"{sno} \t {sname} \t {smarks} \n")
#      print('data written successfully - verify')


# lst = {10,20,30]
# wit} open("open.txt","a") as fp:
#      fp.writelines(f"{lst} \n")
#      print("Data Written to file successfully -  verify ")



# with open("open.txt",'r') as fp:
#      # filedata = fp.read()
#      # print(filedata)

#      filedata = fp.readlines()
#      # print(filedata)
#      for val in filedata:
#           print(val)


# srcfile = input("Enter Source file name  : ")
# with open(srcfile, "r") as fp:
#      filedata = fp.read()
#      dstfile = input("Enter Destination File Name : ")
#      with open(dstfile,"a") as fp:
#           fp.write(str(filedata))
#           print("File Copied Successfully - verify")

# with open("open.txt","r") as fp:
#      filedata = fp.readlines()

#      nl = 0
#      nw = 0
#      nc = 0 
#      for line in filedata:
#         nl = nl+1
#         nw = nw+len(line.split())
#         nc = nc+len(line)
#      print("Number of line : ",nl)
#      print("Number of words : ",nw)
#      print("Number of Chatacters : ",nc)



# with open("C:\\Users\\sdhok\\OneDrive\\Pictures\\backiee-217218.jpg", "rb") as rp:
#      imgdata = rp.read()
#      with open("ptyhom.png","wb") as wp:
#           wp.write(imgdata)
#           print("Image Copied SuccessFully - verify ")

# import pickle
# with open("1.txt" ,"ab") as fp:
#   sno = int(input("Enter Student Number : "))
#   sname = input("Enter Student Name : ")
#   smarks = float(input("Enter Student Marks : "))
#   lst =  []
#   lst.append(sno)
#   lst.append(sname)
#   lst.append(smarks)
#   pickle.dump(lst,fp)
#   print("FIle Data Written Successfully ")

  

# import pickle
# with open("1.txt" ,"rb") as fp:
#      while True:
#       try:
#        records = pickle.load(fp)
#        print(records,end="\t")
#        print()
#       except EOFError:
#          break



# with open("student_data.csv", "r") as fp:
#      filedata = fp.readlines()
#      print(filedata)
#      for val in filedata:
#           print(val)

# with open("student_data.csv", "r") as fp:
#      filedata = fp.read()
#      print(filedata)

# import pandas
# fd = pandas.read_csv("student_data.csv")
# print(fd)

# import csv
# with open("student_data.csv","r") as fp:
#    records = csv.reader(fp)
#    for record in records:
#        for val in record:
#         print(val,end="\t")
#        print()

# import csv 
# with open("student_data.csv" ,"r") as fp:
#      records = csv.DictReader(fp)
#      recno = 0

#      for record in records:
#           # print(record)
#           print(f"Record Number : {recno}")
#           for k,v in record.items():
#                print(f"{k}-->{v}")
#           print()
#           recno +=1



# class Employee:
#      @classmethod
#      def getvalues(cls):
#           cls.compname = "ibm"
#           Employee.city = "Hydrabad"

# Employee.getvalues()
# print(Employee.compname)
# print(Employee.city)


# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = "ibm"

#      @classmethod
#      def getcity(cls):
#           Employee.city = "Hydrabad"

# Employee.getcomp()
# print(Employee.compname)
# Employee.getcity()
# print(Employee.city)

# print("WIth Object name below")
# eo = Employee()
# eo.getcity()
# print(eo.city)
# eo.getcomp()
# print(eo.compname)


# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = "Ibm"
#           # cls.getcity()

#      @classmethod
#      def getcity(cls):
#           Employee.city = "Hydrabad"
#           Employee.getcomp()

# # Employee.getcomp()
# eo = Employee()
# eo.getcity()
# print(Employee.compname)
# print(Employee.city)      
 

# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = "IBM"
#      @classmethod
#      def getcity(cls):
#           cls.city = "Hydrabad"
#           cls.getcomp()
#      def getempvalues(self):
#           self.eno = int(input("Enter Employee Number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = int(input("Enter Employee Salary : "))
#      def displayempvals(self):
#           self.getempvalues()
#           print(self.eno)
#           print(self.name)
#           print(self.sal)
#           print(Employee.compname)
#           print(Employee.city)
# Employee.getcity()
# eo = Employee()
# eo.displayempvals()

# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.comp = "IBM"
#           Employee.getcity()
           
#      @classmethod
#      def getcity(cls):
#           cls.city = "Hydrabad"
         
          
#      def getempvals(self):
#           self.eno = int(input("Enter Employee number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = input("Enter Employee Salary : ")
#           self.displayvals()

#      def displayvals(self):
#          Employee.getcomp()
#          print(self.eno)
#          print(self.name)
#          print(self.sal)
#          print(Employee.comp)
#          print(Employee.city)


# Employee.getcomp()
# eo= Employee()
# eo.getempvals()



# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.comp = "IBM"
#           Employee.getcity()
#           Employee().getempvals()

           
#      @classmethod
#      def getcity(cls):
#           cls.city = "Hydrabad"
         
          
#      def getempvals(self):
#           self.eno = int(input("Enter Employee number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = input("Enter Employee Salary : ")
#           self.displayvals()

#      def displayvals(self):
#          print(self.eno)
#          print(self.name)
#          print(self.sal)
#          print(Employee.comp)
#          print(Employee.city)


# Employee.getcomp()



# Res.displayvals(s,"Student")
# Res.displayvals(e,"Employee")
# Res.displayvals(t,"Teacher")



# Res.displayvals(s,"Student")
# Res.displayvals(e,"Employee")
# Res.displayvals(t,"Teacher")







# class Student:
#      def studvals(self):
#       self.sno = int(input("Enter Student Number : "))
#       self.sname = input("Enter student Name : ")
#       self.smarks = int(input("Enter Student Marks : "))

# class Emp:
#      def empvals(self):
#           self.empsal = int(input("Enter Employee Salary : "))

# class Teacher :
#      def teacherlvas(self):
#           self.tname = input("Enter Teacher Name : ")

# class Res :
#      @staticmethod
#      def vals(cls,obj,objinfo):
#         Res.displayvals(cls,obj,objinfo)
#      @staticmethod
#      def displayvals(obj,objinfo):
#       print(f"Displaying Values of {objinfo}")
#       for k,v in obj.__dict__.items():
#           print(k,v)

# s = Student()
# e = Emp()
# t = Teacher()
# s.studvals()
# e.empvals()
# t.teacherlvas()

# Res.vals("")

#       self.sname = input("Enter student Name : ")
#       self.smarks = int(input("Enter Student Marks : "))

# class Emp:
#      def empvals(self):
#           self.empsal = int(input("Enter Employee Salary : "))

# class Teacher :
#      def teacherlvas(self):
#           self.tname = input("Enter Teacher Name : ")

# class Res :
#      @staticmethod
#      def vals(cls,obj,objinfo):
#         Res.displayvals(cls,obj,objinfo)
#      @staticmethod
#      def displayvals(obj,objinfo):
#       print(f"Displaying Values of {objinfo}")
#       for k,v in obj.__dict__.items():
#           print(k,v)

# s = Student()
# e = Emp()
# t = Teacher()
# s.studvals()
# e.empvals()
# t.teacherlvas()

# Res.vals(e,"EMployee")
# Res.vals(s,"Student")
# Res.vals(t,"Teacher)



# import pickle
# with open("1.pick", "ab")  as fp:
#      d ={}
#      sno = int(input("Enter Student Number : "))
#      name = input("Enter Student Name :")
#      # marks = float(input("Enter Student Marks : "))  
#      d[sno] = name
#      pickle.dump(d,fp)
#      print("Data Added Successfully : ")




# import pickle
# with open("1.pick", "rb")  as fp:
    
#      while True:
#       try:
#        filedata = pickle.load(fp)
#        print(filedata)
#        print(type(filedata))
#       except EOFError:
#           break

# import csv 
# with open("student_data.txt","r") as fp:
#      csvr = csv.reader(fp)
#      print(csvr,type(csvr))

#      for record in csvr:
#           # print(record)
#           for val in record:
#                print(val,end="\t")
#           print()
   



# import csv 
# with open("student_data.csv","r") as fp:
#      csvdr = csv.DictReader(fp)
#      print(csvdr,type(csvdr))

#      recno = 1
#      for record in csvdr:
#           print("-"*20)
#           print(f"RECORD NUMBER : {recno}")
#           print("-"*20)
#           for k,v in record.items():
#                print(k,"->",v,end="\t") 
#           print()
#           recno +=1


# import csv
# with open("student_data.csv","r") as fp:
#      csvdr = csv.DictReader(fp)
#      print(csvdr,type(csvdr))

#      for record in csvdr:
#           print("---------")
#           for k,v in record.items():
#                print(k,"->",v) 




# import csv 
# nc = int(input("Enter How many colums do you want to enter : "))
# if nc <=0: 
#      print("Invalid input Please Enter valid input")
# else:
#      col = []
#      for i in range(1,nc+1):
#           val =input(f"Enter {i} Column Name :  ")
#           col.append(val)

#      else:
#          nr = int(input("Enter How Many Records Do you Want To Enter : "))
#          if nr <=0: 
#             print("Invalid input Please Enter valid input")
#          else:
#           main_record = []
#           for i in range(1,nc+1):
#               print(f"Enter {i} Record : ")
#               record = []
#               for j in range(len(col)):
#                   val = input(f"Enter val for - {col[j]} : ")
#                   record.append(val)
#               else:
#                   main_record.append(record)
#           else:
#               with("1.csv","a") as fp:
#                   csvwr = csv.writer()
#                   csvwr.writerow(col)
#                   csvwr.writerows(main_record)
#                   print("Record saved Successfully ")    




              




# import csv 
# nc = int(input("Enter How many colums do you want to enter : "))
# if nc <=0: 
#      print("Invalid input Please Enter valid input")
# else:
#      col = []
#      for i in range(1,nc+1):
#           val =input(f"Enter {i} Column Name :  ")
#           col.append(val)

#      else:
#          nr = int(input("Enter How Many Records Do you Want To Enter : "))
#          if nr <=0: 
#             print("Invalid input Please Enter valid input")
#          else:
#           main_record = []
#           for i in range(1,nc+1):
#               print(f"Enter {i} Record : ")
#               record = {}
#               for j in range(len(col)): 
#                   val = input(f"Enter val for - {col[j]} : ")
#                   record[col[j]] = val
#               else:
#                   main_record.append(record)
#           else:
#               with("1.csv","a") as fp:
#                   csvwr = csv.DictWriter(fp,fieldnames=col)
#                   csvwr.writeheader()
#                   csvwr.writerows(main_record)
#                   print("Record saved Successfully ")    




              

# import csv
# with open("student_data.csv","r") as fp:
#      csvdr = csv.DictReader(fp)
#      print(csvdr,type(csvdr))

#      for record in csvdr:
#           print("---------")
#           for k,v in record.items():
#                print(k,"->",v) 



# import json
# jd = '{"name": "karan", "age": 18}'


# dict = json.loads(jd)
# print(dict)
# d = {'name': 'karan', 'age': 18}
# jd = str(d)
# print(jd)


# import json
# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York",
#     "country": "USA"
# }

# with open("2.json","a") as fp:
#      json.dump(my_dict,fp)
#      print("Data inserted successfully ")


# import json
# try:
#  with open("2.json","r") as fp:
#       jd = json.load(fp)
#       # print(jd)
#       for k,v in jd.items():
#            print(k,"-->",v)
# except FileNotFoundError as e:
#     print(e)


# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = l1+l2
# print(l3)

# import numpy as np

# arr1 = np.array([1, 2, 3, 4])
# print(f"1D array : {arr1}")


# arr2 = np.array([1, 2, 3, 4])
# print(f"2D array : {arr2}")

# sumarr = arr1+arr2
# print(f"Sum of : {sumarr}")


# l1 = ([1,2,3,4])
# l2 = ([5,6,7,8])
# l3 = l1+l2
# print(l3)


# n = int(input("Enter How Many number you want to generate : "))
# i = 1
# while(i<=n):
#      print(i)
#      i = i+1


# n = int(input("Enter Number : "))
# temp = n
# s = 0
# while n>0:
#      r = n%10
#      s = s+r
#      n = n//10
# print(f"Sum of {temp} = {s} ")

# import sys
# import numpy as np
# lst = [10,20,30,40,56]
# print("lst = ",sys.getsizeof(lst))

# a = np.array(lst)
# print("ndarry = ",sys.getsizeof(a))


# import numpy as np
# import sys 
# lst =[1,2,3,4,56,7,8,9,1,2,3,4,5,6,7,8,9]

# print("Size of lst",sys.getsizeof(lst))

# arr = np.array(lst)
# print("Size of arr ",sys.getsizeof(arr))


# def disp(*kvr):
#      print("Number of values : ",len(kvr))
#      for i in kvr:
#           print(i)


# disp(10,20,30,40,50,60)
# disp(10,20,30,40,60)
# disp(10,20,30,60)
# disp(10,20,30)
# disp(10,20)
# disp(10,)


# n= int(input("Enter a number : "))
# if n<=1:
#      print(f"{n} is invalid input")
# else:
#      res = "Prime"
#      for i in range(2,n):
#           if n%i==0:
#                res ="Not Prime"
#                break
     
     
#      if res == "Prime":
#           print(f"{n} is Prime Number ")
#      else:
#           print(f"{n} is not a prime number ")
          

# n = int(input("Enter a number : "))
# if n<=1:
#      print(f"{n} is invalid number ")
# else:
#      i= 2
#      res = True
#      while i<=n//2:
#           if n%i==0:
#                res = False
#           i = i+1
#      result = "prime" if  res else "NOt prime"
# print(result)
     

# n = int(input("Enter a number : "))
# if n<=1:
#      print(f"{n} is invalid input")
# else:
#      res = 1
#      for i in range(2,n//2+1):
# #           if n%i == 0:
# #                res = 0
# #                break
# # result  = "Prime" if res else "Not prime"
# # print(result)



# for i in range(1,3):
#      print("Outer loop : ",i)
#      for j  in range(1,3):
#           print(j)
#      else:
#       print("Else block of inner for loop")
# else:
#     print("Else block of outer for loop")
     


# n = int(input("Enter a value : "))
# i = 0
# while i<=n:
#      print("Outer loop : ",i) 
#      j = 0
#      while j<=n:
#        print(j)
#        j = j+1 
#      else:
#       print("Else block of inner while loop")
#      i = i+1
# else:
#   print("else block of outer while loop")

# n = int(input("Enter a number : "))
# for val in range(n):
#   print("Outer for loop : ",val)
#   j = n
#   while j>0:
#     print(j)
#     j = j-1
#   else:
#     print("Else block of inner while loop")
# else:
#   print("Else block of outer for loop")

# n= int(input("ENter a number : "))
# i = 0
# while i<=n:
#   print("Outer for loop : ",i)
#   for val in range(n,-1,-1):
#       print(val)
#   else:
#     print("Else block of inner for loop")
#     i = i+1
# else:
#   print("Else block of outer while loop")

# n = int(input("Enter a number upto where you want to genrate : "))
# for i in range(2,n+1):
#   print("---------------------------------------")
#   for j in range(1,11):
#     print(f"{i} X {j}  = {i*j}")
#   print("---------------------------------------")

# n = int(input("Enter a number : "))
# if n<=1:
#   print(f"{n} is invalid input")

# for i in range(2,n+1):  
#   res= True
#   for j in range(2,i):
#     if i%j==0:
#       res = False
#       break
#   if res:
#     print(f"{i} is prime Number  ")
#   else:
#     print(f"{i} is not a prime number")


# n = int(input("ENter number upto u want to check prime number "))
# if n<=1:
#   print(f"{n} is invalid input")
# else:
#   i  =2 
#   while i<=n:
#     j = 2
#     res  = True
#     while j<i:
#       if i%j==0:
#         res = False
#         break
#       j = j+1
#     if res :
#       print(f"{i} is prime number")
#     else:
#       print(f"{i} Not a prime Number")
#     i = i+1





# n= input("Enter a line of text : ").split()
# for word in n:
#   print("------------")
#   print(word)
#   print("------------")
#   for letter in word:
#     print(letter)



# try:
#  sno = int(input("Enter a number : "))
#  if sno in range(100,200):
#    print("Correct")
#  else:
#    print(f"{sno} is invalid student number ")
# except ValueError:
#   print("DOnt enter alnums ,nums , alphabets") 

 # vs 

# while True:
#   while True:
#     sno = input("Enter a Number : ")
#     if sno.isdigit() and int(sno) in range(100,200):
#       break
#     else:
#       print(F"{sno} is invalid student number ")
  
#   while True:
#    sname = input("Enter Student Name : ")
#    words= sname.split()
#    res = True
#    for word in words:
#      if not word.isalpha():
#         res = False
#         break
#    if res :
#     break
#    else:
#     print(f"{sname} is invalid input please enter valid input") 
  
  
#   while True:
#    cm  = int(input("Enter marks in c: "))
#    if cm in range(0,101):
#      break
#    else:
#      print(f"{cm} is invalid marks - try again")
  
#   while True:
#     cppm = int(input("Enter student marks in c++ : "))
#     if cppm in range(0,101):
#       break
#     else:
#       print(f"{cppm} is invalid marks - try again ")
  
#   while True:
#     pym = int(input("Enter students marks in python : "))
#     if pym in range(0,101):
#       break
#     else:
#       print(f"{pym} is invalid marks - try again   ")
  
  
#   totalmarks = cm+cppm+pym
#   percent = totalmarks/300*100
#   if cm<40 or cppm < 40 or pym <40:
#     grade = "FAIL"
#   elif totalmarks in range(250,301):
#     grade = "DISTINCION"
#   elif totalmarks in range(200,250):
#     grade = "FIRST"
#   elif totalmarks in range(150,200):
#     grade = "SECOND"
#   elif totalmarks in range(120,150):
#     grade= "THIRD"
  
  
#   print("----------------------------------------------------")
#   print('\t\t Student Marks Report')
#   print("----------------------------------------------------")
#   print(f"\t Student Number :          {sno} ")
#   print(f"\t Student Name :            {sname}")
#   print(f"\t Student Marks in C :      {cm}")
#   print(f"\t Student Marks in C++ :    {cppm}")
#   print(f"\t Student Marks in Python : {pym}")
#   print(f"\t Total Marks:              {totalmarks}")
#   print(f"\t Percent of Marks :        {percent}")
#   print(f"\t Grade of Student :        {grade}")
  
#   ch = input("Do You want to insert another student Data  - (YES / NO) : ").upper()
#   if ch == "NO":
#     print("Thanks for using this program")
#     break
  




    

# num = int(input("Enter a number "))
# ln = len(str(num))
# Ogval = num
# res= 0
# while num>0:
#   d = num%10
#   sum = d**ln
#   res=  res+sum
#   num= num//10

# if Ogval == res:
#   print("yes")
# else:
#   print("No")




# arr = [1,2,4,5,7,8,3]
# mv = arr[0]
# for val in arr:
#      if val>mv:
#       mv=val
# print(mv)

# arr = [1,2,4,5,7,8,3]
# mv1 = arr[0]
# mv2 = arr[0]

# for i in arr:
#      print(i)
#      if i>mv1:
#           mv1=i
# print("first max : ",mv1)

# for i in arr:
#      if i>mv2 and i!=mv1:
#           mv2=i
# print("Second Max",mv2)


# lst = [1,2,4,5,7,8,3]
# mv1 = lst[0] 
# mv2 = lst[0]  

# for val  in lst:  
#      if val >mv1: 
#           mv2 = mv1
#           mv1= val 
#      elif val > mv2 and val!=mv1: 
#           mv2 = val               
# print(mv2)
     



# lst  = [1,2,4,5,7,8,3]
# mv1 = lst[0]
# mv2 = lst[2]

# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 =  val

# print("Second Max : ",mv2)




# lst  = [1,2,4,5,7,8,3]
# mv1 = lst[0]
# mv2 = lst[0]

# for val in lst:
#      if val > mv1 : 
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 = val
# print("Second Max : ",mv2)

# lst = [10, 20, 15, 2, 23, 90, 80]
# mv1 = lst[0]
# mv2 = lst[0]
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val > mv2  and val!=mv1:
#           mv2 = val
# print("second Max  : ",mv2)


# lst = [-5, -1, -10, -2]
# mv1 = lst[0]
# mv2 = lst[0]
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 =  val
# print("Secong Max : ",mv2)
     


# lst = [99, 1, 2, 3, 98]
# mv1  = 99999999999
# mv2 = 999999999999

# for val in lst:
#      if val<mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val<mv2 and val!=mv1:
#           mv2 = val
# print("Second min   :",mv2)



# lst = [1,2,2,3]
# mv1  = -9999999999
# mv2 = -9999999999

# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 = val
# print("Second max  :",mv2)


# lst = [2,2,2,2,2,2]
# mv1  = -9999999999
# mv2 = -9999999999

# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 = val


# if mv2 == -9999999999:
#      print("all elements are same")
# else:
#      print("Second max  :",mv2)

# lst = [34,54,33,67,2]
# mv1  = -9999999999
# mv2 = -9999999999

# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 = val


# if mv2 == -9999999999:
#      print("all elements are same")
# else:
#      print("Second max  :",mv2)

# lst = [64, 25, 12, 22, 11,33,23,53,33]
# mv1 = -99999999999999
# mv2 = -99999999999999
# mv3 = -99999999999999
# for val in lst:
#      if val>mv1:
#           mv3 = mv2
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1 :
#           mv3 = mv2
#           mv2 = val
#      elif val>mv3 and val!=mv2:
#           mv3 = val
# print("third max: ",mv3)





# lst = [64, 25, 12, 22, 11,33,23,53,33]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
# print(lst)  
        

# lst = [34, -12, 56, 78, -99, 23, 89, 67, -45, 100]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j] = lst[j],lst[i]
# print(lst)

# lst = [-5, -10, -3, -20, -7, -15, -1, -30]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)

# lst = [10, 20, 20, 30, 40, 40, 50, 50, 1,60,  70]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)


# lst = [99, 5, 18, 2, 75, 45, 30, 55, 12, 80]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]  = lst[j],lst[i]

# print(lst)


# lst = [42]
# for i in range(len(lst)):
#      for j in range(i+1 ,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst).


# lst = [7, 7, 7, 7, 7, 7, 7, 7]
# for i in range(len(lst)):
#      for j in range(len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j] = lst[j],lst[i]
# print(lst)

# lst = [32,74,4,2,32,12]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j] = lst[j],lst[i]
# print(lst)


# lst = [38,43,34,54,2,6,76]
# mv1 = -9999999999
# mv2 = -9999999999
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2= val

# print("Second Max : ",mv2)

# lst = [10, 20, 30, 40, 50]
# mv1 = -99999999999
# mv2 = -99999999999
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1  = val
#      elif val>mv2 and  val!=mv1:
#           mv2 = val
# print("Second Max : ",mv2)

# lst = [99, 12, 45, 67, 89, 99]
# mv1 = -9999999
# mv2 = -9999999
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!= mv1:
#           mv2 = val
# print("Second Max : ",mv2)

# lst = [-5, -1, -8, -3, -10]
# mv1 = float("-inf")
# mv2 = float("-inf")
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1= val
#      elif val>mv2 and val!=mv1:
#         mv2 = val

# print("Second Max : ",mv2)

# lst = [99999999, 88888888, 77777777, 66666666, 55555555]
# mv1 = float("-inf")
# mv2 = float("-inf")
# for val in lst:
#      if val>mv1:
#           mv2 = mv1
#           mv1 = val
#      elif val>mv2 and val!=mv1:
#           mv2 =val
# print("Second max ; ",mv2)

# lst = [99999999, 88888888, 77777777, 66666666, 55555555]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j] = lst[j],lst[i]
# print(lst)


# lst = [-5, -1, -8, -3, -10]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)

# # 
# lst = [99, 12, 45, 67, 89, 99]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)


# lst = [34, 7, 23, 32, 5, 62]
# for  i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j] = lst[j],lst[i]
# print(lst)

# lst = [100, 90, 80, 70, 60, 50]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# # print(lst)

# lst = [-10, 20, -30, 40, 0, -50]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)


# lst = [-1, -5, -3, -7, -2, -6]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)

# lst = [15, 42, 15, 60, 42, 90]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)




# print("Second max :",sm)
# print("Second max :",tm)
# mv1 = -99999
# mv2 = -99999
# for val in lst:
#      if val>mv1:
#           mv2=mv1
#           mv1=val
#      elif val>mv2 and val!=mv1:
#           mv2 = val
# print("Second Max  : ",mv2)


# lst = [15, 42, 15, 60, 42, 90]
# for i in range(len(lst)):
#      for j in range(i+1,len(lst)):
#           if lst[i]>lst[j]:
#                lst[i],lst[j]=lst[j],lst[i]
# print(lst)


# n = input("Enter Your Name : ")
# s = ""
# for val in n:
#      if val<="Z" and val>="A":
#           s = s+chr(ord(val)+32)
#      elif val<="z" and val>="a":
#           s = s+chr(ord(val)-32)
# print(s)

# print(ord("c"))
# print(chr(99))




# lst = [15, 42, 15, 60, 42, 90,90]
# lst.sort()
# sm = lst[-lst.count(lst[-1])-1]
# print(sm)

# lst = [15, 42, 15, 60,90, 42, 90,90]
# lst.sort()
# print(lst)
# sm = lst[-lst.count(lst[-1])-1]
# tm = lst[lst.count(lst[-1]) +lst.count(sm)-1]
# print("Second Max  : ",sm)
# print("third max : ",tm)

# lst = [283,53,46,29,26]
# lst.sort(reverse=True)
# print(lst[-1])
# sm = lst[-lst.count(lst[-1])-1]
# tm = lst[-(lst.count(lst[-1])+lst.count(sm))-1]
# print(sm)
# print(tm)


# print(bool([1]))

# print(len({1,2,3,4}))


# def sm(lst):

#  mv1 = -99999
#  mv2 = -99999
#  for val in lst:
#       if val>mv1:
#            mv2 = mv1
#            mv1 = val
#       elif val>mv2 and val!=mv1:
#            mv2 = val
#  return None if mv2 == -99999 else mv2
# res = sm( lst = [10,20,4,45,99])
# print(res)



# print(bin(5))

# print(bin(~5))

