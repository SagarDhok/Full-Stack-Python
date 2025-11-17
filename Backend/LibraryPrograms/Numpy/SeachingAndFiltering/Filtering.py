

#^----------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("Content of a")
# print(a)


#* get all Even Numbers
# ba = a%2==0
# print(ba,type(ba))

# print("List of even values")
# print(a[ba])


#* Get all Odd Elements
# ba = a%2!=0
# print(ba,type(ba))

# print("List of odd values")
# print(a[ba])
#^----------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
# print("Content of a")
# print(a)

#* Get all +Ve Values
# ba = a>0             # here ba is called Boolean Array
# print(a[ba])         #Pass Boolean Array to ndarray object

#*or

# print(a[a>0])


#*Get all the negative values 
# ba = a<0       # here ba is called Boolean Array
# print(a[ba])   #Pass Boolean Array to ndarray object  

#*or 
# print(a[a<0])
#^----------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("Content of a")
# print(a)

#* Get Multiples of 3 
# ba = a%3==0
# print(a[ba])

#*or
# print(a[a%3==0])

#* Get Multiples of 3 and 5
# ba = (a%3==0) & (a%5==0)   # * Here & is called Bitwise AND Operator 
# print(a[ba])

# print(a[(a%3==0) & (a%5==0)])

#^=======================================================================================
#! Filtering with where()
#! 1D
# import numpy as np
# a=np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("Content of a")
# print(a)

#* Get Multiple 4 by using numpy.where()
# indx = np.where(a%4==0)
# print(indx,type(indx))

# for i in indx[0]:                  
     #  print(i)          3index dete   
     # print(a[i])        

                        
#^----------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
# print("Content of a")
# print(a)

#* Get +Ve Elements by using numpy.where()
# indx = np.where(a>0)
# print(indx,type(indx))

# print("positive element indices")
# print(indx[0])

# print("positive elements")
# for i in indx[0]:
#      print(a[i])


#* Get -Ve Elements by using numpy.where()
# indx= np.where(a<0)
# print(indx,type(indx))

# print("Negative element indices")
# print(indx[0])

# print("Negative Elements")
# for i in indx[0]:
#      print(a[i])
#^----------------------------------------------------------------------------------------
#! 2D

import numpy as np
a=np.random.randint(10,25,size=(3,3))
print("Content of a")
# print(a)
a.shape = (9,)        #* 1 d madhe convert karn lagete
# print(a)

#* Get the Elements More than 15 with Filtering
# print(a[a>15])

#* Get the Elements Less than  or equal 15 with Filtering
# print(a[a<=15])

#* Get the Elements More than 15 with numpy.where()
# indx = np.where(a>15)
# print(indx,type(indx))
# for i in indx[0]:
#      print(a[i])

#*Get the Elements Less than  or equal 15 with numpy.where()
# indx = np.where(a<=15)
# print(indx,type(indx))
# for i in indx[0]:
#      print(a[i])
#^----------------------------------------------------------------------------------------
#! Working with Missing Data--which is Represented with np.NaN OR None

#* replacing missing value with 0
# import numpy as np
# data = np.array([10,23,45,None,54])
# print("given data")
# print(data)
# data = np.where(data==None,0,data)
# print(data)

#^----------------------------------------------------------------------------------------
#!examples on numpy.extract(Test Cond, Ndarray Object)
#* Filter missing values
# import numpy as np
# data = np.array([20,34,43,None,43])
# print("given data")
# print(data)

# print("Data without missing values")
# data = np.extract(data!=None,data)
# print(data)

# import numpy as np
# a=np.array([10,32,54,2,36,76,53,2,11,54,15])
# print(a)

#*Get the Values which are more than 20
# morethan20 = np.extract(a>20,a)
# print("Values which are more than 20")
# print(morethan20)

#* get values which are less than 20
# lessthan20 = np.extract(a<20,a)
# print("values which are less than 20")
# print(lessthan20)

# import numpy as np
# a = np.array([1, 2, 3, 4])
# x = np.array([10, 20, 30, 40])
# y = np.array([100, 200, 300, 400])
# print(np.where(a > 2, x, y))


