from StudMenu import Menu
from StudAdd import StudAdd
from StudViews import getallrecords,getrecord
from StudDelete import studdelete
while True:
 Menu()
 try:
  ch = int(input("Enter Your Choice : "))
  match(ch):
   case 1 :StudAdd()
   case 2 :getallrecords()
   case 3 :getrecord()
   case 4 :studdelete()
   case 5 :pass
   case 6 :pass
   case 7 :
    print("Thanks for using this program : ")
    break
   case _:
    print("Your Selection of operation is Wrong")
 except ValueError:
  print("Dont Enter Alphabets,Alnums,Symbols..")