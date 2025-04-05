
#^ --------------------------------------------------------------------------------------
#! Class Level Example -1
# class Employee:
#      @classmethod
#      def getvalues(cls):
#           cls.Compname = input("Enter Company Name : ")  #Employee.Compname =input("Enter Company Name : ")
#           cls.city= input("Enter City Name : ")          #Employee.city= input("Enter City Name : ")
# #here Compname and city is class level data member 

# # #*We can access class level method by classname and object name also 
# # #*And also with cls but it can be only access inside the class only
# Employee.getvalues()
# print("Company Name : ",Employee.Compname)  #Accessing Class Level Data Members w.r.t Class Name
# print("City Name : ",Employee.city)         #Accessing Class Level Data Members w.r.t Class Name

# print("-----------------------------------")

# eo = Employee()                           # object creation
# eo.getvalues()                            # Calling Class Level method w.r.t 
# # print("Content of eo: ",eo.__dict__)    # class level data member are not part of eo object 
# print("Company Name : ",eo.Compname)      # Accessing Class Level Data Members w.r.t Object Name
# print("City Name : ",eo.city)             # Accessing Class Level Data Members w.r.t Object Name
1

# class student :
#      def getvalues(cls):
#           student.classname = int(input("Enter Your Class Name : ")) #cls.classname = int(input("Enter Your Class Name : "))
#           student.schoolname= input("Enter Your School Name : ")  #input("Enter Your School Name : ")

# student.getvalues()   
# print(f"Class Name : {student.classname}")    # Accessing Class Level Data Members w.r.t Class Name
# print(f"School Name : {student.schoolname}")  #  Accessing Class Level Data Members w.r.t Class Name

# print("----------------")
# so = student()
# so.getvalues()
# print(f"Class Name : {so.classname}")         # Accessing Class Level Data Members w.r.t Object Name
# print(f"School Name : {so.schoolname}")       #Accessing Class Level Data Members w.r.t Object Name



# class teacher :
#      @classmethod
#      def getvalues(cls):
#           cls.tno = input("Enter Teacher Name : ")
#           cls.sal = int(input("Enter Teacher Salary : "))

# # to = teacher()
# # to.getvalues()
# # print(to.tno)
# # print(to.sal)

# teacher.getvalues()
# print(teacher.tno)
# print(teacher.sal)
#^ ---------------------------------------------------------------------------------------
#!Class Level Example -2
# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = input("Enter Compnay Name : ")  ##or Employee.compname
#      @classmethod
#      def getcity(cls):
#           cls.city = input("Enter City Name : ") ##or Employee.city


# Employee.getcomp()
# Employee.getcity()
# print("Compnany Name : ",Employee.compname)
# print("City Name : ",Employee.city)

#^ ---------------------------------------------------------------------------------------
#! Class Level Example - 3
# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = input("Enter Your Compnay Name : ")  ##or Employee.compname
#           cls.getcity()  # OR Employee.getcity()
#      @classmethod
#      def getcity(cls):
#           cls.city = input("Enter Your City Name : ")  ##or Employee.city
# # Employee.getcomp()
# # print(Employee.compname)
# # print(Employee.city)


# eo = Employee()
# eo.getcomp()
# print(eo.compname)
# print(eo.city)


#& je function pahile call karin tycha i/o pahile disin

# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = input("Enter Your Company Name : ")
#      @classmethod
#      def getcity(cls):
#           # Employee.getcomp()   
#           cls.city = input("Enter Your City Name : ")
#           cls.getcomp()

# # eo = Employee()
# # eo.getcity()
# # print(eo.compname)
# # print(eo.city)

# Employee.getcity()
# print(Employee.compname)
# print(Employee.city)

#^ ---------------------------------------------------------------------------------------
#! class Level Example - 4
# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = "ibm"

#           cls.city()     #or Employee.city() 
     
#      @classmethod
#      def city(cls):
#           cls.city  = "Hydrabad"


#      def getempdetails(self):
#           self.eno = int(input("Enter Employee Number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = float(input("Enter Employee Salary : "))
#           self.displayempdetails()

#      def displayempdetails(self):
#           print(f"Employee Number : {self.eno}")
#           print(f"Employee Name : {self.name} ")
#           print(f"Employee Salary : {self.sal} ")
#           print(f"Company Name : {Employee.compname}")
#           print(f"City Name : {Employee.city}")

# Employee.getcomp()
# eo = Employee()
# eo.getempdetails()

     

     
# class Employee:
#      @classmethod
#      def getcomp(cls):
#           cls.compname = "ibm"

#           cls.city()     #or Employee.city() 
     
#      @classmethod
#      def city(cls):
          
#           cls.city  = "Hydrabad"

#      @classmethod
#      def display(cls):
#           print(cls.compname)
#           print(cls.city)


#      def getempdetails(self):
#           self.eno = int(input("Enter Employee Number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = float(input("Enter Employee Salary : "))
#           self.displayempdetails()


#      def displayempdetails(self):
#           Employee.display()
#           print(f"Employee Number : {self.eno}")
#           print(f"Employee Name : {self.name} ")
#           print(f"Employee Salary : {self.sal} ")

# Employee.getcomp()
# eo = Employee()
# eo.getempdetails()
#^ ---------------------------------------------------------------------------------------
#! class Level Example - 5
# class Employee:
#      @classmethod
#      def  getcomp(cls):
#           cls.compname = "IBM"

#           cls.getcity()
     
#      @classmethod
#      def getcity(cls):
#           cls.city = "Hydrabad"

#      def getempdetails(self):
#           self.eno= int(input("Enter Employee Number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = float(input("Enter Salary Of Employee : "))
#           self.displayempdetails()

#      def displayempdetails(self):
#           Employee.getcomp()
#           print("Company Name : ",Employee.compname)
#           print("City Name : ",Employee.city)
#           print("Employee Number : ",self.eno)
#           print("Employee Name : ",self.name)
#           print("Employee Salary : ",self.sal)

# Employee.getcomp()
# eo= Employee()
# eo.getempdetails()
# Employee().getempdetails()


# class Employee:
#      @classmethod
#      def  getcomp(cls):
#           cls.compname = "IBM"

     
#      @classmethod
#      def getcity(cls):
#           cls.city = "Hydrabad"

#      def getempdetails(self):
#           self.eno= int(input("Enter Employee Number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = float(input("Enter Salary Of Employee : "))
#           self.displayempdetails()

#      def displayempdetails(self):
#           Employee.getcomp()
#           Employee.getcity()
#           print("Company Name : ",Employee.compname)
#           print("City Name : ",Employee.city)
#           print("Employee Number : ",self.eno)
#           print("Employee Name : ",self.name)
#           print("Employee Salary : ",self.sal)

# eo= Employee()
# eo.getempdetails()
# Employee().getempdetails()

#^ ---------------------------------------------------------------------------------------
#! class Level Example - 6
# class Employee:
#      @classmethod
#      def getcompname(cls):
#           cls.compname = "Ibm"
#      @classmethod
#      def getcity(cls):
#           cls.city ="Hydrabad"
#           # Employee().empdetails()
#           # eo = Employee()
#           # eo.empdetails()
    
#      def empdetails(self):
#           self.eno = int(input("Enter Employee Number : "))
#           self.name = input("Enter Employee Name : ")
#           self.sal = float(input("Enter Employee Salary : "))
#           self.displayvalues()
#           # Employee.displayvalues()

#      def displayvalues(self):
#           Employee.getcompname()
#           print("Company Name : ",Employee.compname)
#           print("City : ",Employee.city)
#           print("Employee Number : ",self.eno)
#           print("Employee Name : ",self.name)
#           print("Employee Salary : ",self.sal)

# Employee().getcity()