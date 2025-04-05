
#! 3.uniform() 
#* slight diffrence 
#* normal = high differece 
#^---------------------------------------------------------------------------------------
#* Syntax-1: numpy.random.uniform()--->Generating Any random floating point value between 0.0 to 1.0.
# import numpy.random as r
# a = r.uniform()
# print(a,type(a))
#^---------------------------------------------------------------------------------------
#* Syntax-2: numpy.random.unform(low,high)--->Generating Any random floating point value between low and high															
# import numpy.random as r
# a = r.uniform(10,11)
# print(a,type(a))
# b = r.uniform(10,20)
# print(b,type(b))


#^---------------------------------------------------------------------------------------
#* Syntax-3: numpy.random.uniform(low,high,size)--->Generating Number of Random floating Values (Row, Cols) 
# 									between low to high  with size(Single Value)	ie. 1-D	
# 									-->Generating Number of Random floating Values (Row, Cols) 
# 									between low to high  with size(Rows x Cols)	ie. 2-D
# 									-->Generating Number of Random floating Values (Matrices,Row, Cols) 
# 									between low to high  with size(Matrices,Rows x Cols)	ie. 3-D	



# import numpy.random as r
# rvs=r.uniform(10,11,size=4) # 1-D  with 4 values
# print(rvs,type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)

# import numpy.random as r
# rvs=r.uniform(10,11,size=(2,3)) # 2-D  with 2 rows and 3 Cols
# print(rvs,type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)

# import numpy.random as r
# rvs=r.uniform(99.1,99.5,size=(3,3,3)) # 3-D  with  3 Matrices along 3 rows and 3 Cols
# print(rvs,type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)


# import numpy.random as r
# rvs=r.uniform(99.1,99.5,size=(2,2,3,3)) # 4-D  with 2 clusters along with 2 Matrices 3 rows and 3 Cols
# print(rvs,type(rvs))
# print("Dim of rvs=",rvs.ndim)
# print("data type of rvs=",rvs.dtype)
# print("Shape of rvs=",rvs.shape)
# print("Size of rvs=",rvs.size)

