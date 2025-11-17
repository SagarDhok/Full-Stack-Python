
#! 1.randint()
#^---------------------------------------------------------------------------------------
#*syntax-1
#*randint(value) -> value-1
# import numpy.random as r
# x= r.randint(100)
# print(x)
# print(type(x))
#^---------------------------------------------------------------------------------------
#*syntax-2
#*randint(low,high) -> high-1
# from numpy import random as r
# x = r.randint(100,1000)
# print(x,type(x))          #*160 <class 'int'>

# from numpy import random as r
# x = r.randint(100,100000000)
# print("MH29"+str(x))          
#^---------------------------------------------------------------------------------------
#*syntax-3
#*randint(low,high,size) -> high-1  ,size = kiti genrate karayche
# from numpy import random as r
# x = r.randint(10,200000000,size=(3))
# print(x)


# from numpy import random as r
# x = r.randint(100,100000000,size=(5))
# print(x)

# from numpy import random as r
# x=r.randint(10,100000,size=3)
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("Shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("Size of x=",x.size)

# from numpy import random as r
# x=r.randint(10,20,size=(3,3))
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("Shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("Size of x=",x.size)


# from numpy import random as r
# x=r.randint(10,20,size=(2,3,3))
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("Shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("Size of x=",x.size)



# from numpy import random as r
# x=r.randint(10,20,size=(2,3,3,3))
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("Shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("Size of x=",x.size)

# from numpy import random as r
# x=r.randint(10,20,size=2+4+5)
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("Shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("Size of x=",x.size)


# from numpy import random as r
# x=r.randint(10,20,size=2*3*3).reshape(2,3,3)
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("Shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("Size of x=",x.size)


# from numpy import random as r
# x = r.randint(2.3)
# print(x)

# y = r.randint(1)
# print(y)