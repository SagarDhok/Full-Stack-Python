
#^--------------------------------------------------------------------------------------------------
#!#Program for Demonstrating the Need of Class Level Data Members
#*Example -1 - direct print
# class Student:pass

# s1 = Student()   #todo - type(s1) <class '__main__.student'>
# s2 = Student()

# s1.sno = 100
# s1.name = "Pankaj"
# s1.marks= 58.54


# s2.sno=200
# s2.name="Travis"
# s2.marks=77.77

# print("Content of S1 Object ")
# print(f"Student Number : {s1.sno}")
# print(f"Student Name : {s1.name}")
# print(f"Student Marks : {s1.marks}")
# print("-"*50)

# print("Content of S1 Object ")
# print(f"Student Number : {s2.sno}")
# print(f"Student Name : {s2.name}")
# print(f"Student Marks : {s2.marks}")

#^--------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
#* Example-2 - printing with __dict__ (magic variable , dunder variale)
# class Student:pass

# s1 = Student()
# s2 = Student()
# print(f"Content of s1 : {s1.__dict__}")
# print(f"Content of s2 : {s2.__dict__} ")
# print(f"Lenght of s1 :  {len(s1.__dict__)}")
# print(f"Lenght of s2 : {len(s1.__dict__)} ")

# #todo - Place Instance Data Members in S1
# s1.sno = 100
# s1.name = "karan"
# s1.marks = 78.33  #todo - Here sno,name and marks are called Instance Data Members

# #todo - Place Instance Data Members in S2
# s2.sno = 877
# s2.name = "jay"
# s2.marks = 88.85

# print("-"*100)
# print(f"Content of s1 : {s1.__dict__}")
# print(f"Content of s2 : {s2.__dict__} ")
# print(f"Lenght of s1 :  {len(s1.__dict__)}")
# print(f"Lenght of s2 : {len(s1.__dict__)} ")
# print("-"*100)

# for val in s1.__dict__:
     # print(val,"-->",s1.__dict__[val])
     # print(val,"-->",s1.__dict__.get(val))
# print("-"*100)

#todo - or
# for k,v in s2.__dict__.items():
     # print(f"{k}-->{v}") 
#todo - or
# for k in s2.__dict__.keys():
#      print(f"{k}-->{s2.__dict__[k]}")
#^--------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
#*Dynamic input
# class student : pass

# s1 = student()
# s2 = student()

# s1.sno = int(input("Enter student number : "))
# s1.sname = input("Enter student name  : ")
# s1.marks = float(input("Enter student Marks  : "))
# print("-"*50)
# print(f"Student no  : {s1.sno}")
# print(f"Student name : {s1.sname}")
# print(f"Student marks  : {s1.marks}")
# print("-"*50)
# print(f"Content of s1  - {s1.__dict__}")
# print("-"*50)

# for k,v in s1.__dict__.items():
#      print(f"{k}-->{v}") 
# print("-"*50)

# s2.sno = int(input("Enter student number : "))
# s2.sname = input("Enter student naem  : ")
# s2.marks = float(input("Enter student Marks  : "))
# print("-"*50)
# print(f"Student no  : {s2.sno}")
# print(f"Student name : {s2.sname}")
# print(f"Student marks  : {s2.marks}")
# print("-"*50)
# print(f"Content of s2  - {s2.__dict__}")
# print("-"*50)
# for val in s2.__dict__:
#      print(val,"-->",s2.__dict__[val])
#^--------------------------------------------------------------------------------------------------