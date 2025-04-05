

#! <10>vstack()
#* Syntax:  varname=numpy.vstack((ndarray1,ndarray2))
#* column number must be same
#^----------------------------------------------------------------------------------------
# import numpy as np
# a1 = np.array([[10,20,30],[40,50,60]])
# print("array 1")
# print(a1)
# a2 = np.array([[1,2,5],[3,8,5],[4,5,7]])
# print("array 2")
# print(a2)


# #* merge array1 and array2 in array3
# a3 = np.vstack((a1,a2))   #*tuple madhe pahijet
# print("array 3")
# print(a3)

# a4 = np.vstack((a2,a1))   #*tuple madhe pahijet
# print("array 4")
# print(a4)

#^----------------------------------------------------------------------------------------
# import numpy as np
# a = np.arange(12).reshape(3,4)
# print(a)

# b= np.ones((2,4),dtype=int)
# print(b)

# c= np.zeros((5,4),dtype=int)
# print(c)


# x = np.vstack((a,b,c))
# print(x)

# x = np.vstack((c,b,a))
# print(x)