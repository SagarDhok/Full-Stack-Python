while True:
 enum  = int(input("ENTER EMPLOYE NUMBER : "))
 ename = input("ENTER EMPLOYEE NAME : ")
 esal = int(input("ENTER EMPLOYEE SALATY : "))
 with open("stud3.data","a") as fp:
      fp.write(str(enum)+"\t")
      fp.write(str(ename)+"\t")
      fp.write(str(esal)+"\n")
      print("DATA IS WRITTEN TO THE FILE - VERIFY")
 ch = input("DO YOU WANT TO ENTER ANOTHE EMPLOYEE DATA - (yes/no) : ")
 if ch.lower == "no":
    break