
#! A) Write a Server Side Program, In such a way that It should accept a Employee Number  from Client Side Program and get other details of employee from Database and give those details to Client Side Program.

import socket,oracledb as orc
s = socket.socket()
s.bind(("localhost",9999))
s.listen(2)
while True:
 try:
      cs,ca =s.accept()
      csdata = cs.recv(1024).decode()
      empno = int(csdata)
 
      #*Write Pdbc code
      con= orc.connect("system/1234@localhost/orcl")
      cur = con.cursor()
      cur.execute("select * from employee where eno = %d"%empno)
      record = cur.fetchone()
      if record!= None:
           s0 ="------------------------------------------------------"
           s1 = f"Employee Number : {record[0]}"
           s2 = f"Employee Name : {record[1]}"
           s3 = f"Employee Salary : {record[2]} "
           s4 = "-------------------------------------------------------"
           res = s0 + "\n" + s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 
           cs.send(res.encode()) 
 
      else:
           cs.send(f"{empno} Record Number Does Not Exist ")
 except ValueError:
     cs.send("Dont Enter Alphabets , Alnums , Symbols ")
 except orc.DatabaseError as db:
      cs.send("Problem in oracle : ",db)
 