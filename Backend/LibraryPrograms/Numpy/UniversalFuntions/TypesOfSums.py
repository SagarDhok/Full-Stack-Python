

#!add()
#*syntax = varname = numpy.add(ndaary1,ndarr2)
#* Doesnt Support axis addtion
#^========================================================================================
#* Element Wise Addition
# #* 1D
# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# newarr = np.add(arr1,arr2)
# print(newarr)

#*2D
# import numpy as np
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2 = np.array([5,6,7,8]).reshape(2,2)
# newarr = np.add(arr1,arr2)
# print(arr1)
# print(arr2)
# print(newarr)
#^========================================================================================



#! sum()
#*syntax = varname = numpy.sum([ndaary1,ndarr2]axis = none)
#*All Element Addtion 
#* Support axis wise Addtion
#^========================================================================================


#*1D
# import numpy as np
# arr1 = np.array([1,2,3])
# newarr = np.sum(arr1)   
# print(newarr)


#*1D
# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([5,6,7])
# newarr = np.sum([arr1,arr2])   #*list madhe pass karan lagete
# print(newarr)

#*2D
# import numpy as np
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2 = np.array([1,2,3,4]).reshape(2,2)
# print(arr1)
# print(arr2)
# newarr  = np.sum([arr1,arr2])
# print(newarr)


#*2D Axis Wise 
#* statistics and sum cumsum same row : axis = 1 , col : axis =0
# import numpy as np
# arr1 = np.array([1, 2, 3,4]).reshape(2,2)
# arr2 = np.array([13,43,9,3]).reshape(2,2)
# print("MATRIX - A")
# print(arr1)
# print("-"*50)
# print("MATRIX - B")
# print(arr2)
# print("-"*50)
# newarr = np.sum([arr1,arr2],axis=1)    #* Col-Col Elements Considers 
# print("MATRIX - C")
# print(newarr)


# *2D Axis Wise 
# import numpy as np
# arr1 = np.array([1, 2, 3,4]).reshape(2,2)
# arr2 = np.array([13,43,9,3]).reshape(2,2)
# print("MATRIX - A")
# print(arr1)
# print("-"*50)
# print("MATRIX - B")
# print(arr2)
# print("-"*50)
# newarr = np.sum([arr1,arr2],axis=0)    #*Row-Row Elements Considers
# print("MATRIX - C")
# print(newarr)


# *1D Axis Wise  - row
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.sum([arr1,arr2],axis=1)
# print(newarr)

# *1D Axis Wise - column
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.sum([arr1,arr2],axis=0)
# print(newarr)
#^========================================================================================




#! cumsum()
#*syntax - varname = np.cumsum(ndarray1)
#*syntax - varname = np.cumsum([ndarray1,ndarray2])
#^========================================================================================
# import numpy as np
# a = np.array([1,2,3])
# arr = np.cumsum(a)
# print(arr)

# import numpy as np
# a = np.array([1,2,3])
# b = np.array([5,6,7])
# c = np.cumsum([a,b])
# print(c)


#*2D
# import numpy as np
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2 = np.array([1,2,3,4]).reshape(2,2)
# newarr  = np.cumsum([arr1,arr2])
# print(arr1)
# print(arr2)
# print(newarr)
#!-----------

#*2D Axis Wise 
#* append insert and delete same row : axis = 0 , col : axis =1
# import numpy as np
# arr1 = np.array([1, 2, 3,4]).reshape(2,2)
# arr2 = np.array([13,43,9,3]).reshape(2,2)
# print("MATRIX - A")
# print(arr1)
# print("-"*50)
# print("MATRIX - B")
# print(arr2)
# print("-"*50)
# newarr = np.cumsum([arr1,arr2],axis=1)    #* row Elements Considers 
# print("MATRIX - C")
# print(newarr)


# *2D Axis Wise 
# import numpy as np
# arr1 = np.array([1, 2, 3,4]).reshape(2,2)
# arr2 = np.array([13,43,9,3]).reshape(2,2)
# print("MATRIX - A")
# print(arr1)
# print("-"*50)
# print("MATRIX - B")
# print(arr2)
# print("-"*50)
# newarr = np.cumsum([arr1,arr2],axis=0)    #*Row-Row Elements Considers
# print("MATRIX - C")
# print(newarr)


# *1D Axis Wise  - column
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.cumsum([arr1,arr2],axis=1)
# print(newarr)

# # *1D Axis Wise - row
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.cumsum([arr1,arr2],axis=0)
# print(newarr)