import oracledb
from College import College
class Student(College):
     def getsd(self):
       self.sno = int(input("Enter Student Number : "))
       self.sname = input("Enter Student Name : ") 
       self.scrs = input("Enter Student Course Name : ") 
       self.getcd()
       self.getud()
        
     def dispsd(self):
          print("-"*20)
          print("Studet Details")
          print("-"*20)
          print(f" Student Number : {self.sno}")
          print(f" Student Name : {self.sname}")
          print(f" Student Course : {self.scrs}")
          self.dispcd()
          self.dispud()
          self.savedata()

     def savedata(self):
          
         
          try:
            con= oracledb.connect("system/1234@localhost/orcl")
            cur= con.cursor()
            iq = "insert into studres values(%d,'%s','%s','%s','%s','%s','%s')"
            cur.execute(iq %(self.sno, self.sname,self.scrs,self.cname,self.cloc,self.uname,self.uloc))
            con.commit()
            print(f"{cur.rowcount} Student Record Inserted Successfully ")
          except oracledb.DatabaseError as db:
              print("Problem in Oracle : ",db)  
