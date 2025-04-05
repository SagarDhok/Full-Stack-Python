import oracledb  
def searchrecord():
  con = oracledb.connect("system/1234@localhost/orcl")
  cur = con.cursor()
  sq= "select * from student"
  cur.execute(sq)
  num = int(input("Enter Student Number Whose Data You Want To Search : "))
  print("-"*50)
  metadata = cur.description
  for col in metadata:
    print(col[0],end="\t\t")
  print()
  print("-"*50)
  records = cur.fetchall()
  for record in records:
      if record[0]==num:
         for val in record:
            print(val,end="\t\t")
