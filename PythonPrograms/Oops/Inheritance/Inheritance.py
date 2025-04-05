
#^-----------------------------------------------------------------------------------------
#! Non-Ineritance 
# class c1 :
#      def getval1(self):
#           print("This is c1 - getval1()")

# class c2:
#      def getval2(self):
#           print("This is c2 - getval2()")
# class c3:
#      def getval3(self):
#           print("This is c3- getval3()")
     

# o1 = c1()
# o2 = c2()
# o3 = c3()
# o1.getval1()
# o2.getval2()
# o3.getval3()
#^-----------------------------------------------------------------------------------------
#! Inheritance 
# class c1 :
#      def getval1(self):
#           print("This is c1 - getval1()")

# class c2(c1):
#      def getval2(self):
#           print("This is c2 - getval2()")
# o1 = c1()
# o1.getval1()
# # o1.getval2()                 #* AttributeError 

# o2 = c2()
# o2.getval1()
# o2.getval2()
#^-----------------------------------------------------------------------------------------
#! Mulilevel Inheritance 
# class c1 :
#      def getval1(self):
#           print("This is c1 - getval1()")

# class c2(c1):
#      def getval2(self):
#           print("This is c2 - getval2()")
# class c3(c2):
#        def getval3(self):
#           print("This is c3 - getval2()")



# o3 = c3()
# o3.getval1()
# o3.getval2()
# o3.getval3()
#^-----------------------------------------------------------------------------------------
#! Addition Of Two Number Using Inheritance 
#* Syntax -1 :
# class A:
#      def getvalA(self):
#        self.a = int(input("Enter First Value : "))

# class B(A):
#      def getvalB(self):
#          self.b = int(input("Enter Second Value : "))
#      def addop(self):
#         self.c = self.a + self.b
#         print(f"First Value is : {self.a} ")
#         print(f"Second Value is : {self.b}")
#         print(f"Sum : ({self.a},{self.b}) = {self.c}")

# o = B()
# o.getvalA()   #* if we dont call anymethod then we get attributeError cause getvalA and GetvalB providing Value to operation C
# o.getvalB()
# o.addop()



#* Syntax -2 :
# class A:
#      def getvalA(self):
#        self.a = int(input("Enter First Value : "))

# class B(A):
#      def getvalB(self):
#          self.b = int(input("Enter Second Value : "))
#      def addop(self):
#         self.getvalA()
#         self.getvalB()
#         self.c = self.a + self.b
#         print(f"First Value is : {self.a} ")
#         print(f"Second Value is : {self.b}")
#         print(f"Sum : ({self.a},{self.b}) = {self.c}")

# o = B()
# o.addop()
#^-----------------------------------------------------------------------------------------
#! Inheriting GrantParent Property to parent and parent to child
#* Syntax - 1
# class grandparent:
#      def getgpp(self):
#           self.gpp = float(input("Enter GrandParent Property : "))

# class parent(grandparent):
#      def getp(self):
#           self.p = float(input("Enter Parent Property : "))
# class Child(parent):
#      def getcp(self):
#           self.cp = float(input("Enter Child Property "))
#      def disppropty(self):
#           print(f"GrantParent Property : {self.gpp}")
#           print(f"Parent Property : {self.p}")
#           print(f"Child Property : {self.cp}  ")
#           self.tp = self.gpp+self.p+self.cp
#           print(f"Total Property : ({self.gpp},{self.p},{self.cp}) = {self.tp} ")

# co = Child()
# co.getgpp()
# co.getp()
# co.getcp()
# co.disppropty()


#! Inheriting GrantParent Property to parent and parent to child
#* Syntax - 2
# class grandparent:
#      def getgpp(self):
#           self.gpp = float(input("Enter GrandParent Property : "))

# class parent:
#      def getp(self):
#           self.p = float(input("Enter Parent Property : "))
# class Child(parent,grandparent):
#      def getcp(self):
#           self.cp = float(input("Enter Child Property "))

#      def disppropty(self):
#           self.getgpp()
#           self.getp()
#           self.getcp()
#           print(f"GrantParent Property : {self.gpp}")
#           print(f"Parent Property : {self.p}")
#           print(f"Child Property : {self.cp}  ")
#           self.tp = self.gpp+self.p+self.cp
#           print(f"Total Property : ({self.gpp},{self.p},{self.cp}) = {self.tp} ")

# co = Child()

# co.disppropty()
#^-----------------------------------------------------------------------------------------
# #! Inheriting GrantParent Property to parent and parent to child
# #* Using same Data Member 
# #* dictonary remembers only latest key if there are duplicate keys

# class GrandParent:
#      def getgpp(self):
#           self.p = float(input("Enter GrandParent Proprty : "))
#           return self.p
# class Parent(GrandParent):
#      def getp(self):
#           self.p = float(input("Enter Parent Property : "))
#           return self.p
# class Child(Parent):
#      def getcp(self):
#           self.p = float(input("Enter child property : "))
#           return self.p 
#      def display(self,x,y,z):
#              print(f"GrantParent Property : {x}")
#              print(f"Parent Property : {y}")
#              print(f"Child Property : {z}  ")
#              tp = x+y+z
#              print(f"Total Property : ({x},{y},{z}) = {tp} ")



# co = Child()
# x = co.getgpp()
# y = co.getp()
# z = co.getcp()
# co.display(x,y,z)

#! Inheriting GrantParent Property to parent and parent to child
#* Using same Data Member 
#* dictonary remembers only latest key if there are duplicate keys
#* Syntax-2
# class GrandParent:
#      def getgpp(self):
#           self.p = float(input("Enter GrandParent Proprty : "))
#           return self.p
# class Parent(GrandParent):
#      def getp(self):
#           self.p = float(input("Enter Parent Property : "))
#           return self.p
# class Child(Parent):
#      def getcp(self):
#           self.p = float(input("Enter child property : "))
#           return self.p 
#      def display(self):
#              x = co.getgpp()
#              y = co.getp()
#              z = co.getcp()
#              print(f"GrantParent Property : {x}")
#              print(f"Parent Property : {y}")
#              print(f"Child Property : {z}  ")
#              tp = x+y+z
#              print(f"Total Property : ({x},{y},{z}) = {tp} ")



# co = Child()

# co.display()

#^-----------------------------------------------------------------------------------------
#!Saving Student Result in Dabase Using Inheritance
#* Syntax - 1
# import oracledb
# class University:
#      def getud(self):
#           self.uname = input("Enter University Name : ")
#           self.uloc = input("Enter University Location : ")

#      def dispud(self):
#           print("-"*20)
#           print("University Details")
#           print("-"*20)
#           print(f" University Name : {self.uname} ")
#           print(f" University Location : {self.uloc}")
     
# class College(University):
#      def getcd(self):
#           self.cname = input("Enter College Name : ")
#           self.cloc = input("Enter College Location : ")

#      def dispcd(self):
#           print("-"*20)
#           print("College Details")
#           print("-"*20)
#           print(f" College Name : {self.cname}")
#           print(f" College Location : {self.cloc}")

# class Student(College):
#      def getsd(self):
#        self.sno = int(input("Enter Student Number : "))
#        self.sname = input("Enter Student Name : ") 
#        self.scrs = input("Enter Student Course Name : ") 
        
#      def dispsd(self):
#           print("-"*20)
#           print("Studet Details")
#           print("-"*20)
     
#           print(f" Student Number : {self.sno}")
#           print(f" Student Name : {self.sname}")
#           print(f" Student Course : {self.scrs}")
#      def savedata(self):
#           try:
#             con= oracledb.connect("system/1234@localhost/orcl")
#             cur= con.cursor()
#             iq = f"insert into studres(sno,name,crs,cname,cloc,uname,uloc) values({self.sno},'{self.sname}','{self.scrs}','{self.cname}','{self.cloc}',{self.uname},{self.cloc})"
#             cur.execute(iq)
#             con.commit()
#             print(f"{cur.rowcount} Student Record Inserted Successfully ")
#           except oracledb.DatabaseError as db:
#               print("Problem in Oracle : ",db)  

# so = Student()
# so.getsd()
# so.getcd()
# so.getud()
# so.dispsd()
# so.dispcd()
# so.dispud()
# so.savedata()



#* Syntax - 2
# import oracledb
# class University:
#      def getud(self):
#           self.uname = input("Enter University Name : ")
#           self.uloc = input("Enter University Location : ")

#      def dispud(self):
#           print("-"*20)
#           print("University Details")
#           print("-"*20)
#           print(f" University Name : {self.uname} ")
#           print(f" University Location : {self.uloc}")
     
# class College(University):
#      def getcd(self):
#           self.cname = input("Enter College Name : ")
#           self.cloc = input("Enter College Location : ")

#      def dispcd(self):
#           print("-"*20)
#           print("College Details")
#           print("-"*20)
#           print(f" College Name : {self.cname}")
#           print(f" College Location : {self.cloc}")

# class Student(College):
#      def getsd(self):
#        self.sno = int(input("Enter Student Number : "))
#        self.sname = input("Enter Student Name : ") 
#        self.scrs = input("Enter Student Course Name : ") 
        
#      def dispsd(self):
#           print("-"*20)
#           print("Studet Details")
#           print("-"*20)
     
#           print(f" Student Number : {self.sno}")
#           print(f" Student Name : {self.sname}")
#           print(f" Student Course : {self.scrs}")
#      def savedata(self):
#           try:
#             con= oracledb.connect("system/1234@localhost/orcl")
#             cur= con.cursor()
#             iq = "insert into studres values(%d,'%s','%s','%s','%s','%s','%s')"
#             cur.execute(iq %(self.sno, self.sname,self.scrs,self.cname,self.cloc,self.uname,self.uloc))
#             con.commit()
#             print(f"{cur.rowcount} Student Record Inserted Successfully ")
#           except oracledb.DatabaseError as db:
#               print("Problem in Oracle : ",db)  

# so = Student()
# so.getsd()
# so.getcd()
# so.getud()
# so.dispsd()
# so.dispcd()
# so.dispud()
# so.savedata()

#^-----------------------------------------------------------------------------------------
# ! Student Res
class University:
     def getud(self):
          self.uname = input("Enter University Name : ")
          self.uloc = input("Enter University Location : ")

     def dispud(self):
          print("-"*20)
          print("University Details")
          print("-"*20)
          print(f" University Name : {self.uname} ")
          print(f" University Location : {self.uloc}")
     
class College(University):
     def getcd(self):
          self.cname = input("Enter College Name : ")
          self.cloc = input("Enter College Location : ")

     def dispcd(self):
          print("-"*20)
          print("College Details")
          print("-"*20)
          print(f" College Name : {self.cname}")
          print(f" College Location : {self.cloc}")

class Student(College):
     def getsd(self):
       self.sno = int(input("Enter Student Number : "))
       self.sname = input("Enter Student Name : ") 
       self.scrs = input("Enter Student Course Name : ") 
        
     def dispsd(self):
          so.getsd()
          so.getcd()
          so.getud()
         
          print("-"*20)
          print("Studet Details")
          print("-"*20)
     
          print(f" Student Number : {self.sno}")
          print(f" Student Name : {self.sname}")
          print(f" Student Course : {self.scrs}")
          so.dispcd()
          so.dispud()
so = Student()

so.dispsd()
#^-----------------------------------------------------------------------------------------

