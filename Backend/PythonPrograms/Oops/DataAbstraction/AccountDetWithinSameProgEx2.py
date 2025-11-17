
class Account:
     def  __init__(self):
          self.__acno = 100
          self.name = 'Karan'
          self.__bal = 1000
          self.__pin = 1234
          self.bname = "SBI"
     def __displavals(self):
          print(self.__acno)  
          print(self.name)  
          print(self.__bal)  
          print(self.__pin)  
          print(self.bname)  
     def showval(self):
          self.__displavals()


ao = Account()  #-- not possible 

# print(ao.acno)  
# print(ao.name)  
# print(ao.bal)  
# print(ao.pin)  
# print(ao.bname) 
ao.showval()