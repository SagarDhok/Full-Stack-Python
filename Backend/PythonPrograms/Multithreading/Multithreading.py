
#^------------------------------------------------------------------------------------------------
#! Defualt Thread Name 
# import threading

# tname = threading.current_thread().name
# print("Name of default thread is : ",tname)
#^------------------------------------------------------------------------------------------------
#! Program for Showing the Internal Flow of Default Thread
# import threading
# print("*"*50)
# print("\t\tDefault flow ")
# print("*"*50)
# def welcome():
#      print(f"Line 15 - Exexuted by : {threading.current_thread().name} ")

# def hello():
#      print(f"Line 18 - Executed by  : {threading.current_thread().name}")

# def hi():
#      print(f"Line 21 Executed by : {threading.current_thread().name}")


# print("line 24----------------------------------------------------------")
# print(f"Program executon started by {threading.current_thread().name}")
# print("-----------------------------------------------------------------")
# welcome()
# print("line28")
# hello()
# print("line30")
# hi()
# print("line32")
# print("-----------------------------------------------------------------")
# print(f"Program executon Ended by {threading.current_thread().name}")
# print("-----------------------------------------------------------------")
#^------------------------------------------------------------------------------------------------
#! Program for Showing the Internal Flow of Sub Threads and Default Thread
# import threading
# print("*"*50)
# print("\t\tSubthreads flow ")
# print("*"*50)
# def welocome():
#      print(f"welcome()- This is Executed by : {threading.current_thread().name}")
# def hello():
#      print(f"hello() - This is Executed by : {threading.current_thread().name}")
# def hi(): 
#      print(f"hi()- This is Executed by : {threading.current_thread().name}")

# print("line-49---------------------------------------------")
# print(f"Program Execution Started by : {threading.current_thread().name}")
# print("-----------------------------------------------------")
# print()
# print()
 
#  #* threding is module and Thread is class name
# t1= threading.Thread(target=welocome)     #* here t1 is called thread object whose name is Thread-
# t1.name="salaman"  #todo - programmer defined subthread name
# print("line - 58")
# t2= threading.Thread(target=hello)        #* here t2 is called thread object whose name is Thread-2
# t2.name = "aamir"  #todo - programmer defined subthread name
# print("line - 61")
# t3 = threading.Thread(target=hi)          #* here t3 is called thread object whose name is Thread-3
# t3.name = "Hrithik" #todo - programmer defined subthread name
# print("line - 61")

# #* Dispatch the sub threads
# #* here t1 , t2 and t3 are objects of thread class
# t1.start()     
# print("line-69")
# t2.start()    
# print("line-71")
# t3.start()     
# print("line-73")


# print()
# print()
# print("----------------------------------------------------")
# print(f"Program Execution Ended by : {threading.current_thread().name}")
# print("-----------------------------------------------------")

#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Sequential Execution only with Deafult Thread--MainThread
# import threading,time
# def square(lst):
#      for val in lst:
#           print(f"{threading.current_thread().name} : SQUARE ({val}) = {val**2}")
#           time.sleep(1)
           
# def cube(lst):
#      for val in lst:
#       print(f"{threading.current_thread().name} : CUBE ({val}) = {val**3} ")
#       time.sleep(1)
      

# bt=time.time()
# print(f"Program Execution Started by : {threading.current_thread().name}")
# print("-"*60)

# lst = [10,20,30,40,50]
# square(lst)
# print("\t------------------------------")

# cube(lst)

# print("-"*60)
# print(f"\tProgram Execution Ended by : {threading.current_thread().name}")
# et = time.time()
# print(f"Total Execution Time With Default Thread : {et-bt}")
#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Concurrent Execution only with Sub Threads along MainThread
# import threading,time
# def square(lst):
#      for val in lst:
#       print(f"{threading.current_thread().name} -> Square({val}) = {val**2}")
#       time.sleep(1)
     
# def cube(lst):
#       for val in lst:
#        print(f"{threading.current_thread().name} -> Cube({val}) = {val**3}")
#        time.sleep(1)


# bt = time.time()
# print(f"Program Execution Started by : {threading.current_thread().name}")
# print("-"*60)

# lst = [10,20,30,40,50]
# t1 = threading.Thread(target=square ,args = (lst,))


# t2 = threading.Thread(target=cube , args=(lst,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# print("-"*60)
# print(f"Program Execution Ended by : {threading.current_thread().name}")
# et = time.time()
# print("Total Time With Sub threads :",et-bt)

#^------------------------------------------------------------------------------------------------
#! Program for demonstrating the default thread
# import threading
# t1 = threading.current_thread()
# print(t1.name)
# print("---------or------------")
# print(threading.current_thread().name)
#^------------------------------------------------------------------------------------------------
#! Program for finding number of threads running in python Program
# import threading 
# print(threading.current_thread())  # <_MainThread(MainThread, started 16080)>
# print("Current Thread : ",threading.current_thread().name)
# print("Number of Running Threads : ",threading.active_count())

#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating Sub thread creation and dispatching the sub thread
# import threading,time

# def greet(val):
#      print(f"{threading.current_thread().name} : Hello {val} Good Morning ")


# print(f"Program Execution Started by : {threading.current_thread().name}")
# t1 = threading.Thread(target=greet ,args=("Salman Khan",))
# print("Execution Status of Sub thread t1=",t1.is_alive())
# print(f"Number of Active Threads : {threading.active_count()}")

# #* Dispatching the Sub Thread(s)
# t1.start()
# print("Execution Status of Sub thread t1=",t1.is_alive())
# print(f"Number of Active Threads : {threading.active_count()}")

#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating Sub thread creation and dispatching the sub thread
# import threading 
# def greet(val):
#      print(f"{threading.current_thread().name} : Hi {val} Good Morning")


# t1 = threading.Thread(target=greet , args=("Allu Arjun",))

# print(t1.getName())  #* -> DeprecationWarning: getName() is deprecated, get the name attribute instead
# print(t1.name)

# t1.setName("Rossum")   #*->  DeprecationWarning: getName() is deprecated, get the name attribute instead

# t1.name = "Rossum"
# print(t1.name)

# t1.start()
#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating the need of join() of Thread class
#* without joit first maithread will execute it wont wait for subthreads
# import threading,time
# def welcome(val):
#      print(f"{threading.current_thread().name} : hi {val} Good Morning")
#      time.sleep(10)
#      print(f"{threading.current_thread().name} : Coming Out Of the Sleep")


# print(f"Program Execution Started by : {threading.current_thread().name}")
# t1= threading.Thread(target=welcome, args=("kunla",))
# print(f"Exucution staus of t1 before start() : {t1.is_alive()} ")

# t1.start()
# print(f"Execution status of t1 after start() : {t1.is_alive()} ")


# t1.join()  #* Make the MainThread to wait until Sub Threads joins with MainThread
# print("Exectution status of t1 after join() : ",t1.is_alive())

# print(f"Program execution ended by : {threading.current_thread().name}")
#^------------------------------------------------------------------------------------------------
#! Program for generating 1 to N numebrs by using threads
#! NumberGenFunEx1.py
# import threading, time
# def numsgenrator(n):
#      if n<=0:
#           print(f"{threading.current_thread().name()} : {n} Is invalid Input")
#      else:
#           for i in range(1,n+1):
#                print(f"{threading.current_thread().name} - Value of i : {i}")
#                time.sleep(0.25)
# n = int(input("Enter How many numbers do you want to genrate : "))
# t1 = threading.Thread(target=numsgenrator,args=(n,))

# t1.start()
     
#^------------------------------------------------------------------------------------------------
#! Program for generating 1 to N numebrs by using threads
#! NumberGenOopsEx1.py
# import threading,time
# class Numbers:
#      def numbergenrator(self,n):
#             if n<=0:
#                   print(f"{threading.current_thread().name} - {n} is invalid input")
#             else:
#                for i in range(1,n+1):
#                     print(f"{threading.current_thread().name} - val of i : {i}")
#                     time.sleep(0.20)


# n = int(input("Enter How many numbers do you want to generat : "))
# no = Numbers()
# t1 = threading.Thread(target=no.numbergenrator,args=(n,))
# t1.start()
#^------------------------------------------------------------------------------------------------
#!Program for generating 1 to N numebrs by using threads
#!NumberGenOopsEx2.py
# import threading, time
# class Numbers:
#      def numgenrator(self,val):
#           if val<=0:
#                print(f"{threading.current_thread().name} - {val} is invalid input")
#           else:
#                for i in range(1,val+1):
#                     print(f"{threading.current_thread().name} - value of i : {i}")
#                     time.sleep(0.25)

# t1 = threading.Thread(target=Numbers().numgenrator,args=(int(input("Enter how many numbers do you want to genrate : ")),))
# t1.start()
#^------------------------------------------------------------------------------------------------
#! Program for generating 1 to N numebrs by using threads
#! NumberGenOopsEx3.py
# import threading,time
# class Numbers : 
#      def numgenrator(self,n):
#           if n<=0:
#                print(f"{threading.current_thread().name} - {n} is invalid input")
#           else:
#                for i in range(1,n+1):
#                     print(f"{threading.current_thread().name} - i values is : {i}")
#                     time.sleep(0.25)

# threading.Thread(target=Numbers().numgenrator, args=(int(input("Enter how many numbers do you want to genrate : ")),)).start()

#* if target is not given  AssertionError
#^------------------------------------------------------------------------------------------------
#! Program for generating 1 to N numebrs by using threads
#! NumberGenOopsEx4.py
# import threading,time
# class Numbers:
#      def __init__(self,n):
#           self.n = n
#      def numbergen(self):
#           if self.n<=0:
#                print(f"{threading.current_thread().name} - {self.n} is invalid input")
#           else:
#                for i in range(1,self.n+1):
#                     print(f"{threading.current_thread().name} - value of i - {i}")
#                     time.sleep(0.25)

# n = int(input("Enter How many numbers do you want to genrate : "))
# no= Numbers(n)
# t1 = threading.Thread(target=no.numbergen)
# t1.start()
          
#^------------------------------------------------------------------------------------------------
#! Program for generating 1 to N numebrs by using threads
#! NumberGenOopsEx5.py
# import threading,time
# class Numbers:
#      def __init__(self,n):
#           self.n = n
          
#      def numbergen(self):
#           if self.n <= 0:
#                print(f"{threading.current_thread().name} - {self.n}  is invalid input")

#           else:
#                for i in range(1,self.n+1):
#                     print(f"{threading.current_thread().name} - value of i : {i}")
#                     time.sleep(0.25)
# n = int(input("enter How Many numbers do you want to genrate : "))
# t1 = threading.Thread(target=Numbers(n).numbergen)
# t1.start()
#^------------------------------------------------------------------------------------------------
#! Program for generating 1 to N numebrs by using threads
#! NumberGenOopsEx6.py
# import threading,time
# class Numbers:
#      def __init__(self,n):
#           self.n = n
          
#      def numbergen(self):
#           if self.n <= 0:
#                print(f"{threading.current_thread().name} - {self.n}  is invalid input")

#           else:
#                for i in range(1,self.n+1):
#                     print(f"{threading.current_thread().name} - value of i : {i}")
#                     time.sleep(0.25)
# n = int(input("enter How Many numbers do you want to genrate : "))
# threading.Thread(target=Numbers(n).numbergen).start()
#^------------------------------------------------------------------------------------------------
#! Program for accepting Line of Text and display every word and letters in that word
# import threading,time
# class lineoftext:
#      def __init__(self,line):
#           self.line= line
#      def displine(self):
#           for word in self.line.split():
#                print(f"{threading.current_thread().name} : {word} ")
#                time.sleep(0.25)
#                for ch in word:
#                     print(f"{threading.current_thread().name} : {ch}")
#                     time.sleep(0.25)
#                print()

# line = input("Enter A line : ")
# lo = lineoftext(line)
# t1 = threading.Thread(target=lo.displine)   
# t1.start()       


#^------------------------------------------------------------------------------------------------
#! Program for accepting Line of Text and display every word and letters in that word
#! WordsGenerateOops.py
# import threading,time
# class Lineoftext:
#      def __init__(self,line):
#           self.line = line
#      def displaytxt(self):
#           for word in self.line.split():
#                time.sleep(0.25)
#                print(f"{threading.current_thread().name} :  {word}")
#                for ch in word:
#                     print(f"{threading.current_thread().name} : {ch}")
#                     time.sleep(0.25)
#                print()

# threading.Thread(target=Lineoftext(input("Enter Line Of text :")).displaytxt).start()
#^------------------------------------------------------------------------------------------------
#! Program for Generating Odd and Even threads by using Multiple Threads
#! EvenOddFunEx1.py

# import threading,time

# def oddval(n):
#      if n <=0:
#           print(f"{threading.current_thread().name} - {n} is invalid input")
#      else:
#       for i in range(1,n+1,2):
#            print(f"{threading.current_thread().name} - ODD VALUE : {i} ")
#            time.sleep(0.25)
# def evenval(n):
#      if n<=0:
#          print(f"{threading.current_thread().name} - {n} is invalid input")
#      for i in range(0,n+1,2):
#           print(f"{threading.current_thread().name} - EVEN VALUE : {i}")
#           time.sleep(0.25)

# print(f"Program Execution started by : {threading.current_thread().name}")
# t1 = threading.Thread(target=oddval ,args = (10,) )
# t2 = threading.Thread(target=evenval, args=(10,))
# print(f"Number of threds active before start() : {threading.active_count()}")
# #* Dispatching the threads
# t1.start()
# t2.start()
# print(f"Number of threads acive after start() : {threading.active_count()}")
# #* Joining the threads
# t1.join()
# t2.join()
# print(f"Number of threads after active join(): {threading.active_count()}")
# print(f"Program Execution Ended by : {threading.current_thread().name}")

#^------------------------------------------------------------------------------------------------
#! Program for Generating Odd and Even threads by using Multiple Threads
#! EvenOddFunEx2.py
# import threading,time
# def oddval(n):
#   if n<=0:
#     print(f"{threading.current_thread().name} - {n} is invlaid input")
#   else:
#     for i in range(1,n+1,2):
#       print(f"{threading.current_thread().name} - Odd val : {i}")
#       time.sleep(0.25)
# def evenval(n):
#   if n<=0:
#     print(f"{threading.current_thread().name} - {n} is invalid input")
#   else:
#     for i in range(0,n+1,2):
#       print(f"{threading.current_thread().name} - Even val : {i}")
#       time.sleep(0.25)

# print(f"Program Execution started by : {threading.current_thread().name}")
# t1 = threading.Thread(target=oddval, args=(int(input("Enter how many Numbers do you want to genrate odd : ")),))
# t2 = threading.Thread(target=evenval , args=(int(input("Enter How many Numbers do you want to genrate even : ")),))
# print(f"Number of threds active before start() : {threading.active_count()}")

# #* Dispatching the threads
# t1.start()
# t2.start()
# print(f"Number of threads acive after start() : {threading.active_count()}")

# #* Joining the threads
# t1.join()
# t2.join()
# print(f"Number of threads after active join(): {threading.active_count()}")

# print(f"Program Execution Ended by  : {threading.current_thread().name}")
#^------------------------------------------------------------------------------------------------
#! Program for Generating Odd and Even threads by using Multiple Threads
#! EvenOddFunEx2.py
# import threading,time
# def oddval(n):
#   if n<=0:
#     print(f"{threading.current_thread().name} - {n} is invlaid input")
#   else:
#     for i in range(1,n+1,2):
#       print(f"{threading.current_thread().name} - Odd val : {i}")
#       time.sleep(0.25)
# def evenval(n):
#   if n<=0:
#     print(f"{threading.current_thread().name} - {n} is invalid input")
#   else:
#     for i in range(0,n+1,2):
#       print(f"{threading.current_thread().name} - Even val : {i}")
#       time.sleep(0.25)

# print(f"Program Execution started by : {threading.current_thread().name}")
# t1 = threading.Thread(target=oddval, args=(int(input("Enter how many Numbers do you want to genrate odd : ")),))
# t2 = threading.Thread(target=evenval , args=(int(input("Enter How many Numbers do you want to genrate even : ")),))
# print(f"Number of threds active before start() : {threading.active_count()}")

# #* Dispatching the threads
# t1.start()
# t2.start()
# print(f"Number of threads acive after start() : {threading.active_count()}")

# #* Joining the threads
# t1.join()
# t2.join()
# print(f"Number of threads after active join(): {threading.active_count()}")

# print(f"Program Execution Ended by  : {threading.current_thread().name}")
#^------------------------------------------------------------------------------------------------
#! Program for Generating Odd and Even threads by using Multiple Threads
#! EvenOddOopEx1.py
# import threading,time
# class Number:
#  def oddval(self,n):
#    if n<=0:
#      print(f"{threading.current_thread().name} - {n} is invlaid input")
#    else:
#      for i in range(1,n+1,2):
#        print(f"{threading.current_thread().name} - Odd val : {i}")
#        time.sleep(0.25)
#  def evenval(self,n):
#    if  n<=0:
#      print(f"{threading.current_thread().name} - {n} is invalid input")
#    else:
#      for i in range(0,n+1,2):
#        print(f"{threading.current_thread().name} - Even val : {i}")
#        time.sleep(0.25)

# print(f"Program Execution started by : {threading.current_thread().name}")
# t1 = threading.Thread(target=Number().oddval, args=(int(input("Enter how many Numbers do you want to genrate odd : ")),))
# t2 = threading.Thread(target=Number().evenval , args=(int(input("Enter How many Numbers do you want to genrate even : ")),))
# print(f"Number of threds active before start() : {threading.active_count()}")

# #* Dispatching the threads
# t1.start()
# t2.start()
# print(f"Number of threads acive after start() : {threading.active_count()}")

# #* Joining the threads
# t1.join()
# t2.join()
# print(f"Number of threads after active join(): {threading.active_count()}")

# print(f"Program Execution Ended by  : {threading.current_thread().name}")
#^------------------------------------------------------------------------------------------------
#! Program for Generating Odd and Even threads by using Multiple Threads
#! EvenOddOopEx1.py
# import threading,time
# class OddNum:
#  def oddval(self,n):
#    if n<=0:
#      print(f"{threading.current_thread().name} - {n} is invlaid input")
#    else:
#      for i in range(1,n+1,2):
#        print(f"{threading.current_thread().name} - Odd val : {i}")
#        time.sleep(0.25)
# class EvenNum:
#  def evenval(self,n):
#    if  n<=0:
#      print(f"{threading.current_thread().name} - {n} is invalid input")
#    else:
#      for i in range(0,n+1,2):
#        print(f"{threading.current_thread().name} - Even val : {i}")
#        time.sleep(0.25)

# print(f"Program Execution started by : {threading.current_thread().name}")
# t1 = threading.Thread(target=OddNum().oddval, args=(int(input("Enter how many Numbers do you want to genrate odd : ")),))
# t2 = threading.Thread(target=EvenNum().evenval , args=(int(input("Enter How many Numbers do you want to genrate even : ")),))
# print(f"Number of threds active before start() : {threading.active_count()}")

# #* Dispatching the threads
# t1.start()
# t2.start()
# print(f"Number of threads acive after start() : {threading.active_count()}")

# #* Joining the threads
# t1.join()
# t2.join()
# print(f"Number of threads after active join(): {threading.active_count()}")

# print(f"Program Execution Ended by  : {threading.current_thread().name}")
#^------------------------------------------------------------------------------------------------
