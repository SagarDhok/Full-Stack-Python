
#^-----------------------------------------------------------------------------------------
#!Find Max and min Values from ndarray--1 Dim
# import numpy as np

# print(a)
# max = np.amax(a)
# min = np.amin(a)
# print("MAX VALUE : ",max)
# print("MIN VALUE : ",min)


#! Find Max and min Values from ndarray--2 Dim
# import numpy as np
# a = np.array([37,34,23,65,68,55]).reshape(2,3)
# print(a)

# max = np.amax(a)
# min = np.amin(a)
# print("MAX VALUE : ",max)
# print("MIN VALUE : ",min)

#^-----------------------------------------------------------------------------------------
#! Now My Req: To find Column-wise and Row-wise Max and Min Values
#*To Do the above, we must use axis concept.
#* if axis=1 then It refers ROWS
#* if axis=0 then It refers COLUMNS

# import numpy as np
# a = np.random.randint(10,30,size=(4,4))
# print(a)

# max = np.amax(a)
# min = np.amin(a)
# rmax = np.amax(a,axis=1)
# rmin = np.amin(a,axis=1)
# cmax = np.amax(a,axis=0)
# cmin = np.amin(a,axis=0)
# print("MAX VALUE : ",max)
# print("MIN VALUE : ",min)
# print("ROW MAX : ",rmax)
# print("ROW MIN : ",rmin)
# print("COL MAX : ",cmax)
# print("COL MIN :",cmin)
#^-----------------------------------------------------------------------------------------
#! Find the mean on ndarray by using mean()--1-Dim
# import numpy as np
# a=np.array([3,1,2,4])
# print(a)

# m = np.mean(a)
# print(f"MEAN : ({a}) = {m} ")

#! Our Own Code for Finding Sum and Mean (Average)
# import numpy as np
# a = np.array([3,2,1,4])
# print(a)
# s = 0
# for v in a:
#      s = s+v
# print(f"Average : ({a}) = {s/len(a)}")


#! Find the mean on ndarray by using mean()--2-Dim
#! Find the mean for Col and Row
# import numpy as np
# a =np.array([3,1,2,4]).reshape(2,2)
# print(a)
# m = np.mean(a)
# rm = np.mean(a,axis=1)
# cm = np.mean(a,axis=0)
# print(f"Mean : {m}")
# print(f"Row Mean : {rm}")
# print(f"Col Mean :{cm}")

#! Find the mean on ndarray by using mean()--2-Dim
#! Find the mean for Col and Row
# import numpy as np
# a = np.random.randint(1,50,size=(5,5))
# print(a)
# m = np.mean(a)
# rm = np.mean(a,axis=1)
# cm = np.mean(a,axis=0)
# print(f"Mean : {m}")
# print(f"Row Mean : {rm}")
# print(f"Col Mean :{cm}")
#^-----------------------------------------------------------------------------------------
#! Find the median of ndarray--1-Dim with ODD Number of Elements
# import numpy as np
# a=np.array([10,2,14,3,18,20,5])
# print(a)
# m = np.median(a)
# print("Median : ",m )

#! Find the median of ndarray--1-Dim with Even Number of Elements
# import numpy as np
# a=np.array([10,2,14,3,18,20,5,6])
# a.sort()
# print(a)
# m = np.median(a)
# print("Median : ",m)

# #! Find the median of ndarray--2-Dim with Even Number of Elements
# import numpy as np
# a=np.array([10,2,14,3,18,20,5,6,12,22,13,25,19,4,1,9]).reshape(4,4)
# print(a)
# m = np.median(a)
# rm = np.median(a,axis=1)
# cm = np.median(a,axis=0)
# print("Median : ",m)
# print("Row Median : ",rm)
# print("Col Median : ",cm)
#^-----------------------------------------------------------------------------------------

#! Finding Variance by using var()
# import numpy as np
# a=np.array([3,1,2,4])
# print(a)
# v = np.var(a)
# print("Variance : ",v)

#! Find Col and Row-wise variance
# import numpy as np
# a=np.array([3,1,2,4]).reshape(2,2)
# print(a)
# v = np.var(a)
# rv= np.var(a,axis=1)
# cv = np.var(a,axis=0)
# print("Variance : ",v)
# print("Row Var=",rv)
# print("Col Var=",cv)

#!Find Col and Row-wise variance
# import numpy as np
# a=np.arange(4*3).reshape(4,3)
# print(a)
# v = np.var(a)
# rv= np.var(a,axis=1)
# cv = np.var(a,axis=0)
# print("Variance : ",v)
# print("Row Var=",rv)
# print("Col Var=",cv)


#!Find Col and Row-wise variance
# import numpy as np
# a=np.arange(4*3).reshape(4,3)
# print(a)
# v = np.var(a)
# rv= np.var(a,axis=1)
# cv = np.var(a,axis=0)
# print("Variance : ",v)
# print("Row Var=",rv)
# print("Col Var=",cv)

# print("Row-wise Var")
# for v in rv:
#     print(round(v,2),end="  ")
# print()    

# print("Col-wise Var")
# for v in cv:
#     print("%0.1f"%v,end="  ")
# print()    

#^-----------------------------------------------------------------------------------------
#! We Know that standard Deviation= sqrt(Var)
#! Find Col and Row-wise variance
# import numpy as np
# a=np.array([3,1,2,4]).reshape(2,2)
# s=np.std(a)
# rsd=np.std(a,axis=1)
# csd=np.std(a,axis=0)
# print("Standard Deviation : ",s)
# print("Row Std=",rsd)
# print("Col Std =",csd)

# import numpy as np
# a=np.array([3,1,2,4])
# s=np.std(a)
# print(s)
#^-----------------------------------------------------------------------------------------
#! Find the Mode of ndarray 
#* AttributeError
# import numpy as np
# a=np.array([3,1,2,4,3,3])
# print(a)
#m=np.mode(a)-----------AttributeError: module 'numpy' has no attribute 'mode'
#^-----------------------------------------------------------------------------------------
#! Find the Mode of ndarray by using a pre-defined Module statistics of python
# import statistics as s
# import numpy as np
# a=np.array([3,1,1,1,2,4,3,3])
# print(a)
# m=s.mode(a)
# print("Mode=",m)

# import numpy as np,statistics as s
# a=np.array([3,1,1,1,1,2,4,3,3,3])
# print(a)
# m=s.mode(a)
# print("Mode=",m)

# ! Find the Mode of ndarray by using a pre-defined Module statistics of python
# import statistics as s
# import numpy as np
# a=np.array([1,3,2,4,3,3,1,1,2,2,3,3,2])
# m=s.multimode(a)
# print("Mode=",m)


# import statistics as s
# import numpy as np
# a=np.array([1,1,2,2,3,3,4,5])
# m=s.multimode(a)
# print("Mode=",m)