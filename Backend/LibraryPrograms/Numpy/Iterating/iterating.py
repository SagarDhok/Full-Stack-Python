
#* Iterate the Data from ndarray object by using Loops
#^----------------------------------------------------------------------------------------
#! 1-D array
# import numpy as np
# a = np.random.randint(10,20,size = 10)
# print("Content of a")
# print(a)
# print("Dimension of a  :",a.ndim)
# for i in a:
#      print(i)
#^----------------------------------------------------------------------------------------
#! 2-D array
# import numpy as np
# a = np.random.randint(10,20,size = (3,3))
# print("Content of a")
# print(a)
# print("Dimension of a  :",a.ndim)
# for row in a:
#    for col in row:
#       print(col)
#    print("-------")
#^----------------------------------------------------------------------------------------
# #! 3-D array
# import numpy as np
# a = np.random.randint(10,100,size =(2,3,3))
# print("Content of a ")
# print(a)
# print("Dimension of a ",a.ndim)

# for matrices in a :
#     for row in matrices: 
#         for col in row:
#             print(col)
#         print("---------")   
# 

# import numpy as np
# lst = [[[10,20],[40,50]],[[60,70],[80,90]]]
# a = np.array(lst)
# print(a)
# print("Dimension of a : ",a.ndim)

# for matrices in a:
#      for row in matrices:
#           for col in row:
#                print(col)

#^----------------------------------------------------------------------------------------
#! 4-D array
# import numpy as np
# a = np.random.randint(10,100,size =(2,2,2,2))
# print("Content of a ")
# print(a)
# print("Dimension of a ",a.ndim)


# for clusters in a:
#  for matrices in clusters:
#     for row in matrices: 
#         for col in row:
#            print(col)
#         print("-----------")
#^----------------------------------------------------------------------------------------
#! terate the Data from ndarray object by using nditer()
# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80,90])
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")
# for i in np.nditer(a):
#      print(i)
#^----------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")
# for i in np.nditer(a):
#      print(i)

# import numpy as np
# a=np.arange(3*3*3).reshape(3,3,3)
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")
# for i in np.nditer(a):
#      print(i)


# import numpy as np
# a=np.arange(2*2*2*2).reshape(2,2,2,2)
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")
# for i in np.nditer(a):
#      print(i)


# a.shape = (16,)
# print(a)
#^----------------------------------------------------------------------------------------
#! Iterate the Data from ndarray object by using ndenumerate() with Indices and values
#* 1-D
#^----------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,20,30,10,50,10,70,10,90])
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")

# for index,value in np.ndenumerate(a):
#      print(index[0],value)

# import numpy as np
# a=np.array([10,20,30,10,50,10,70,10,90])
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")

# for index,val in np.ndenumerate(a):
#      print(index,val)


# import numpy as np
# a=np.array([10,20,30,10,50,10,70,10,90])
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")

# for index,val in np.ndenumerate(a):
#      print(index[0],val)
#^----------------------------------------------------------------------------------------
#! Iterate the Data from ndarray object by using ndenumerate() with Indices and values
#* 2-D
# import numpy as np
# a=np.array([10,20,30,10,50,10,70,10,90]).reshape(3,3)
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")

# for index in np.ndenumerate(a):
#      print(f"Row:{index[0][0]}  Col:{index[0][1]}   Val:{index[1]}")


# import numpy as np
# a=np.array([10,20,30,10,50,10,70,10,90]).reshape(3,3)
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")

# for index in np.ndenumerate(a):
#      #* Find Thw Row Indices and Col Indices of 10 of 2D
#      if index[1]==10:
#       print(f"Row:{index[0][0]}  Col:{index[0][1]}   Val:{index[1]}")



# import numpy as np
# a=np.array([10,20,30,10,50,10,70,10,90]).reshape(3,3)
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)
# print("---------------------------------")

# for index,val in np.ndenumerate(a):
#      print(f"Row : {index[0]}   Column: {index[1]}    val : {val}")

#^----------------------------------------------------------------------------------------
#! Iterate the Data from ndarray object by using ndenumerate() with Indices and values
#* 3-D

# import numpy as np
# a=np.random.randint(10,20,size=(3,2,2))
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)

# print("MatrixNo\tRowNum\tColNum\tValue")
# for index in np.ndenumerate(a):
#      print(f"\t{index[0][0]} \t {index[0][1]} \t {index[0][2]}\t{index[1]}")



# import numpy as np
# a=np.random.randint(10,20,size=(3,2,2))
# print("content of a")
# print(a)
# print("Dim of a=",a.ndim)

# print("MatrixNo\tRowNum\tColNum\tValue")
# for index,val in np.ndenumerate(a):
#      print(f"\t{index[0]} \t {index[1]} \t {index[2]}\t{val}")


# import numpy as np
# from numpy import random as r
# a = r.randint(10,50,size=(3,3)) #* extra tuple yete
# print(a)
  
# print("-"*20)
# for i in np.ndenumerate(a):
#      print(i[0][0],i[0][1],i[1])
# print("-"*20)
# for i,v in np.ndenumerate(a):
#   print(i[0],i[1],v)

