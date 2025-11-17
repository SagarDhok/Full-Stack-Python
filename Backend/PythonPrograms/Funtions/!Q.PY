

#?  =============================================================================================
# def func1(name,age,countr="INDIA"):
#  print(name, age ,countr)

# print("name  age countr")
# func1("SAGAR",19)
# func1("SAHIL",22)
# func1(age=22,name = "MAROTI")
# func1(25,"HARRY","USA")
#?  =============================================================================================
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
# disp(str("HI"),tuple([47]),set(),list(),dict({2:3}))
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
# #calculate(600,"SS",city="MUL",1.2,2.2,3.3,4.4,5.5,6.6)---SyntaxError: positional argument follows keyword argument
# calculate(700,"KV")
#?  =============================================================================================


