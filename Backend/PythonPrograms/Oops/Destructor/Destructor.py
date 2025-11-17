
#^-----------------------------------------------------------------------------------------
# import time
# class Employee:
#      def __init__(self,eno,ename):
#           self.eno = eno
#           self.ename = ename
#           print(f"\t {self.eno}  {self.ename},{id(self)}") 
     
#      def __del__(self):
#           print("gc calls __del__() for deallocating memory space --->",id(self))

# print("Program Execution stated")
# e1 = Employee(10,20)
# e2 = Employee(200,300)
# e3 = Employee(40,50)
# print("Program Execution Ended ")
# print("-------------------------")
# time.sleep(5)
#^-----------------------------------------------------------------------------------------
#*calculating how size of object gets destroyed
# import sys,time
# class Employee:
#      def __init__(self,eno,name):
#           self.eno = eno
#           self.name = name
#           print(f"\t {self.eno} \t {self.name}")


#      def __del__(self):
#           global ms
#           ms = ms-sys.getsizeof(self)
#           print("Destroyed Memory Space : ",ms)
       


# e1 = Employee(10,20)
# e2 = Employee(20,40)
# e3 = Employee(50,60)
# ms = sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
# print("memory space of three : ",ms)
# time.sleep(2)
#^-----------------------------------------------------------------------------------------
#!Forcefully calling destructor by using None
# import time
# class Employee:
#      def __init__(self,eno,name):
#           self.eno = eno 
#           self.name = name
#           print(f"\t {self.eno} {self.name} -> {id(self)}")
     
#      def __del__(self):
#           print("\t Gc calls __del__() Automatically ")
#           print(f"\t {id(self)}")

# print("-"*50)
# e1 = Employee(10,20)
# print("Object gets immediatly destroyed - e1")
# time.sleep(3)
# e1 = None
# print("-"*50)
# e2 = Employee(40,50)
# print("Object gets immediatly destroyed - e2")
# time.sleep(3)
# e2 = None
# print("-"*50)
# e3 = Employee(33,36)
# print("Object gets immediatly destroyed - e3")
# time.sleep(3)
# e3 = None
# print("-"*50)

#^-----------------------------------------------------------------------------------------
#!Forcefully calling destructor by using del
# import time
# class Employee:
#      def __init__(self,eno,name):
#           self.eno = eno 
#           self.name = name
#           print(f"\t {self.eno} {self.name} -> {id(self)}")
     
#      def __del__(self):
#           print("\t Gc calls __del__() Automatically ")
#           print(f"\t {id(self)}")

# print("-"*50)
# e1 = Employee(10,20)
# print("Object gets immediatly destroyed - e1")
# time.sleep(3)
# del e1
# print("-"*50)
# e2 = Employee(40,50)
# print("Object gets immediatly destroyed - e2")
# time.sleep(3)
# del e2
# print("-"*50)
# e3 = Employee(33,36)
# print("Object gets immediatly destroyed - e3")
# time.sleep(3)
# del e3
# print("-"*50)

#^-----------------------------------------------------------------------------------------

# import time
# class Employee:
#      def __init__(self,eno,name):
#           self.eno = eno 
#           self.name = name
#           print(f"\t {self.eno} {self.name} -> {id(self)}")
     
#      def __del__(self):
#           print("\t Gc calls __del__() Automatically ")
#           print(f"\t {id(self)}")

# e1 = Employee(10,20)
# e2 = e1 
# e3 = e1
# print("OG",e1.__dict__,e2.__dict__,e3.__dict__)
# e1.__dict__['name']="Mrbeast"
# print("Updated",e1.__dict__,e2.__dict__,e3.__dict__)
#^-----------------------------------------------------------------------------------------
# import time
# class Employee:
#      def __init__(self,eno,name):
#           self.eno = eno 
#           self.name = name
#           print(f"\t {self.eno} {self.name} -> {id(self)}")
     
#      def __del__(self):
#         	print("GC Calls __del__() for de-allocating the memory space of current object:")

    

# e1 = Employee(10,20)
# e2 = e1  
# e3 = e1

# print("No Longer Interested to use object e1")
# e1 = None
# time.sleep(5)

# print("No Longer Interested to use object e2")
# del e2
# time.sleep(5)
 
# print("No Longer Interested to use object e3")
# del e3
# time.sleep(5)
 
#^-----------------------------------------------------------------------------------------
# import gc
# a = 10
# b = 20
# print("At stating gc is running : ",gc.isenabled())
# c= a+b
# gc.disable()
# print("NOw gc is running : ",gc.isenabled())
# gc.enable()
# print(c)
# print("NOw gc is running : ",gc.isenabled())

#^-----------------------------------------------------------------------------------------