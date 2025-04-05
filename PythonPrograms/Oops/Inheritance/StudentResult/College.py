from University import University
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
