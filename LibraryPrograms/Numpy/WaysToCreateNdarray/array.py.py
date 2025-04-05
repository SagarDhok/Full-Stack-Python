
#! <1>.array()
#^----------------------------------------------------------------------------------------
#* int
#*syntax-1
# import numpy as np
# a = 10
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


#*syntax-2
# import numpy as np
# a = 20
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a,dtype = str)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


#*syntax-3
# import numpy as np
# a = 20
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a,float)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)
#^----------------------------------------------------------------------------------------
#*float
#*syntax-1
# import numpy as np
# a = 20.2
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


# #*syntax-2
# import numpy as np
# a = 20.2
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a,dtype = int)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


# #*syntax-3
# import numpy as np
# a = 20.2
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a,str)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)
#^----------------------------------------------------------------------------------------
#*str
# import numpy as np
# a = "python"
# print("content of a =",a)
# print("type of a =",a)
# b = np.array(a)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)
#^----------------------------------------------------------------------------------------
#* range
#* syntax-1
# import numpy as np
# r = range(12)
# print("content of a =",r)
# print("type of a =",r)
# b = np.array(r)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


# #* syntax-2
# import numpy as np
# r = range(12)
# print("content of a =",r)
# print("type of a =",r)
# b = np.array(r,dtype=str)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


#* syntax-3
# import numpy as np
# r = range(12)
# print("content of a =",r)
# print("type of a =",r)
# b = np.array(r,float)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)



# import numpy as np
# r = range(10,21,2)
# print("content of a =",r)
# print("type of a =",r)
# b = np.array(r)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)


# import nu
# print("size of b = ",b.size)mpy as np
# r = range(10,21,2)
# print("content of a =",r)
# print("type of a =",r)
# b = np.array(r,float)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)

# import numpy as np
# r = range(10,21,2)
# print("content of a =",r)
# print("type of a =",r)
# b = np.array(r)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)
# print("size of b = ",b.size)
#^----------------------------------------------------------------------------------------
#! Re-Shape the ndarray Elements
#* 1. By using reshape() of ndarray object
#* 2. By using shape attribute
# import numpy as np
# a  = [10,20,30,40,50,60]
# b = np.array(a)
# print(b.reshape(3,2))
# print(b)

#*b la pan update karaych asel tr b madhi store kara lagte
# b = b.reshape(3,2)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)

# import numpy as np
# a  = [10,20,30,40,50,60]
# b = np.array(a)
# b.shape = (3,2)
# # b = b.reshape(6,)
# # print(b)
# b.shape = (6,)
# print(b)


#* i want to convert 2-D Array into 1-D Array, reshape() can't be used
#* To do this, we use shape attribute

# b.shape = (6,)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)


#* shape is attribute it also modifies original
# b.shape = (3,2)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b = ",b.shape)


# import numpy as np
# a=np.array(range(16))
# print("Content of a=\n",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#*#Convert the above 1D data into 2D
# a.shape= (4,4)
# print("Content of a=",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)



#* Convert the above 2D data into 3D---(2,4,2)
# a.shape = (2,4,2)
# print("Content of a=",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


#* Convert the above 3D data into 4D---(2,2,2,2)
# a.shape = (2,2,2,2)
# print("Content of a=",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# a.shape = (4,2,2,1)
# print("Content of a=",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


#* convert list object into ndarray object
# lst=[10,20,30,40,50,60,70,80,90]
# a=np.array(lst)
# print("Content of a=",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# lst=[10,20,30,40,50,60,70,80,90]
# a=np.array(lst,float)
# print("Content of a=",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)



# a.shape=(3,3)
# print("Content of a=\n",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)



# import numpy as np
# lst=[10,"RS",34.56,True,2+3j]
# a=np.array(lst)
# print("Content of a=",a)
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# import numpy as np
# lst=[10,"RS",34.56,True,2+3j,"python"]
# a=np.array(lst,dtype=object)
# print("Content of a=",a)
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)



# a=a.reshape(3,2)
# print("Content of a=\n",a)
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# import numpy as np
# lst=(10,"RS",34.56,True,2+3j,"Python")
# print("content of lst=",lst)
# print("Type of lst=",type(lst))
# print("---------------------------------")
# a=np.array(lst,object)
# print("Content of a=\n",a)
# print("Data Type of a=",a.dtype)
# print(type(a))
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

# import numpy as np
# s={10,20,30,40,50,60}
# a=np.array(s)
# print("Content of a=\n",a)
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# import numpy as np
# d={10:1.2,20:2.2,30:3.3,40:4.4}
# a=np.array(d)
# print("Content of a=\n",a)
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)