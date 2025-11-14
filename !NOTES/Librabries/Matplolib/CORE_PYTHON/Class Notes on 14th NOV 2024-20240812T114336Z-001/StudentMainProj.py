#StudentMainProj.py<---------------Main Program
from StudentMenu import menu
from StudentAdd import savestuddata
from StudentViews import getallrecords, getrecord
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                savestuddata()
            case 2:
                getallrecords()
            case 3:
                getrecord()
            case 4: pass
            case 5: pass
            case 6: pass
            case 7:
                print("Thx for using this App")
                break
            case _:
                print("Ur Selection of Operation wrong-Try again")
    except ValueError:
        print("Don't Enter alnums,strs and symbols for Choice--try again")

