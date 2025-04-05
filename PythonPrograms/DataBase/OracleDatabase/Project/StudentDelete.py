import oracledb
def deleterecord():
  try:
   con = oracledb.connect("system/1234@localhost/orcl")
   cur = con.cursor()
   sno = int(input("Enter Student Number : "))
   dq = f"delete from student where sno = {sno}"
   cur.execute(dq)
   con.commit()
   if cur.rowcount>0:
    print(f"{cur.rowcount} Student Record  Deleted ")
   else:
     print("Record Does Not Exist ")
  except oracledb.DatabaseError as db:
    print("Problem in Oracle : ",db)
  except ValueError:
    print("Dont Enter Alphabets, Alnums, Symbols As Student Number ")
