

#!split()
#*syntax : varname = numpy.split()
#*same like append () insert(), delete(), 
#* axis 1 = column
#* axis 0 = row  
#^======================================================================================
#! 1D Array

# #* Splitting the array into 2 equal parts along the first axis (axis=0)
# import numpy as np
# arr = np.arange(6)
# print("Array")
# print(arr)
# result = np.split(arr,2)
# print("Result After numpy.split()")
# print(result)
# print(result[0])
# print(result[1])

# #* Splitting the array into 2 equal parts along the first axis (axis=0)
# import numpy as np
# arr = np.arange(6)
# print("Array")
# print(arr)
# result= np.split(arr,2)
# print("Result after np.split()")
# print(result)
# for arr in result:
#      print(arr,end=",")

#*unequal nahi karat
# #* Splitting the array into 2 equal parts along the first axis (axis=0)
# import numpy as np
# array = np.arange(7)
# print("Array")
# print(array)
# result = np.split(array,2)
# print("Result after numpy.split()")
# print(result)

#! 2D Array
# * Splitting the array into 3 equal parts along the second axis (axis=1)
# import numpy as np
# arr = np.array([[3,2,1],[8,9,7],[4,6,5]]) 
# print("2D array")
# print(arr) 
# result = np.split(arr,3,axis=1)
# print("result after numpy,split() along wiht axis = 1")
# print(result)


#* Splitting the array into 3 equal parts along the First axis (axis=0)
# import numpy as np
# arr = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
# print("2D array")
# print(arr)
# result = np.split(arr,3,axis=0)
# print("result after np.split()")
# print(result)




#^======================================================================================
#!array_split()
#*syntax : varname = numpy.array_split()
#^======================================================================================
# #! 1D Array
# import numpy as np
# arr = np.arange(13)
# print("Array")
# print(arr)
# # * Splitting the array into 4 unequal parts along the first axis (axis=0)
# result = np.array_split(arr,4)
# print("result after numpy.array_split()")
# print(result)

# #* Splitting the array into 4 equal parts along the first axis (axis=0)
# import numpy as np
# arr = np.arange(12)
# print("Array")
# print(arr)
# result = np.array_split(arr,4)
# print(result)

#!2D
# #! Splitting the array into 2 unequal parts along the first axis (axis=0)
# import numpy as np
# a = np.random.randint(10,99,size=(3,3))
# print("Array")
# print(a)
# x = np.array_split(a,2,axis=0)
# print("result after np.array_spilit()")
# print(x)

#! Splitting the array into 2 unequal parts along the second axis (axis=1)
# import numpy as np
# a = np.random.randint(10,99,size=(3,3))
# print("Array")
# print(a)
# x = np.array_split(a,2,axis=1)
# print("result after np.array_spilit()")
# print(x)
#^======================================================================================

#!vsplit()  #*horizontal split()
#*syntax : varname = numpy.vsplit()
#^======================================================================================

#* Vertical splitting into 2 subarrays along axis=0
# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print("Matrix")
# print(matrix)
# result = np.vsplit(matrix,2)   #& OR   result=np.split(matrix,2,axis=0)
# print("result after np.vsplit()")
# print(result)


# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print("Matrix")
# print(matrix)
# result = np.split(matrix,2,axis=0)   #& result=np.vsplit(matrix, 2)
# print("result after np.vsplit()")
# print(result)


#^======================================================================================

#!hsplit()  #*vartical split()
#*syntax : varname = numpy.hsplit()
#^======================================================================================
#& horizontally splitting into 2 subarrays along axis=1
# import numpy as np
# array = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
# print("Matrix")
# print(array)
# x = np.hsplit(array,2)   #&or  np.split(array, 2,axis=1)
# print("result after np.hsplit()")
# print(x)
# print("First Subarray : \n",x[0])
# print("Second Subarray : \n",x[1])

# import numpy as np
# array = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
# print("Matrix")
# print(array)
# x = np.split(array, 2,axis=1)   #&or  np.hsplit(array,2)
# print("result after np.hsplit()")
# print(x)
# print("First Subarray : \n",x[0])
# print("Second Subarray : \n",x[1])

#^======================================================================================

#!dsplit()
#*syntax : varname = np.dsplit()
#^======================================================================================
# import numpy as np
# arr = np.arange(24).reshape(2, 3, 4)
# print("MAtrix")
# print(arr)
# #& Splitting along axis=2 (third axis)
# result = np.dsplit(arr,2)  #&np.split(arr,2,axis=2)
# print("result after np.dsplit()")
# print(result)

# import numpy as np
# arr = np.arange(24).reshape(2, 3, 4)
# print("MAtrix")
# print(arr)
# #& Splitting along axis=2 (third axis)
# result = np.split(arr,2,axis=2)
# print("result after np.dsplit()")
# print(result)
#^======================================================================================
# import numpy as np
# arr = np.arange(16).reshape(4,4)
# print("ORIGiNAL ARRAY")
# print(arr)

# print("Reversed Array")
# print(arr[::-1])


#*& get diagonal element
# x = arr[[0,1,2,3],(0,1,2,3)]
# print("Diagonal elements",x)   #*Internally Taken as (0,0),(1,1),(2,2),(3,3)

#&get Diagnol Elements without Advanced Slicing
# x = np.diag(arr)
# print(x)
# print(x[::-1])



#^======================================================================================
# import numpy as np
# arr = np.arange(12).reshape(2,6)
# print(arr)
# print(arr.shape)

#& Get the Transpose of ndarray row to column , column to row
# print(arr.T)
# print(arr)

#&updating arr itself
# arr = arr.T
# print(arr)
# print(arr.shape)


# import numpy as np
# arr = np.arange(12).reshape(2,6)
# print(arr)
# print(arr.shape)

# #& Get the Transpose of ndarray row to column , column to row
# # print(np.transpose(arr))
# # print(arr)

# #&updating arr itself
# arr = np.transpose(arr)
# print(arr)
# print(arr.shape)


#^======================================================================================