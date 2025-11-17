
#!A) Write a Server Side Program, In such a way that It should accept a Employee Number  from Client Side Program and 
# ! get other details of employee from Database and give those details to Client Side Program.


import socket,oracledb as orc
s = socket.socket()
s.bind(("127.0.0.1","9999"))
s.listen(2)
print("Ssp is ready for Connetionn ")
while True:
     try:
          cs,ca = s.accept()
          csdata = cs.recv(1024).decode()
          print(f"Employee Number at server side : {csdata}")
          empno = int(csdata)
          
          #*Write Pdbc code 
          con = orc.connect("system/1234@localhost/orcl")
          cur = con.cursor()
          cur.execute("select * from employee where empno=%d "%empno)
          record = cur.fetchone()
          if record !=None:
                  cs.send(str(record).encode())
          else:
                  cs.send(f"{empno} Record Number Does not exist ") 
     except ValueError:
            cs.send("Dont Enter Alphabets ,Alnums,Symbols - Try Again ".encode())
     except orc.DatabaseError as DB:
            print("Problem in oracle : ",orc)