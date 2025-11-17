class Employee:
     def readvalues(self,eno,name,sal):
          self.eno = eno
          self.name = name
          self.sal = sal
     def dispvals(self):
          print(f"{self.eno} \t {self.name} \t {self.sal} ")