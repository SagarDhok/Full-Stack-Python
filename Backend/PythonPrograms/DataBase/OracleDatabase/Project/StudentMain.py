from StudentMenu import menu
from StudentAdd import addstudentrecord
from StudentViews import getallrecords,getrecord
from StudentDelete import deleterecord
from StudentUpdate import updaterecord
from StudentSearch import searchrecord
import oracledb
while True:
 menu()
 ch = int(input("Enter Your Choice : ")) 
 match(ch):
      case 1:
           addstudentrecord()
      case 2:
           getallrecords() 
      case 3:
            getrecord() 
      case 4: 
           deleterecord()
  
      case 5:
           updaterecord()
      case 6:
           searchrecord()
      case 7:
           print("Thanks For Using This Program ")
           break
      case _:
           print("Your Selection Of Operation is Wrong - Try again")
     


