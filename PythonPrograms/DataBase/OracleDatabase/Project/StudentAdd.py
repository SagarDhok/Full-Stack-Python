import oracledb    
def addstudentrecord():
 try:
  con = oracledb.connect("system/1234@localhost/orcl")
  cur = con.cursor()
  sno = int(input("Enter Student Number : "))
  sname = input("Enter Student Name : ")
  smarks = float(input("Enter Student Marks : "))
  iq = f"insert into student (sno,sname,smarks) values({sno},'{sname}',{smarks})"
  cur.execute(iq)
  con.commit()
  print(f"{cur.rowcount} Student Record Inseted")
 except oracledb.DatabaseError as db:
  print("Problem in Oracle : ",db)
 except ValueError :
  print("Dont Enter Alphabets, Alnums, Symbols as Student Number Or Student Marks ")


