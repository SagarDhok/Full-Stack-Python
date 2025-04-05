
#^----------------------------------------------------------------------------------------
#!Static Method Example -1 
# class Emp:
#  def getempvals(self):
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))


# class student : 
#      def getstudvals(self):
#           self.sno = int(input("Enter Student Number :  "))
#           self.name = input("Enter Student Marks : ")

# class teacher :
#     def getteachervals(self):
#         self.tno = int(input("Enter Teacher Number : "))
#         self.name = input("Enter Teacher Name : ")
#         self.exp = int(input("Enter Teacher Experiance : "))
#         self.sub = input("Enter Teacher Subject : ")

# class Res:
#   @staticmethod
#   def displayvals(obj,objinfo):
#       print(f"{objinfo} Object Information")
#       print("-"*20)
#       for dmn,dmv in obj.__dict__.items():
#           print(dmn,"-->",dmv)
#       print("-"*20)

# eo = Emp()
# so = student()
# to = teacher()
# eo.getempvals()
# print("-"*20)
# so.getstudvals()
# print("-"*20)
# to.getteachervals()
# print("-"*20)

# Res.displayvals(eo,"Employee")
# Res.displayvals(so,"Student")
# Res.displayvals(to,"Teacher")


# class Emp:
#  def getempvals(self,objinfo):
#      print(f"Enter Values for : {objinfo}")
#      print("-"*20)
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))


# # class student : 
# #      def getstudvals(self,objinfo):
# #           print(f"Enter Values for : {objinfo}")
# #           print("-"*20)
# #           self.sno = int(input("Enter Student Number :  "))
# #           self.name = input("Enter Student Marks : ")

# # class teacher :
# #     def getteachervals(self,objinfo):
# #         print(f"Enter Values for : {objinfo}")
# #         print("-"*20)
# #         self.tno = int(input("Enter Teacher Number : "))
# #         self.name = input("Enter Teacher Name : ")
# #         self.exp = int(input("Enter Teacher Experiance : "))
# #         self.sub = input("Enter Teacher Subject : ")

# # class Res:
# #   @staticmethod
# #   def displayvals(obj,objinfo):
# #       print(f"{objinfo} Object Information")
# #       print("-"*20)
# #       for dmn,dmv in obj.__dict__.items():
# #           print(dmn,"-->",dmv)
# #       print("-"*20)

# # eo = Emp()
# # so = student()
# # to = teacher()
# # eo.getempvals("Employee")
# # print("-"*20)
# # so.getstudvals("Student")
# # print("-"*20)
# # to.getteachervals("Teacher")
# # print("-"*20)

# # Res.displayvals(eo,"Employee")
# # Res.displayvals(so,"Student")
# # Res.displayvals(to,"Teacher")
#^----------------------------------------------------------------------------------------

#!Static Method Example -2
# class Emp:
#  def getempvals(self,objinfo):
#      print(f"Enter Values for : {objinfo}")
#      print("-"*20)
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))


# class student : 
#      def getstudvals(self,objinfo):
#           print(f"Enter Values for : {objinfo}")
#           print("-"*20)
#           self.sno = int(input("Enter Student Number :  "))
#           self.name = input("Enter Student Marks : ")

# class teacher :
#     def getteachervals(self,objinfo):
#         print(f"Enter Values for : {objinfo}")
#         print("-"*20)
#         self.tno = int(input("Enter Teacher Number : "))
#         self.name = input("Enter Teacher Name : ")
#         self.exp = int(input("Enter Teacher Experiance : "))
#         self.sub = input("Enter Teacher Subject : ")

# class Res :
#     @staticmethod
#     def Displayobjinfo(obj,objinfno):
#         print(f"Display {objinfno} Object Information")
#         print("-"*20) 
#         for k,v in obj.__dict__.items():
#             print(k,"->",v)
#         print("-"*20)


# e = Emp()
# s = student()
# t = teacher()
# e.getempvals("Employee")
# print("-"*20)
# s.getstudvals("Student")
# print("-"*20)
# t.getteachervals("Teacher")
# print("-"*20)

# r1 = Res()
# r1.Displayobjinfo(e,"Employee")
# r1.Displayobjinfo(s,"Student")
# r1.Displayobjinfo(t,"Teacher")
#^----------------------------------------------------------------------------------------
#!Static Method Example -3
# class Emp:
#  def getempvals(self,objinfo):
#      print(f"Enter Values for : {objinfo}")
#      print("-"*20)
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))

#      print("-"*20)
#      Res.Displayobjinfo(self,"Employee")



# class student : 
#      def getstudvals(self,objinfo):
#           print(f"Enter Values for : {objinfo}")
#           print("-"*20)
#           self.sno = int(input("Enter Student Number :  "))
#           self.name = input("Enter Student Marks : ")
          
#           Res.Displayobjinfo(self,"Student")


# class teacher :
#     def getteachervals(self,objinfo):
#         print(f"Enter Values for : {objinfo}")
#         print("-"*20)
#         self.tno = int(input("Enter Teacher Number : "))
#         self.name = input("Enter Teacher Name : ")
#         self.exp = int(input("Enter Teacher Experiance : "))
#         self.sub = input("Enter Teacher Subject : ")

#         print("-"*20)
#         Res.Displayobjinfo(self,"Teacher")

# class Res :
#     @staticmethod
#     def Displayobjinfo(obj,objinfno):
#         print(f"Display {objinfno} Object Information")
#         print("-"*20) 
#         for k,v in obj.__dict__.items():
#             print(k,"->",v)
#         print("-"*20)


# e = Emp()
# s = student()
# t = teacher()
# e.getempvals("Employee")
# s.getstudvals("Student")
# t.getteachervals("Teacher")

#^----------------------------------------------------------------------------------------
#!Static Method Example -4
# class Emp:
#      def getempvals(self):
#           self.eno = int(input("Enter Student Number : "))
#           self.name = input("Enter Student Name : ")
#           self.sal = int(input("Enter Student Salary : "))


# class Student : 
#      def getstudvales(self):
#           self.sno= int(input("Enter Student Number : "))
#           self.marks = int(input("Enter Student Marks :  ")) 
           

# class Teacher : 
#      def getteachervals(self):
#           self.tname= input("Enter Teacher Name : ")

# class Res : 
#      def dispvals(self,obj,objinfo):
#           # r = Res()
#           Res.result(obj,objinfo)

#      @staticmethod
#      def result(obj,objinfo):
#           print(f"Result of {objinfo}")
#           print("-"*20)

#           for k,v in obj.__dict__.items():
#                print(f"{k} - > {v}")
#           print()
# e = Emp()
# e.getempvals()
# print("-"*20)
# s = Student()
# s.getstudvales()
# print("-"*20)
# t = Teacher()
# t.getteachervals()
# print("-"*20)

# Res().dispvals(e,"Employee")
# Res().dispvals(s,"Student")
# Res().dispvals(t,"Teacher")
#^----------------------------------------------------------------------------------------

# class Emp:
#      def getempvals(self):
#           self.eno = int(input("Enter Student Number : "))
#           self.name = input("Enter Student Name : ")
#           self.sal = int(input("Enter Student Salary : "))
#           Res().dispvals(self,"Employee")


# class Student : 
#      def getstudvales(self):
#           self.sno= int(input("Enter Student Number : "))
#           self.marks = int(input("Enter Student Marks :  ")) 
#           Res().dispvals(self,"Student")
          

# class Teacher : 
#      def getteachervals(self):
#           self.tname= input("Enter Teacher Name : ")
#           Res().dispvals(self,"Teacher")
          
# class Res : 
#      def dispvals(self,obj,objinfo):
#           self.result(obj,objinfo)

#      @staticmethod
#      def result(obj,objinfo):
#           print(f"Result of {objinfo}")
#           print("-"*20)

#           for k,v in obj.__dict__.items():
#                print(f"{k} - > {v}")
#           print()
# e = Emp()
# e.getempvals()
# print("-"*20)
# s = Student()
# s.getstudvales()
# print("-"*20)
# t = Teacher()
# t.getteachervals()
# print("-"*20)

#^----------------------------------------------------------------------------------------

# class Emp:
#      def getempvals(self):
#           self.eno = int(input("Enter Student Number : "))
#           self.name = input("Enter Student Name : ")
#           self.sal = int(input("Enter Student Salary : "))
#           Res().getempvals(self,"Employee")        


# class Student : 
#      def getstudvales(self):
#           self.sno= int(input("Enter Student Number : "))
#           self.marks = int(input("Enter Student Marks :  ")) 
#           Res().getempvals(self,"Student")        


# class Teacher : 
#      def getteachervals(self):
#           self.tname= input("Enter Teacher Name : ")
#           Res().getempvals("Teacherc")        
          
# class Res : 
#      def dispvals(self,obj,objinfo):
#           self.result(obj,objinfo)

#      @staticmethod
#      def result(obj,objinfo):
#           print(f"Result of {objinfo}")
#           print("-"*20)

#           for k,v in obj.__dict__.items():
#                print(f"{k} - > {v}")
#           print()
# e = Emp()
# print("-"*20)
# s = Student()
# print("-"*20)
# t = Teacher()
# print("-"*20)

#^----------------------------------------------------------------------------------------
#!Static Method Example -5
class Emp:
     def getempvals(self):
          self.eno = int(input("Enter Student Number : "))
          self.name = input("Enter Student Name : ")
          self.sal = int(input("Enter Student Salary : "))


class Student : 
     def getstudvales(self):
          self.sno= int(input("Enter Student Number : "))
          self.marks = int(input("Enter Student Marks :  ")) 
           

class Teacher : 
     def getteachervals(self):
          self.tname= input("Enter Teacher Name : ")

class Res : 
     @classmethod
     def dispvals(cls,obj,objinfo):
          cls.result(obj,objinfo)

     @staticmethod
     def result(obj,objinfo):
          print(f"Result of {objinfo}")
          print("-"*20)

          for k,v in obj.__dict__.items():
               print(f"{k} - > {v}")
          print()
e = Emp()
e.getempvals()
print("-"*20)
s = Student()
s.getstudvales()
print("-"*20)
t = Teacher()
t.getteachervals()
print("-"*20)

Res.dispvals(e,"Employee")
Res.dispvals(s,"Student")
Res.dispvals(t,"Teacher")
#^----------------------------------------------------------------------------------------