
# def func1(name,age,countr="INDIA"):
#  print(name, age ,countr)

# print("name  age countr")
# func1("SAGAR",19)
# func1("SAHIL",22)
# func1(age=22,name = "MAROTI")
# func1(25,"HARRY","USA")

# def  disp(*kvr): # Here *kvr is called Variable Length Parameter and kvr type is <class,tuple>
# 	print("Number of Values=",len(kvr))
# 	for val in kvr:
# 		print("\t{}".format(val))

# #Main Program
# disp(10,20,30,40,50) # Function Call-1 with 5 Pos Args
# disp(10,20,30,40) # Function Call-2 with 4 Pos Args
# disp(10,20,30) # Function Call-3 with 3 Pos Args
# disp(10,20) # Function Call-4 with 2 Pos Args
# disp(10) # Function Call-5 with 1 Pos Args
# disp()# Function Call-6 with 0 Pos Args
# disp([],(),{})
# disp(set())
# disp(str("HI"),tuple(),set(),list(),dict())
# disp("KVR","PYTHON",1.2,2+3j,True)


# def  calculate(sno,sname,*vals,city="HYD"):  # Here *val is called Variable Length Parameter and vals type is <class,tuple>
# 	print("----------------------------------------------------")
# 	print("Student Number:{}".format(sno))
# 	print("Student Name:{}".format(sname))
# 	print("Student City:{}".format(city))
# 	print("----------------------------------------------------")
# 	if(len(vals)==0):pass
# 	else:	
# 		s=0
# 		for val in vals:
# 			print("\t{}".format(val))
# 			s+=val
# 		print("----------------------------------------------------")
# 		print("Sum={}".format(s))
# 		print("----------------------------------------------------")

# #Main Program
# calculate(100,"RS",10, 20, 30, 40,50)
# calculate(200,"TR",10,20,30,40)
# calculate(300,"DR",10,20,30)
# calculate(400,"DR",10,20)
# calculate(500,"SR",10)
# calculate(600,"SS",1.2,2.2,3.3,4.4,5.5,6.6,city="AP")
# calculate(700,"KV")
#  calculate(600,"SS",city="MUL",1.2,2.2,3.3,4.4,5.5,6.6)---SyntaxError: positional argument follows keyword argument



# def  disp(*kvr): # Here *kvr is called Variable Length Parameter and kvr type is <class,tuple>
# 	print(kvr,type(kvr),len(kvr))
# #Main Program
# disp(10,20,30,40,50) # Function Call-1 with 5 Pos Args
# disp(10,20,30,40) # Function Call-2 with 4 Pos Args
# disp(10,20,30) # Function Call-3 with 3 Pos Args
# disp(10,20) # Function Call-4 with 2 Pos Args
# disp(10) # Function Call-5 with 1 Pos Args
# disp()# Function Call-6 with 0 Pos Args
# disp([23,5,6],(),{})
# disp(set())
# disp(str(),tuple([43],),set([34],),list([24]),dict({23:5}))
# disp("KVR","PYTHON",1.2,2+3j,True)



# def findtotalmarks(sno,sname,cls, *vals,city="HYD",**submarks):
# 	print("@"*40)
# 	for val in vals:
# 		print("{}".format(val),end=" ")
# 	print("\t Number Var Length Values={}".format(len(vals)))
# 	print()
# 	print("@"*40)
# 	print("*"*50)
# 	print("\tStudent Number:{}".format(sno))
# 	print("\tStudent Name:{}".format(sname))
# 	print("\tStudent Class:{}".format(cls))
# 	print("\tStudent City:{}".format(city))
# 	print("-"*40)
# 	if(len(submarks)==0):pass
# 	else:		
# 		print("\tSubjects\tMarks")
# 		print("-"*40)
# 		totmarks=0
# 		for subject,marks in submarks.items():
# 			print("\t{}\t\t{}".format(subject,marks))
# 			totmarks=totmarks+marks
# 		print("-"*40)
# 		print("\tTOTAL MARKS={}".format(totmarks))
# 		print("-"*40)

# #Main Program
# findtotalmarks(10,"RS","X",1,2,3,4,5,Telugu=70,Hindi=80,English=85,Maths=99,Science=89,Social=90)
# findtotalmarks(20,"TR","XII",10,20,30,40,Sanskrit=99,English=80,Maths=75,Physics=59,Chemistry=58)
# findtotalmarks(30,"SS","B.Tech(CSE)",1.2,2.3,3.4,OS=50,DBMS=60,CGI=45)
# findtotalmarks(40,"DR","Research",2,3,4)
# findtotalmarks(50,"SD","BA",city="AP",History=60,Eco=77,Civics=60,Geo=56)
# #findtotalmarks(60,"SR","BA",History=60,Eco=77,Civics=60,Geo=56,"AP")--SyntaxError: positional argument follows keyword argument
# findtotalmarks(60,"SR","BA",0.9,0.8,0.7,0.6,0.5,History=60,Eco=77,Civics=60,Geo=56,city="BANG")
# #findtotalmarks(commerce=50,accounts=45,civics=56,"TAMILNADU",70,"Kaushal","B.Com")--SyntaxError: positional argument follows keyword argument

# #findtotalmarks("KitKat","CadBurry","KinderJoy",commerce=50,accounts=45,civics=56,city="TAMILNADU",sno=70,sname="Kaushal",cls="B.Com")----SyntaxError
# findtotalmarks(70,"Himansu","B,Com","KitKat","CadBurry","KinderJoy",commerce=50,accounts=45,civics=56,city="TAMILNADU")


#NOTE:
#>>> sno,sname,*marks=10,"RS",70,80,90,77
#>>> print(sno)-----------------------10
#>>> print(sname)--------------------RS
#>>> print(marks,type(marks))---------[70, 80, 90, 77] <class 'list'>

#NOTE:
#>>> sno,sname,**submarks=10,"SR",C=30,CPP=40,PY=67-------   sno,sname,**submarks=10,"SR",C=30,CPP=40,PY=67
              
#>>> *marks=10,20,30,40,50--------------------SyntaxError: starred assignment target must be in a list or tuple
#>>> sno,*marks=100,1.3,1.4,3.4
#>>> print(sno,marks)----------------100 [1.3, 1.4, 3.4]


#^----------------------------------------------------------------------------------------------


# def PosPar(sno,sname,smarks):
#      print(sno)
#      print(sname)
#      print(smarks)

# PosPar(10,20,20)
# PosPar(30,40,50)
# PosPar(60,70,80)


#^----------------------------------------------------------------------------------------------
# def kywrd(sno,sname,smarks,city="Hydrabad"):
#       print(sno,sname,smarks,city)

# kywrd(10,"sagar",90)
# kywrd(smarks=70,sno=20,sname="jay")
# kywrd(city="Akola",smarks=70,sno=20,sname="jay")
# kywrd(30,smarks=30,sname="sahil")

#^----------------------------------------------------------------------------------------------

# def varlen(*kvr):

#      for val in kvr:
#           print(val)
#      print("------------------------")
          
# varlen(10,20,30,50)
# varlen(23,43,53,53,)
# varlen(34,54,2)
# varlen()
# varlen([],(),{},set())
# varlen(str("HI"),tuple([147]),set([10]),list[10],tuple(),list(),dict({2:3}))
#^----------------------------------------------------------------------------------------------


# def calculate(sno,sname,*vals,city ="Hyd",**Sbj):
#      print("sno\tsname\tcity")
#      print(sno,"\t",sname,"\t",city)
#      if  len(vals)==0:
#          print("MARKS ARE NOT GIVEN ")
#      else:
#       print("------MARKS--------")
#       s = 0
#       for val in vals:
#            print(val)
#            s = s+val
#       print(f"Sum of marks : {s}")

#      print("-------SUBJECTS---------")
#      for k,v in Sbj.items():
#          print(f"{k}->{v}")
#      print("---------------")
# calculate(10,"rs",90,40,20,30)
# calculate(20,"rs",28,3,12,43)
# calculate(30,"rs",)
 #* kuthehi chalte dfparameter fact *val chya pahile nahi
# calculate(40,"rs",48,30,2,23,city="Akola")
# calculate(10,"rs",90,40,20,0,city="Rohada",First="Science",Second="History",Third="Geography",Fourth="Math")
# calculate(10,"rs",90,40,20,0,First="Science",Second="History",Third="Geography",city="Jaypur")
# calculate(10,"rs",90,40,20,0,First="Science",Second="History",Third="Geography",city="Rohada",Fourth="Math")
#^----------------------------------------------------------------------------------------------