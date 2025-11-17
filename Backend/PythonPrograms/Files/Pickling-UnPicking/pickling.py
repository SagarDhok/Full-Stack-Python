
#! WPP WHICH WILL READ STUDENTS DATA FROM KEYBOARD AND SAVE IT AS A RECORD
def pfun():
 import pickle
 while True:
  with open("Ex1.pick","ab") as fp:
       snum = int(input("Enter student number : "))
       sname = input("Enter student name : ")
       smarks = int(input("Enter students marks : "))
  
       lst = []
       lst.append(snum)
       lst.append(sname)
       lst.append(smarks)
        
       pickle.dump(lst,fp)

  ch = input("Do you want to enter another student data - (yes or no ): ")
  if ch.lower() == "no":
   print("Data added successfully ")
   break
       
pfun() 