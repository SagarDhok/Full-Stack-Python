
#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Occurence of Dead Lock() 
#! DeadLockFunEx1.py
# import threading,time
# def multable(n):
#      if n<=0:
#           print(f"{threading.current_thread().name} - {n} is invalid input")
#      for i in range(1,11):
#           print(f"{threading.current_thread().name} - {n} X {i} = {n*i}")
#           time.sleep(0.25)
#      print()

# t1 = threading.Thread(target=multable , args=(10,))
# t2 = threading.Thread(target=multable , args=(15,))
# t3 = threading.Thread(target=multable , args=(19,))
# t4 = threading.Thread(target=multable , args=(7,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()

#^------------------------------------------------------------------------------------------------
#!Program for Demonstrating the Occurence of Dead Lock() 
#! DeadLockOopsEx1.py
# import threading,time
# class Table:
#  def multable(self,n):
#       if n<=0:
#            print(f"{threading.current_thread().name} - {n} is invalid input")
#       for i in range(1,11):
#            print(f"{threading.current_thread().name} - {n} X {i} = {n*i}")
#            time.sleep(0.25)
#       print()
 
# t1 = threading.Thread(target=Table().multable , args=(10,))
# t2 = threading.Thread(target=Table().multable , args=(17,))
# t3 = threading.Thread(target=Table().multable , args=(19,))
# t4 = threading.Thread(target=Table().multable , args=(4,))
 
# t1.start()
# t2.start()
# t3.start()
# t4.start()
#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#! SynchFunEx1.py

# import threading,time
# def multable(n):
#      #* Get the lock
#      L.acquire()
#      if n<=0:
#           print(f"{threading.current_thread().name} - {n} is invalid input")
#           print()
#      else:
#       for i in range(1,11):
#            print(f"{threading.current_thread().name} - {n} X {i} = {n*i}")
#            time.sleep(0.25)
#       print()
#      #* release the lock
#      L.release()

# #* Create an object of Lock class of threading
# L = threading.Lock()
# t1 = threading.Thread(target=multable , args=(10,))
# t2 = threading.Thread(target=multable , args=(-2,))
# t3 = threading.Thread(target=multable , args=(19,))
# t4 = threading.Thread(target=multable , args=(7,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()

#! WITH DIRECTLY L
# import threading,time
# def multable(n):
#    with L:
    
#      if n<=0:
#           print(f"{threading.current_thread().name} - {n} is invalid input")
#           print()
#      else:
#       for i in range(1,11):
#            print(f"{threading.current_thread().name} - {n} X {i} = {n*i}")
#            time.sleep(0.25)

# #* Create an object of Lock class of threading
# L = threading.Lock()
# t1 = threading.Thread(target=multable , args=(10,))
# t2 = threading.Thread(target=multable , args=(-2,))
# t3 = threading.Thread(target=multable , args=(19,))
# t4 = threading.Thread(target=multable , args=(7,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()

#^-----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#! SynchOopsEx1.py
# import threading,time
# class Table:
#  def multable(self,n):
#       #* Get the lock
#       L.acquire()
#       if n<=0:
#            print(f"{threading.current_thread().name} - {n} is invalid input")
#            print()
#       else:
#        for i in range(1,11):
#             print(f"{threading.current_thread().name} - {n} X {i} = {n*i}")
#             time.sleep(0.25)
#        print()
#       #* release the lock
#       L.release()
 
# #* Create an object of Lock class of threading
# L = threading.Lock()
# t1 = threading.Thread(target=Table().multable , args=(10,))
# t2 = threading.Thread(target=Table().multable , args=(-2,))
# t3 = threading.Thread(target=Table().multable , args=(19,))
# t4 = threading.Thread(target=Table().multable , args=(7,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()

#! WITH DIRECTLY L
# import threading,time
# class Table:
#  def multable(self,n):
#      with L:
#       if n<=0:
#            print(f"{threading.current_thread().name} - {n} is invalid input")
#            print()
#       else:
#        for i in range(1,11):
#             print(f"{threading.current_thread().name} - {n} X {i} = {n*i}")
#             time.sleep(0.25)
#        print()
     
 
# #* Create an object of Lock class of threading
# L = threading.Lock()
# t1 = threading.Thread(target=Table().multable , args=(10,))
# t2 = threading.Thread(target=Table().multable , args=(-2,))
# t3 = threading.Thread(target=Table().multable , args=(19,))
# t4 = threading.Thread(target=Table().multable , args=(7,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
#^-----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#! SynchOopsEx2.py

# import threading,time
# class Table:
#  def __init__(self,n):
#     self.n = n
#  def multable(self):
#       #* Get the lock
#       L.acquire()
#       if self.n<=0:
#            print(f"{threading.current_thread().name} - {self.n} is invalid input")
#            print()
#       else:
#        for i in range(1,11):
#             print(f"{threading.current_thread().name} - {self.n} X {i} = {self.n*i}")
#             time.sleep(0.25)
#        print()
#       #* release the lock
#       L.release()
 
# #* Create an object of Lock class of threading
# L = threading.Lock()
# t1 = threading.Thread(target=Table(10).multable)
# t2 = threading.Thread(target=Table(20).multable)
# t3 = threading.Thread(target=Table(-4).multable)
# t4 = threading.Thread(target=Table(2).multable)

# t1.start()
# t2.start()
# t3.start()
# t4.start()

#^-----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#! SynchOopsEx3.py

# import threading,time
# class Table:
#  L = threading.Lock()
#  def __init__(self,n):
#     self.n = n
#  def multable(self):
#       #* Get the lock
#       Table.L.acquire()
#       if self.n<=0:
#            print(f"{threading.current_thread().name} - {self.n} is invalid input")
#            print()
#       else:
#        for i in range(1,11):
#             print(f"{threading.current_thread().name} - {self.n} X {i} = {self.n*i}")
#             time.sleep(0.25)
#        print()
#       #* release the lock
#       Table.L.release()
 
# #* Create an object of Lock class of threading
# L = threading.Lock()
# t1 = threading.Thread(target=Table(10).multable)
# t2 = threading.Thread(target=Table(20).multable)
# t3 = threading.Thread(target=Table(-4).multable)
# t4 = threading.Thread(target=Table(2).multable)

# t1.start()
# t2.start()
# t3.start()
# t4.start()


#^-----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#! SynchOopsEx4.py


# import threading,time
# class Table:
#  @classmethod
#  def getlock(cls):
#   cls.L = threading.Lock()
#  def __init__(self,n):
#     self.n = n
#  def multable(self):
#       #* Get the lock
#       Table.L.acquire()
#       if self.n<=0:
#            print(f"{threading.current_thread().name} - {self.n} is invalid input")
#            print()
#       else:
#        for i in range(1,11):
#             print(f"{threading.current_thread().name} - {self.n} X {i} = {self.n*i}")
#             time.sleep(0.25)
#        print()
#       #* release the lock
#       Table.L.release()
 
# #* Create an object of Lock class of threading
# Table.getlock()
# t1 = threading.Thread(target=Table(10).multable)
# t2 = threading.Thread(target=Table(20).multable)
# t3 = threading.Thread(target=Table(-4).multable)
# t4 = threading.Thread(target=Table(2).multable)
# t5 = threading.Thread(target=Table(0).multable)

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
#^-----------------------------------------------------------------------------------------------
#! ReservationAppFun.py
# import threading,time
# def reservation(nos):
#      lockobj.acquire()
#      print("----------------------------------------------------------------------------")

#      global totseats
#      if nos>totseats:
#           print(f"Dear Customer : '{threading.current_thread().name}', {nos} - Seats are not available Better Luck Next Time")
#           time.sleep(2)
#      else:
#           totseats = totseats-nos
#           print(f"Dear Passenger :'{threading.current_thread().name}', {nos} - Seats are reseved Happy journy ")
#           print("Available Seats : ",totseats)
#           if totseats==0:
#                print("Bus Is Full")
#           time.sleep(2)
#      print("----------------------------------------------------------------------------")
#      lockobj.release()


# lockobj = threading.Lock()
# totseats = 10
# t1 = threading.Thread(target=reservation,args = (10,))
# t1.name = "Karan"
# t2 = threading.Thread(target=reservation,args = (7,))
# t2.name = "Jay"
# t3 = threading.Thread(target=reservation,args = (5,))
# t3.name = "Parth"
# t4 = threading.Thread(target=reservation,args = (2,))
# t4.name = "Nilesh"

# t1.start()
# t2.start()
# t3.start()
# t4.start()
#^-----------------------------------------------------------------------------------------------
#! SynchBankWithDrawFunEx.py
# import threading,time
# def checkclear(camnt):
#      lockobj.acquire()
#      global vmamt
#      print("----------------------------------------------------------------------------")
#      if camnt>vmamt:
#           print(f"Dear Customer : '{threading.current_thread().name} - Your Check Of INR :{camnt}' Is Bounced - Contact Source")
#           time.sleep(2)
#      else:
#           vmamt= vmamt-camnt
#           print(f"Dear Cusomer : '{threading.current_thread().name}' Your Check Of INR {camnt} Is Cleared ")
#           time.sleep(2)
#           print(f"Avaiable Balence Of Vm Account is : {vmamt}")
#           print("----------------------------------------------------------------------------")
#      lockobj.release()
# lockobj= threading.Lock()
# vmamt = 2000
# t1 = threading.Thread(target=checkclear,args=(2000,))
# t1.name = "karan"
# t2 = threading.Thread(target=checkclear,args=(7300,))
# t2.name = "ravi"
# t3 = threading.Thread(target=checkclear,args = (400,))
# t3.name = "parth"
# t4 = threading.Thread(target=checkclear,args = (6060,))
# t4.name = "jay"

# t1.start()
# t2.start()
# t3.start()
# t4.start()


#^-----------------------------------------------------------------------------------------------
#! SynchBankWithDrawOopsEx.py
import threading,time

class Borrower:
     @classmethod
     def getlock(cls):
         cls.L = threading.Lock()
         Borrower.getvm()

     @classmethod
     def getvm(cls):
          cls.vm = 1000


     def __init__(self,camt):
          self.camt = camt
    
     def checkclear(self):
          Borrower.L.acquire()
          print("----------------------------------------------------------------------------")

          if self.camt > Borrower.vm:
               print(f"Dear Customer {threading.current_thread().name} - Your Check Of INR : {self.camt} Is Bounced Contact Support")
               time.sleep(2)
          else:
               Borrower.vm = Borrower.vm - self.camt
               print(f"Dear Customer : {threading.current_thread().name} - Your Check Of INR {self.camt} Is Cleared")
               time.sleep(2)
               print(f"Available Balence : {Borrower.vm}")
          print("----------------------------------------------------------------------------")

          Borrower.L.release()


Borrower.getlock()
t1 = threading.Thread(target=Borrower(1000).checkclear)
t1.name = "karan"
t2 = threading.Thread(target=Borrower(20000).checkclear)
t2.name = "parth"
t3 = threading.Thread(target=Borrower(200).checkclear)
t3.name = "jay"
t4 = threading.Thread(target=Borrower(4000).checkclear)
t4.name = "rakesh"

t1.start()
t2.start()
t3.start()
t4.start()