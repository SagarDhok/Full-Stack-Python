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
