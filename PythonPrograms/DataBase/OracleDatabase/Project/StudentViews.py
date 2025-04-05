import oracledb
def getallrecords():
  con = oracledb.connect("system/1234@localhost/orcl")
  cur = con.cursor()
  sq= "select * from student"
  cur.execute(sq)
  print("-"*50)
  metadata = cur.description
  for col in metadata:
    print(col[0],end="\t\t")
  print()
  print("-"*50)
  records = cur.fetchall()
  for record in records:
    for val in record:
      print(val,end="\t\t")
    print()
  if cur.rowcount==0:
     print("Record Does Not Exist ")


# def getrecord():
#   con = oracledb.connect("system/1234@localhost/orcl")
#   cur = con.cursor()
#   sq= "select * from student"
#   cur.execute(sq)
#   num = int(input("Enter Student Number Whose Data You Want To View : "))
#   print("-"*50)
#   metadata = cur.description
#   for col in metadata:
#     print(col[0],end="\t\t")
#   print()
#   print("-"*50)
#   records = cur.fetchall()
#   for record in records:
#       if record[0]==num:
#          for val in record:
#             print(val,end="\t\t")
#   if cur.rowcount==0:
#      print("Record Does Not Exist ")





def getrecord():
  con = oracledb.connect("system/1234@localhost/orcl")
  cur = con.cursor()
  sq= "select * from student"
  cur.execute(sq)
  num = int(input("Enter Student Number Whose Data You Want To View : "))
  # print("-"*50)
  # metadata = cur.description
  # for col in metadata:
  #   print(col[0],end="\t\t")
  # print()
  # print("-"*50)
  records = cur.fetchall()
  res = False
  for record in records:
      if record[0]==num:
         res = True
  if res:
    print(f"Student Number : {record[0]}")
    print(f"Student Name : {record[1]}")
    print(f"Student Marks {record[2]}")
  else:
    print("Record Does Not Exist ")

        
