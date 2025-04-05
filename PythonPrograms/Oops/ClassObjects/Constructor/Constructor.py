# ^----------------------------------------------------------------------------------------
#! Default constructor or Parameterless Constructor
# ^----------------------------------------------------------------------------------------
# class Add:
#      def __init__(self):
#           print("I am From Default Construcor")
#           self.a = 10
#           self.b = 20
    


# ao = Add()
# print(ao.__dict__)

# bo = Add()
# print(bo.__dict__)

# co = Add()
# print(co.__dict__)


#* Construcor with dynamic inputs
# class Add:
#      def __init__(self):
#           self.a = int(input("Enter Your Number : " ))
#           self.b = input("Enter Your Name : ")


# ao = Add()
# print(ao.__dict__)

# bo = Add()
# print(bo.__dict__)

# co = Add()
# print(co.__dict__)


# ^----------------------------------------------------------------------------------------
#! Parameterized Constructor 
# class Test:
#      def __init__(self,val1,val2):
#        print("I am from Parameterized Construcor ")
#        self.a = val1
#        self.b = val2       
#        print(f"a ={self.a}\t b = {self.b} ")
#        print("-------------")

# t1 = Test(10,20)
# t1 = Test(100,200)
# t1 = Test(1000,2000)
# ^----------------------------------------------------------------------------------------

# class Test :
#      def __init__(self,k = 10, v = 20):
#           self.a = k
#           self.b = v
#           print(f"a= {self.a} and b = {self.b}")


# t1 = Test()
# t2 = Test("jay",100)
# t3 = Test(101)
# t4 = Test(2000,v="modi")
# t5 = Test(v="modi",k  = "shah")

# t6 = Test (10,a = 20)  #ypeError: Test.__init__() got an unexpected keyword argument 'a'
# t7 = Test(b = 1001,1)  #SyntaxError: positional argument follows keyword argument
# ^----------------------------------------------------------------------------------------
#! Program for printing words at same place using classes and objects 
# class reverseWord:
 
#      def __init__(self):
#           self.line = input("Enter Your line of Text : ")
#           # print("Given Line : ",self.line)

#      def rvrs(self):
#         word = self.line.split()
#         lst = []
#         for i in word:
#             lst.append(i[::-1])
#         else:
#             self.rl = " ".join(lst)
#           #   print("Reverse Line : ",self.rl)

# r = reverseWord()
# print("GIVEN LINE : ",r.line)
# r.rvrs()
# print("Reverse Line : ",r.rl)

# ^----------------------------------------------------------------------------------------
#! Printing list without elements

# class Uniquelst :
#      def __init__(self):
#           self.lst = [i for i in input("Enter values seprated by space : ").split()]
     
#      def dispres(self):
#           self.ul = []
#           for val in self.lst:
#                if val not in self.ul:
#                     self.ul.append(val)
          

# uo = Uniquelst()
# uo.dispres()
# print("Given List : ",uo.lst)
# print("Unique List : ",uo.ul)



# class Uniquelst :
#      def __init__(self):
#           self.lst = [i for i in input("Enter values seprated by space : ").split()]
#           print("Given List : ",self.lst)
     
#      def dispres(self):
#           ul = []
#           for val in self.lst:
#                if val not in ul:
#                     ul.append(val)
#           print("Unique List : ",ul)

# uo = Uniquelst()
# uo.dispres()


# class Uniquelst :
#      def getval(self):
#           self.lst = [i for i in input("Enter values seprated by space : ").split()]
#           print("Given List : ",self.lst)
     
#      def dispres(self):
#           ul = []
#           for val in self.lst:
#                if val not in ul:
#                     ul.append(val)
#           print("Unique List : ",ul)

# uo = Uniquelst()
# uo.getval()
# uo.dispres()


     
# class Res:
#      def getval(self):
#           self.lst = [i for i in input("Enter values seprated by space : ").split()]
#           print("Given List : ",self.lst)

#      @staticmethod
#      def dispres(obj):
#           ul = []
#           for val in obj.lst:
#                if val not in ul:
#                     ul.append(val)
#           print("Unique List : ",ul)


# r = Res()
# r.getval()
# Res.dispres(r)



# class Res:
#      def __init__(self):
#           self.lst = [i for i in input("Enter values seprated by space : ").split()]
#           print("Given List : ",self.lst)

#      @staticmethod
#      def dispres(self):
#           ul = []
#           for val in self.lst:
#                if val not in ul:
#                     ul.append(val)
#           print("Unique List : ",ul)


# r = Res()
# Res.dispres(r)




# class getlst:
#      def __init__(self):
#           self.lst = [i for i in input("Enter values seprated by space : ").split()]
#           print("Given List : ",self.lst)


# class Res:
#      @staticmethod
#      def dispres(self):
#           ul = []
#           for val in self.lst:
#                if val not in ul:
#                     ul.append(val)
#           print("Unique List : ",ul)


# r = getlst()
# Res.dispres(r)



# class getlst:
#      @staticmethod
#      def lst(obj):
#           obj.lst = [i for i in input("Enter values seprated by space : ").split()]
#           print("Given List : ",obj.lst)


# class Res:
#      @staticmethod
#      def dispres(obj):
#           ul = []
#           for val in obj.lst:
#                if val not in ul:
#                     ul.append(val)
#           print("Unique List : ",ul)


# r = getlst()
# r.lst(r)
# Res.dispres(r)
# ^----------------------------------------------------------------------------------------
#! Program for printing factorial 
# class Factorial:
#      def __init__(self):
#       self.n = int(input("Enter Your number : "))

#      def dispres(self) :
#         if self.n<1:
#            print(f'{self.n} Is Invalid Input')
#         else:
#            fact = 1
#            for i in range(1,self.n+1):
#               fact *= i
#            print(f"Factorial of {self.n}= {fact}")
            

# fo= Factorial()
# fo.dispres()
# ^----------------------------------------------------------------------------------------
#! printing lenght of every word present in list using class and object

# class Findilenght:
#      def getlst(self):
#           self.line = input("Enter a line of text : ")
#           self.wordlen()

#      def wordlen(self):
#           words = self.line.split()
#           self.d = {}
#           for i in words:
#                self.d[i] = len(i)
#           # print(self.d)
           
# f = Findilenght()
# f.getlst()
# print(f.d)



# class Findilenght:
#      def getlst(self):
#           self.line = input("Enter a line of text : ")
#           self.lst = [word for word in self.line.split()]

#      def wordlen(self):
#           self.d = {}
#           for i in self.lst:
#                self.d[i] = len(i)
#           # print(self.d)
           
# f = Findilenght()
# f.getlst()
# f.wordlen()
# print(f.d)

# ^----------------------------------------------------------------------------------------
