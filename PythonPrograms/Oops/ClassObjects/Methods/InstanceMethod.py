#^-------------------------------------------------------------------------------------------
#! program for Reading and Displaying the Deatils students by using Classes and Objects
#*Example-1
# class student:
#      def readstudent(self):
#           print(f"Current Object Reference In Instance Method : {id(self)}")

# s1 = student()
# print(f"Content of S1 before reading : {s1._dict_}")
# print(f"Memory id of S1 in Main Program : {id(s1)}")
# s1.readstudent()                   #todo calling instace method
# print("-----------------")
# s2 = student()
# print(f"Content of S2 before reading : {s2._dict_}")
# print(f"Memory address of S1 in Main Program : {id(s2)} ")
# s2.readstudent()       #todo calling instace method     
#^-------------------------------------------------------------------------------------------
#! program for Reading and Displaying the Deatils students by using Classes and Objects
#*Example-2
# class student:
#     def readstudent(self,objinfo):
#      print(f"Enter {objinfo} Student Data : ")
#      self.sno = int(input("Enter Student Number : "))
#      self.sname = input("Enter Student Name : ")
#      self.marks = float(input("Enter Student Marks "))

# s1 = student()
# s2 = student()

# s1.readstudent("First")
# s2.readstudent("Second")


# print("Display the content of S1")
# for dmn,dmv in s1._dict_.items():
#    print(dmn,"-->",dmv)

# print("---------------")

# print("Display the content of S1")
# for dmn in s2._dict_:
#    print(dmn,"-->",s2._dict_[dmn])
#^-------------------------------------------------------------------------------------------
#! program for Reading and Displaying the Deatils students by using Classes and Objects
#*Example-3
# class student:
#      def readstudent(self,objinfo):
#           print(f"Enter {objinfo} Student Data : ")
#           self.sno = int(input("Enter Student Number : "))
#           self.sname = input("Enter Student Name : ")
#           self.marks = float(input("Enter Student Marks : "))
#      def displaydata(self,objinfo):
#           print(f"display {objinfo} Student Data")
#           print(f"Student Number : {self.sno}")
#           print(f"Studen Name : {self.sname}")
#           print(f"Student Marks  : {self.marks}")

# s1 = student()
# s2 = student()
# #read the Student Object Data by using Instance Methods
# s1.readstudent("First") # calling Instance Method
# s2.readstudent("Second") # calling Instance Method
# print("--------------")
# s1.displaydata("First") 
# s2.displaydata("Second") 
#^-------------------------------------------------------------------------------------------
#! Program for Reading and Displaying the Deatils students by using Classes and Objects
#*Example-4
# class student:
#     def readstudent(self,objinfo):
#      print(f"Enter {objinfo} Student Data : ")
#      self.sno = int(input("Enter Student Number : "))
#      self.sname = input("Enter Student Name : ")
#      self.marks = float(input("Enter Student Marks "))
#     def displaydata(self,objinfo):
#         print(f"display {objinfo} Student Data")
#         for dmn,dmv in self._dict_.items():
#                print(dmn,"-->",dmv)


# s1 = student()
# s2 = student()
# #read the Student Object Data by using Instance Methods
# s1.readstudent("First") # calling Instance Method
# s2.readstudent("Second") # calling Instance Method
# print("--------------")
# s1.displaydata("First") 
# s2.displaydata("Second") 
#^-------------------------------------------------------------------------------------------
#! Program for Reading and Displaying the Deatils students by using Classes and Objects
#*Example-5
#*Syntax-1

# class student:
#      def readdata(self,objinfo):
#           print("-"*30)
#           print(f"Enter {objinfo} Student Data ")
#           print("-"*30)
#           self.sno = int(input("Enter Student Number : "))
#           self.sname = input("Enter Student Name : ")
#           self.marks = float(input("Enter Student Marks : "))
#           self.displaydata(objinfo)

#      def displaydata(self,objinfo):
#           print("-"*30)
#           print(f"Display {objinfo} Student Data")
#           print("-"*30)
#           print(f"Student Number : {self.sno}")
#           print(f"Student Name : {self.sname}")
#           print(f"Student Marks : {self.marks}")
          
# s1 = student()
# s2 = student()

# s1.readdata("First")
# s2.readdata("Second")



# class student:
#      def readdata(self,objinfo):
#           print("-"*30)
#           print(f"Enter {objinfo} Student Data ")
#           print("-"*30)
#           self.sno = int(input("Enter Student Number : "))
#           self.sname = input("Enter Student Name : ")
#           self.marks = float(input("Enter Student Marks : "))

#      def displaydata(self,objinfo):
#           print("-"*30)
#           print(f"Display {objinfo} Student Data")
#           print("-"*30)
#           print(f"Student Number : {self.sno}")
#           print(f"Student Name : {self.sname}")
#           print(f"Student Marks : {self.marks}")
          
#           self.displaydata(objinfo)
# s1 = student()
# s2 = student()

# s1.readdata("First")
# s2.readdata("Second")



#*Syntax-1
# class student:
#      def readdata(self,objinfo):
#           print("-"*30)
#           print(f"Enter {objinfo} Student Data ")
#           print("-"*30)
#           self.sno = int(input("Enter Student Number : "))
#           self.sname = input("Enter Student Name : ")
#           self.marks = float(input("Enter Student Marks : "))
#           self.displaydata(objinfo)

#      def displaydata(self,objinfo):
#           print("-"*30)
#           print(f"Display {objinfo} Student Data")
#           print("-"*30)
#           for k,v in self._dict_.items():
#                print(f"{k}->{v}")
          
# s1 = student()
# s2 = student()

# s1.readdata("First")
# s2.readdata("Second")


#^-------------------------------------------------------------------------------------------
#! Program for Finding Sum of Two Numbers by using Classes and Objects
#*Example - 6
# class sum:pass

# s = sum()
# s.a = int(input("Enter First Value : "))
# s.b = int(input("Enter Seacond Value : "))
# s.c= s.a + s.b
# print(f"Sum : ({s.a},{s.b})= {s.c}")
# print(s._dict_)
#^-------------------------------------------------------------------------------------------
#! Program for Finding Sum of Two Numbers by using Classes and Objects
#*Example - 7
# class Sumop : 
#    def readvalues(self):
#      self.a = int(input("Enter First Value : "))
#      self.b = int(input("Enter Second Value : "))
#    def addvalues(self):
#       self.c = self.a + self.b
#    def displayvalues(self):
#       print(f"First value : {self.a}")
#       print(f"Second Value : {self.b}")
#       print(f"Sum :  ({self.a},{self.b}) = {self.c}")

# s = Sumop()
# s.readvalues()
# s.processvalues()
# s.displayvalues()
#^-------------------------------------------------------------------------------------------
#! Program for Finding Sum of Two Numbers by using Classes and Objects
#*Example - 8
# class sumop:
#      def readval(self):
#           self.a = int(input("Enter First value : "))
#           self.b = int(input("Enter Second value : "))
#      def addval(self):
#           self.c = self.a + self.b
#      def display(self):
#           self.readval()
#           self.addval()
#           print(f"First value : {self.a}") 
#           print(f"Second value : {self.b}") 
#           print(f"Sum : ({self.a},{self.b}) =  {self.c}") 
     
# s = sumop()
# s.display()


# class sumop:
#      def readval(self):
#           self.a = int(input("Enter First value : "))
#           self.b = int(input("Enter Second value : "))
#      def addval(self):
#           self.readval()
#           self.c = self.a + self.b
#      def display(self):
#           self.addval()
#           print(f"First value : {self.a}") 
#           print(f"Second value : {self.b}") 
#           print(f"Sum : ({self.a},{self.b}) =  {self.c}") 

# s = sumop()
# s.display()
#^-------------------------------------------------------------------------------------------
#! Program for Finding Sum of Two Numbers by using Classes and Objects
#* Local Variable
#*Example - 9
#*Syntax - 1

# class sumop:
#      def readval(self):
#           self.a = int(input("Enter First Value : "))
#           self.b= int(input("Enter Second Value : "))
#      def addval(self):
#            c = self.a + self.b
#            return c
#      def displayval(self):
#           self.readval()
#           kvr =  self.addval()
#           print(f"First value : {self.a}")
#           print(f"Second value : {self.b}")
#           print(f"Sum:  ({self.a},{self.b}) =  {kvr}")

# s = sumop()
# s.displayval()


#*Syntax - 2
# class sumop:
#      def readval(self):
#           self.a = int(input("Enter First Value : "))
#           self.b= int(input("Enter Second Value : "))
#      def addval(self):
#            c = self.a + self.b
#            return c
#      def displayval(self):
#           self.readval()
          
#           print(f"First value : {self.a}")
#           print(f"Second value : {self.b}")
#           print(f"Sum:  ({self.a},{self.b}) =  {self.addval()}")

# s = sumop()
# s.displayval()

#*referance
# def sumop():
#      a = int(input(1))
#      b = int(input(2))
#      c = a+b
#      return c
# print(sumop())


#^-------------------------------------------------------------------------------------------
#! Program for Cal Fctorial of a Number
#*Example - 10
#*syntax-1
# import sys
# class Factorial:
#      def readval(self):
#        try:
#           self.n = int(input("Enter Value : "))
#        except ValueError:
#           print("Dont Enter Alnums, Alphabets , Symbols ")
#           sys.exit()
#      def calfact(self):
#         if self.n < 0 :
#            return f"{self.n} Is invalid Input"
#         else:
#            fact = 1
#            for i in range(1,self.n+1):
#               fact*=i
#            return fact
#      def dispfact(self,res):
#         print(f"factorial of {self.n} is {res} ")
        
     

#*syntax-2
# fo= Factorial()
# fo.readval()
# res = fo.calfact()
# fo.dispfact(res)





#*syntax-3
# import sys
# class Factorial:
#      def readval(self):
#        try:
#           self.n = int(input("Enter Value : "))
#        except ValueError:
#           print("Dont Enter Alnums, Alphabets , Symbols ")
#           sys.exit()
#      def calfact(self):
#         if self.n < 0 :
#            return f"{self.n} Is invalid Input"
#         else:
#            fact = 1
#            for i in range(1,self.n+1):
#               fact*=i
#            return fact
#      def dispfact(self,res):
#         print(f"factorial of {self.n} is {res} ")
        
     

# fo= Factorial()
# fo.readval()
# fo.dispfact( fo.calfact())


#*syntax-4
# import sys
# class Factorial:
#      def readval(self):
#        try:
#           self.n = int(input("Enter Value : "))
#        except ValueError:
#           print("Dont Enter Alnums, Alphabets , Symbols ")
#           sys.exit()
#      def calfact(self):
#         fo.readval()
        
#         if self.n < 0 :
#            return f"{self.n} Is invalid Input"
#         else:
#            fact = 1
#            for i in range(1,self.n+1):
#               fact*=i
#            return fact
#      def dispfact(self,res):
#         print(f"factorial of {self.n} is {res} ")
        
     

# fo= Factorial()
# fo.dispfact( fo.calfact())




#*syntax-5
# import sys
# class Factorial:
#      def readval(self):
#       try:
#        self.n = int(input("Enter A Number : "))
#       except ValueError:
#          print("Dont Enter ALnums,Alphabets ,Symbols")
#          sys.exit()

#      def calfact(self):
#         if self.n<0:
#            print(f"{self.n} Is Invalid input")
#         else:
#            self.fact = 1
#            for i in range(1,self.n+1):
#               self.fact = self.fact*i
#      def displayfact(self):
#         print(f"Factorial of {self.n} = {self.fact}")

# fo = Factorial()
# fo.readval()
# fo.calfact()
# fo.displayfact()


#*syntax-6
# import sys
# class Factorial:
#      def readval(self):
#       try:
#        self.n = int(input("Enter A Number : "))
#       except ValueError:
#          print("Dont Enter ALnums,Alphabets ,Symbols")
#          sys.exit()

#      def calfact(self):
#         if self.n<0:
#            print(f"{self.n} Is Invalid input")
#         else:
#            self.fact = 1
#            for i in range(1,self.n+1):
#               self.fact = self.fact*i
#      def displayfact(self):
#         fo.readval()
#         fo.calfact()
#         print(f"Factorial of {self.n} = {self.fact}")

# fo = Factorial()

# fo.displayfact()





#*syntax-6
# import sys
# class Factorial:
#      def readval(self):
#       try:
#        self.n = int(input("Enter A Number : "))
#       except ValueError:
#          print("Dont Enter ALnums,Alphabets ,Symbols")
#          sys.exit()

#      def calfact(self):
#         fo.readval()
#         if self.n<0:
#            print(f"{self.n} Is Invalid input")
#         else:
#            self.fact = 1
#            for i in range(1,self.n+1):
#               self.fact = self.fact*i
#      def displayfact(self):
#         fo.calfact()
#         print(f"Factorial of {self.n} = {self.fact}")

# fo = Factorial()

# fo.displayfact()
#^-------------------------------------------------------------------------------------------
#! Program for Cal Fctorial of a Number
#*Exaple - 11
#*syntax-1
# class Factorial : 

#    def readval(self):
#      try:
#       self.n = int(input("Enter A Number : "))
#      except ValueError:
#        print("Dont Enter Alnums , Alphabets , Symbols ")
#      else:
#        res = self.calfact() 
#        self.dispfact(res)

    
#    def calfact(self):
#      if self.n<0:
#        return f"{self.n} is invalid input"
#      else:
#        fact = 1
#        for i in range(1,self.n+1):
#          fact*=i
#        return fact
#    def dispfact(self,res):
#      print(f"Factorial of {self.n} = {res}")
         
   
# fo=  Factorial()
# fo.readval()


#*syntax-2
# class Factorial : 

#    def readval(self):
#      try:
#       self.n = int(input("Enter A Number : "))
#      except ValueError:
#        print("Dont Enter Alnums , Alphabets , Symbols ")
#      else:
        
#        self.dispfact(self.calfact())

    
#    def calfact(self):
#      if self.n<0:
#        return f"{self.n} is invalid input"
#      else:
#        fact = 1
#        for i in range(1,self.n+1):
#          fact*=i
#        return fact
#    def dispfact(self,res):
#      print(f"Factorial of {self.n} = {res}")
         
   
# fo=  Factorial()
# fo.readval()



#^----------------------------------------------------------------------------------------
#!Program for Reading Student Data from KBD and Save them in Student Table by using Classes and Obejcts
#*Example-11
#*Syntax-1
# import sys
# import oracledb  # noqa: F401
# sys.path.append("E:\\FULL STACK PYTHON\\PythonPrograms\\ExceptionHandling\\NameValidation")
# from NameExecpt import InvalidNameError, ZerolenError,SpaceError
# from NameValidation import validation

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")


#      def dispstud(self):
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = f"insert into student (sno,name,marks) values({self.sno},'{self.name}',{self.marks})"
#         cur.execute(iq)
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()
# s.dispstud()
# s.savestud()

#*Syntax-2
# import sys
# import oracledb  # noqa: F401
# sys.path.append("E:\\FULL STACK PYTHON\\PythonPrograms\\ExceptionHandling\\NameValidation")
# from NameExecpt import InvalidNameError, ZerolenError,SpaceError
# from NameValidation import validation

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")
#       else:
#          s.dispstud()


#      def dispstud(self):
#           s.savestud()
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = "insert into student values(%d,'%s',%f)"
#         cur.execute(iq%(self.sno,self.name,self.marks))
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()

#*Syntax-3
# import sys
# import oracledb  # noqa: F401
# sys.path.append("E:\\FULL STACK PYTHON\\PythonPrograms\\ExceptionHandling\\NameValidation")
# from NameExecpt import InvalidNameError, ZerolenError,SpaceError
# from NameValidation import validation

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")
#       else:
#          s.dispstud()
#          s.savestud()


#      def dispstud(self):
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = "insert into student values(%d,'%s',%f)"
#         cur.execute(iq%(self.sno,self.name,self.marks))
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()
#^----------------------------------------------------------------------------------------
#*Syntax-1
# import oracledb  # noqa: F401


# class InvalidNameError(Exception):pass
# class ZerolenError(BaseException):pass
# class SpaceError(Exception):pass
# class NameValidation:
#     def validation(self,name): # Instance Method
#         if(len(name)==0):
#             raise ZerolenError
#         elif(name.isspace()):
#             raise SpaceError
#         else:
#                 words = name.split()
#                 res = True
#                 for word in words:
#                     if (not word.isalpha()):
#                         res = False
#                         break
#                 if (res):
#                    return name
#                 else:
#                    raise InvalidNameError
# no = NameValidation()       

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = no.validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")


#      def dispstud(self):
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = f"insert into student (sno,name,marks) values({self.sno},'{self.name}',{self.marks})"
#         cur.execute(iq)
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()
# s.dispstud()
# s.savestud()


#*Syntax-2
# import oracledb  # noqa: F401


# class InvalidNameError(Exception):pass
# class ZerolenError(BaseException):pass
# class SpaceError(Exception):pass
# class NameValidation:
#     def validation(self,name): # Instance Method
#         if(len(name)==0):
#             raise ZerolenError
#         elif(name.isspace()):
#             raise SpaceError
#         else:
#                 words = name.split()
#                 res = True
#                 for word in words:
#                     if (not word.isalpha()):
#                         res = False
#                         break
#                 if (res):
#                    return name
#                 else:
#                    raise InvalidNameError
# NameValidation()       

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = NameValidation().validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")
#       else :
#         self.dispstud()
#         self.savestud()


#      def dispstud(self):
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = f"insert into student (sno,name,marks) values({self.sno},'{self.name}',{self.marks})"
#         cur.execute(iq)
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)
    

# s = student()
# s.readstud()

#^----------------------------------------------------------------------------------------

# import mysql.connector  # noqa: F401


# class InvalidNameError(Exception):pass
# class ZerolenError(BaseException):pass
# class SpaceError(Exception):pass
# class NameValidation:
#     def validation(self,name): # Instance Method
#         if(len(name)==0):
#             raise ZerolenError
#         elif(name.isspace()):
#             raise SpaceError
#         else:
#                 words = name.split()
#                 res = True
#                 for word in words:
#                     if (not word.isalpha()):
#                         res = False
#                         break
#                 if (res):
#                    return name
#                 else:
#                    raise InvalidNameError
# NameValidation()       

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = NameValidation().validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")


#      def dispstud(self):
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = mysql.connector.connect(host = "localhost",
#                                       user = "root",
#                                       passwd= "1234" ,
#                                       database = "9ambatch"
#                                       )
#         cur = con.cursor()
#         iq = f"insert into student (sno,name,marks) values({self.sno},'{self.name}',{self.marks})"
#         cur.execute(iq)
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except mysql.connector.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()
# s.dispstud()
# s.savestud()
#^----------------------------------------------------------------------------------------