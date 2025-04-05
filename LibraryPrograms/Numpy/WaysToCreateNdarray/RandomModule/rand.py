

#! 2.rand()
#^---------------------------------------------------------------------------------------
#*Syntax-1: varname=numpy.random.rand()------------>Single Random Value between 0.0 to 1.0
# from numpy import random as r
# x = r.rand()
# print("random float value  = ",x)
# print(type(x))

# from numpy import random as r
# x = r.rand()
# print("random float value  = %0.2f"%x)
#^---------------------------------------------------------------------------------------
#*Syntax-2: varname=numpy.random.rand(Value)
#*Random Number of Values (Value times) between 0.0 to 1.0--1-
#*value - kiti value pahijet

# from numpy import random as r
# rvs = r.rand(3)
# print("Content of rvs = ",rvs)
# print("Type of rvs = ",type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)

#^---------------------------------------------------------------------------------------
#*Syntax-3: varname=numpy.random.rand(Rows,Cols)
#*Random Number of Values (Value times) between 0.0 to 1.0 ---2-D 

# from numpy import random as r
# rvs = r.rand(3,3,3)
# print("Content of rvs = \n",rvs)
# print("Type of rvs = ",type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)

# from numpy import random as r
# rvs = r.rand(2,3,3)
# print("Content of rvs = \n",rvs)
# print("Type of rvs = ",type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)
#^---------------------------------------------------------------------------------------

# from numpy import random as r
# a = r.rand(6)
# print(a)
# for i in a:
#      print("%0.2f"%i)
#      print(round(i,2))


#^---------------------------------------------------------------------------------------
# from numpy import random as r
# a=r.rand(3,4)
# print(a)
# print("-"*50)
# for ri in a:
#      for ci in ri:
#           print(round(ci,2),end = " ")  
#      print()   

# from numpy import random as r
# a=r.rand(3,4)
# print(a)
# print("-"*50)
# for ri in range(len(a)):
#      for ci in range(len(a[0])):
#           print(round(a[ri,ci],2),end = " ")
#      print()
#^---------------------------------------------------------------------------------------
# from numpy import random as r
# a=r.rand(2,3,3)
# print(a)
# print("-----------------------------------------")
# for mi in a:
#      for ri in mi:
#           for ci in ri:
#                  print(round(ci,2),end = " ")  
#           print()   


# from numpy import random as r
# a=r.rand(2,3,3)
# print(a)
# print("-----------------------------------------")
# for mn in range(len(a)): # Number of Matrices
#     for rn in range(len(a[0])): # Number of Rows in Each Matrix
#         for cn in range(len(a[0])): # Number of Cols in Each Matrix
#           #   print(mn,rn,cn,)
#             print(round(a[mn,rn,cn],3),end="\t")
#         print()
#     print("-----------------------------")
        
