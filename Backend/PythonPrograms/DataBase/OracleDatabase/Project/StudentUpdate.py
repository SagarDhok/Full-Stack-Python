# import oracledb

# def updaterecord():
#   try:
#    con = oracledb.connect("system/1234@localhost/orcl")
#    cur = con.cursor()
#    sno = int(input("Enter Student Number : "))
#    sname = input("Enter New Student Name : ")
#    smarks = float(input("Enter Neww Student Marks : "))
#    uq = f"update student set sname = '{sname}',smarks = {smarks} where sno = {sno}"
#    cur.execute(uq)
#    if cur.rowcount>0:
#     print(f"{cur.rowcount} Student Record Updated Successfully ")
#    else:
#      print("Record Does Not Exist ")
#    con.commit()
#   except oracledb.DatabaseError as db:
#       print("Problem in Oracle : ",db)
#   except ValueError:
#       print("Dont Enter Alphabets, Alnums, Symbols As Student Number And Student Marks ")

