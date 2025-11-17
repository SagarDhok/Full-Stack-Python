


#! For all
#*alter table student modify smarks real not null  # without () use database direct databse name
#*alter table student add smarks real not null  # without ()
# import mysql.connector 
# try:
#  con = mysql.connector.connect(host = "localhost",user  ="root", passwd = "1234",database = "9ambatch")
#  cur = con.cursor()
#  q = input("Enter you query : ")
#  cur.execute(q)
#  con.commit()
#  print("Done")
# except mysql.connector.DatabaseError as db:
#   print("problem in mysql : ",db)
#^-------------------------------------------------------------------------------------------------
#!Program for connecting python program for mysql
#*DNS
# import mysql.connector # type: ignore
# try:
#  con = mysql.connector.connect(host = "localhost",
#                                user = "root",
#                                passwd="1234"
#                                )
#  print("Python Program got connection from MySql")
# except mysql.connector.DatabaseError as db:
#  print("Problem in Mysql : ",db)

#*IpAdress
# import mysql.connector 
# try:
#  con = mysql.connector.connect(host = "localhost",
#                                user = "root",
#                                passwd="1234"
#                                )
# #  print(type(con))  <class 'mysql.connector.connection.MySQLConnection'>
#  print("Python Program got connection from MySql")
# except mysql.connector.DatabaseError as db:
#  print("Problem in Mysql : ",db)
#^-------------------------------------------------------------------------------------------------
#!Program for creating an object of cursor
# import mysql.connector 
# try:
#  con = mysql.connector.connect(host = "localhost",
#                                user ="root",
#                                passwd = "1234"
#                                )
 
#  print("Python program got  connection from mysql ")
#  cur = con.cursor()
#  print(type(cur))
#  print("Cursor object created")
# except mysql.connector.DatabaseError as db:
#  print("Problem in mysql : ",db)
#^-------------------------------------------------------------------------------------------------
#! Progarm for creating database 9ambatch 
# import mysql.connector 
# try:
#  con = mysql.connector.connect(host = "localhost",
#                                user = "root",
#                                passwd = "1234"
#                              )
#  cur = con.cursor() 
#  dq = "create database jay"
#  cur.execute(dq)
 
#  print(f"{cur.rowcount} Database created successfully")
# except mysql.connector.DatabaseError as db:
#  print("Problem in mysql : ",db)
#^-------------------------------------------------------------------------------------------------
#!Progarm for creating table in mysql:
# import mysql.connector 
# try:
#  con = mysql.connector.connect(host = "localhost",user = "root",passwd = "1234",database ="9ambatch")
#  cur= con.cursor()
#  cq = "create table student(sno int(2) primary key ,sname varchar(10) not null , smarks real not null)"
#  cur.execute(cq)
#  print(f"{cur.rowcount} table created successfully ")
# except mysql.connector.DatabaseError  as db:
#  print("Problem in mysql :",db)
#^-------------------------------------------------------------------------------------------------
# #! Program for inserting data in table
# import mysql.connector 
# try:
#  con = mysql.connector.connect(host = "localhost",user = "root",passwd = "1234",database= "9ambatch")
#  cur = con.cursor()
#  sno = int(input("Enter Student number : "))
#  sname = input("Enter student name :")
#  smarks = float(input("Enter studnet marks "))
#  iq = f"insert into student (sno,sname,smarks) values({sno},'{sname}',{smarks})"
#  cur.execute(iq)
#  con.commit()
#  print(f"{cur.rowcount} record inserted successfully : ")
# except mysql.connector.DatabaseError as db:
#  print("Problem in mysql : ",db)
# except ValueError:
#  print("Dont enter alnums, alphabets , symbols for sno,smarks")
   
#^-------------------------------------------------------------------------------------------------
#! Program for updating name and marks from sno
# import mysql.connector as mys
# try:
#  con = mys.connect(host = "localhost",user = "root",passwd = "1234",database  = "9ambatch")
#  cur = con.cursor()
#  sno = int(input("Enter Student Number : "))
#  sname = input("Enter Student Name : ")
#  smarks = float(input("Enter Student Marsk : "))
#  uq = f"update student set sname = '{sname}',smarks = {smarks} where sno = {sno}"
#  cur.execute(uq)
#  con.commit()
#  if cur.rowcount>0:
#   print(f"{cur.rowcount} is updated successfully  : ")
#  else:
#   print("Record does not exist ")
# except mys.DatabaseError as db:
#  print("problem in mysql : ",db)
# except ValueError:
#  print("Dont enter alnums, alphabets , symbols for sno,smarks")
#^-------------------------------------------------------------------------------------------------
#! Program for deleting one record from table
# import mysql.connector as msq
# try:
#  con = msq.connect(host = "localhost",user = "root",passwd = "1234",database="9ambatch")
#  cur= con.cursor()
#  sno= int(input("Enter Studeent Number : "))
#  dq= "delete from student where sno = %d"%sno
#  cur.execute(dq)
#  con.commit()
#  if cur.rowcount>0:
#   print(f"{cur.rowcount} deleted successfully ")
#  else:
#   print("Record does not exist ")
# except msq.DatabaseError as db:
#  print("problem in mysql : ",db)
# except ValueError:
#  print("Dont enter alnums, alphabets , symbols for sno")
#^-------------------------------------------------------------------------------------------------
#! #Program for Getting the Records from any Table along with Col Names
# import mysql.connector as mys
# con = mys.connect(host = "localhost",user = "root",passwd  = "1234",database = "9ambatch")
# cur = con.cursor()
# sq = "select * from student"
# cur.execute(sq)
# metadata = cur.description
# print("-------------------------------")
# for col in metadata:
#      print(col[0], end = "\t")
# print()
# print("--------------------------------")
# records = cur.fetchall()
# for record in records:
#      for val in record:
#           print(val,end="\t")
#      print()
# print("--------------------------------")
#^--------------------------------------------------------------------------------------------------