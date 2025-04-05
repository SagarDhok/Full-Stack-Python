# ^---------------------------------------------------------------------------------------------
#! checking oracle version
# import oracledb
# print(oracledb.__version__)
# ^----------------------------------------------------------------------------------------------
#!Program for Obtaining Connection from Oracle DB
# * DNS
# import oracledb as orc
# try:
#  conn = orc.connect("system/1234@localhost/orcl")
#  print(type(conn))      #<class 'oracledb.Connection'>
#  print("orcle database conncected successfully ")
# except orc.DatabaseError as db:
#   print("Problem with Oracle :",db)


# *IpAddres
# import oracledb as orc
# try:
#  conn = orc.connect("system/1234@127.0.0.1/orcl")
#  print(type(conn))                                   #<class 'oracledb.Connection'>
#  print("orcle database conncected successfully ")
# except orc.DatabaseError as db:
#   print("Problem with Oracle :",db)

# ^----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Cursor Object Creation
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  print("Connection Created successfully ")
# except oracledb.DatabaseError as db:
#  print("Proble with : ",db)
# else:
#    print("Python Program got connection from Oracle Database")
#    print("Type of conn=", type(conn))
#    print("---------------------")
#    cur = conn.cursor()                         #<class 'oracledb.Cursor'>
#    print("Cursor object created succesfully ")
#    print(type(cur))
# finally :
#   try :
#    print("----------------------------------")
#    print("i am from finnaly block")
#    conn.close()
#    print("PRogram closed succesfully ")
#   except NameError:
#     print("COnnection is not estblished no need to close ")
# ^----------------------------------------------------------------------------------------------
#! Program for creating a table
# * Syntax - 1
# import oracledb  # step-1
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl") #step-2
#  cur = conn.cursor()  #step-3
#  #step - 4
#  ctq = "create table employee(sno number(3) primary key,sname varchar(2) not null,smarks number(5,2))"
#  cur.execute(ctq)
#  print(" Tabel created succesfully ")
# except oracledb.DatabaseError as db:
#  print("Proble with conncting database  : ",db)

# * Syntax - 2
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl").cursor().execute("create table jay(sno number(3) primary key,sname varchar(2) not null,smarks number(5,2))")
#  print(" Tabel created succesfully ")
# except oracledb.DatabaseError as db:
#  print("Proble with conncting database  : ",db)


# *taking dynamic query
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  ctq = input("Enter A Query : " )
#  cur.execute(ctq)
#  print("Table created successfully : ")
# except oracledb.DatabaseError as db:
#  print("Problem in oracle : ",db)
# ^----------------------------------------------------------------------------------------------
#! Program For Adding or Modify New Column
# * Dynmaic Query
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  ctq = input("Enter A Query for altering table : ")
#  cur.execute(ctq)
#  print("Table altered successfully")
# except oracledb.connect as db:
#  print("Proble in oracle : ",db)
# ^----------------------------------------------------------------------------------------------
#! Program inserting data in table
# * syntax-1
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  iq = "insert into employee values(1,'karan',11.44)"
#  cur.execute(iq)
#  conn.commit()
#  print("EMployee record inserted successfully  ")
# except oracledb.DatabaseError as db:
#  print("Problem in Oracle : ",db)

# * syntax-2
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  iq = input("Enter Query for insertion :  ")
#  cur.execute(iq)
#  conn.commit()
#  print("EMployee record inserted successfully  ")
# except oracledb.DatabaseError as db:
#  print("Problem in Oracle : ",db)


# *Dynamic insertion
# import oracledb
# while True:
#  try:
#       con = oracledb.connect("system/1234@localhost/orcl")
#       cur = con.cursor()
#       sno = int(input("Enter Student number : "))
#       sname= input("Enter Name of Student :")
#       smarks = float(input("Enter Marks of Student : "))
#       iq = f"insert into student(sno,sname,smarks) values ({sno},'{sname}',{smarks})"
#       cur.execute(iq)
#       con.commit()
#       print(f"{cur.rowcount}  Student Record Inserted Successfully : ")
#  except oracledb.DatabaseError as db:
#       print("Problem in Oracle : ",db)
#  except ValueError:
#       print("Dont enter alnums,alphabets, symbols  for sno , sname ")
#  ch = input("Do You Want To Enter Another Student Record :  ").lower()
#  if ch == "no" :
#      break
#  if ch not in ["yes","no"]:
#      print("You have Enter Invalid input")
# ^----------------------------------------------------------------------------------------------
#! Program for deleting Query Salary
# import oracledb
# try:
#  con = oracledb.connect("system/1234@localhost/orcl")
#  cur  =con.cursor()
#  dq = "delete from student where sno=50"
#  cur.execute(dq)
#  con.commit()
#  print(f"{cur.rowcount} record is deleted : ")
# except oracledb.DatabaseError as db:
#  print("Problem in oracle ",db)

# * Dynamic Deletion
# import oracledb
# while True:
#  con = oracledb.connect("system/1234@localhost/orcl")
#  try:
#   cur = con.cursor()
#   sno = int(input("Enter Student Number : "))
#   dq = f"delete from student where sno={sno}"
#   cur.execute(dq)
#   con.commit()
#   if cur.rowcount > 0:
#     print(f"{cur.rowcount} record is delted ")
#   else:
#    print("Record does not exist ")
#  except oracledb.DatabaseError as db:
#   print("Problem in oracle : ", db)
#  ch = input("Do you want to delete another student record - (yes / no) : ").lower()
#  if ch == "no":
#   break
#  if ch not in ["yes", "no"]:
#   print("You have Enter Invalid input")
#   break
# ^----------------------------------------------------------------------------------------------
#! program for updating marks of student by 10%
# import oracledb
# try:
#      con = oracledb.connect("system/1234@localhost/orcl")
#      cur = con.cursor()
#      upq = "update student set smarks = smarks*10/100"
#      cur.execute(upq)
#      con.commit()
#      print(f"{cur.rowcount} record updated : ")
# except oracledb.DatabaseError as db:
#      print("Problem in Oracle :",db)

# import oracledb
# try:
#      con = oracledb.connect("system/1234@localhost/orcl")
#      cur = con.cursor()
#      upq = "update student set smarks = smarks + smarks * 10 / 100 where sno = 5"
#      cur.execute(upq)
#      con.commit()
#      print(f"{cur.rowcount} record updated : ")
# except oracledb.DatabaseError as db:
#      print("Problem in Oracle :",db)
# ^----------------------------------------------------------------------------------------------
#! Program for updating studen,Name,Marks based on sno
# import oracledb
# while True:
#  try :
#   con = oracledb.connect("system/1234@localhost/orcl")
#   cur = con.cursor()

#   sno = int(input("Enter Student Number :  "))
#   sname = input("Enter New Name : ")
#   smarks = float(input("Enter New Marks : "))
#   upq= f"update student set  sname = '{sname}',smarks = {smarks} where sno = {sno}"
#   cur.execute(upq)
#   con.commit()
#   if cur.rowcount>0:
#    print(f"{cur.rowcount} Record Updated Successfully ")
#   else:
#    print("Record does not exitst ")
#  except oracledb.DatabaseError as db:
#   print("Problem in Oracle :",db)
#  except ValueError:
#   print("Dont enter alnums , alphabest , symbols for sno , marks")
#  ch = input("Do you want update another another student record - (yes/no) :").lower()
#  if ch == "no":
#   print("Thanks for using this program  ")
#   break
# ^----------------------------------------------------------------------------------------------
#! Program for giving hike to employee sal 10 % whose sal is less than 3 lkah and 20 % whose sal is greater than 3 lakh
# import oracledb
# try :
#    con = oracledb.connect("system/1234@localhost/orcl")
#    cur = con.cursor()
#    upq1="update employee set esal = esal+esal*10/10
#   where esal <3"
#    cur.execute(upq1)
#    row_update1 = cur.rowcount

#    upq2="update employee set esal = esal+esal*20/100  where esal >3 "
#    cur.execute(upq2)
#    row_update2= cur.rowcount
#    con.commit()

#    total_rowcount = row_update1+row_update2
#    if total_rowcount>0:
#     print(f"{cur.rowcount} Record Updated Successfully ")
#    else:
#     print("Record does not exitst ")
# except oracledb.DatabaseError as db:
#    print("Problem in Oracle :",db)
# except ValueError:
#    print("Dont enter alnums , alphabest , symbols for sno , marks")


# ^----------------------------------------------------------------------------------------------
#! Program for reading the records from employee table
# * fetchone()
#* if record is not present it gives none and       # type of record = <class 'tuple'>
# import oracledb as orc
# def selectrecords():
#     try:
#         con = orc.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         sq = "select * from employee"
#         cur.execute(sq)
#         while True:
#          record = cur.fetchone()
#          # print(record,type(record))      # type of record = <class 'tuple'>
#          if record : 
#             for val in record:
#              print(val,end = "\t")
#             print()
#          else:
#              break
#          # *or
#          if record!= None:
#             print(record,type(record))
#          else:
#             break

#     except orc.DatabaseError as db:
#         print("Problem in oracle : ", db)
# selectrecords()
# ^----------------------------------------------------------------------------------------------
#! Program for reading the records from employee table
# * fetchmany()  # tuple in  list,tuple ,value
# import oracledb
# def selectrecords():
#      try:
#        con = oracledb.connect("system/1234@localhost/orcl")
#        cur = con.cursor()
#        sq = "select * from employee"
#        cur.execute(sq)
#        records = cur.fetchmany()     # nothing all records,100 all recors ,0 and -1 no output
#        #print(records,type(records))   #  tuple in <class 'list'>
#        for record in records:
#          #   print(record,type(record))   #<class 'tuple'>
#          for val in record: 
#             print(val,end="\t")
#          print()


#      except oracledb.DatabaseError as db:
#          print("Problem in oracle : ",db)
# selectrecords()
# ^----------------------------------------------------------------------------------------------
#! Program for reading the records from employee table
#* fetchall()
# import oracledb
# def selectrcords():
#  con = oracledb.connect("system/1234@localhost/orcl")
#  cur = con.cursor()
 
#  sq = "select * from employee"
#  cur.execute(sq)
#  records = cur.fetchall()
#  #print(records) #tuple in list
#  for record in records:
#      # print(record)  # tuple
#      for val in record:
#          print(val,end ="\t")
#      print()
# selectrcords()
# ^----------------------------------------------------------------------------------------------
#! Progarm for getting column names from table 
# import oracledb
# try:
#  con = oracledb.connect("system/1234@localhost/orcl")
 
#  cur = con.cursor()
#  sq = "select * from employee"
#  cur.execute(sq)
#  metadeta = cur.description   #[('ENO', <DbType DB_TYPE_NUMBER>, 21, None, 20, 0, False), ('ENAME', <DbType DB_TYPE_VARCHAR>, 20, 20, None, None, False), ('ESAL', <DbType DB_TYPE_NUMBER>, 38, None, 37, 0, False)]
#  for col in metadeta:
#       print(col[0],end="\t\t")
#  print()
# except oracledb.DatabaseError as db:
#    print("Problem in oracle : ",db)
# ^----------------------------------------------------------------------------------------------
#! Program for getting column names from table with records 
# import oracledb
# con = oracledb.connect("system/1234@localhost/orcl")
# cur = con.cursor()
# sq = "select * from employee"
# cur.execute(sq)
# #To get the col names, we use an attribute description present in cursor object
# metadata = cur.description
# for col in metadata:
#  print(col[0],end = "\t")
# print()
# records = cur.fetchall()
# for record in records:
#  for val in record:
#    print(val,end="\t")
#  print()
# ^----------------------------------------------------------------------------------------------
#! Program for getting column names from table with records by order  
# import oracledb
# con = oracledb.connect("system/1234@localhost/orcl")
# cur = con.cursor()
# sq = "select * from employee order by eno desc"
# cur.execute(sq)
# #To get the col names, we use an attribute description present in cursor object
# metadata = cur.description
# for col in metadata:
#  print(col[0],end = "\t")
# print()
# records = cur.fetchall()
# for record in records:
#  for val in record:
#    print(val,end="\t")
#  print()
# ^----------------------------------------------------------------------------------------------