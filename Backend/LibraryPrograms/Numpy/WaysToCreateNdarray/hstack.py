


#! <9>.hstack()
#* Syntax:  varname=numpy.hstack((ndarray1,ndarray2))
#* rows number must be same
#^----------------------------------------------------------------------------------------
# import numpy as np
# a1 = np.array([[10,20,30],[40,50,60]])
# print("array 1")
# print(a1)
# a2 = np.array([[1,2],[3,8]])
# print("array 2")
# print(a2)

#* merge array1 and array2 in array3
# a3 = np.hstack((a1,a2))   #*tuple madhe pahijet
# print("array 3")
# print(a3)

# a4 = np.hstack((a2,a1))   #*tuple madhe pahijet
# print("array 4")
# print(a4)
#^----------------------------------------------------------------------------------------
# import numpy as np
# a = np.arange(9).reshape(3,3)
# print(a)

# b= np.ones((3,4),dtype=int)
# print(b)

# c= np.zeros((3,6),dtype=int)
# print(b)

# x = np.hstack((a,b,c))
# print(x)

# x = np.hstack((b,a,c))
# print(x)