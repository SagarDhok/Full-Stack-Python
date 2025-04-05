

#! unique()
#* styntax  : varname   = np.unique(arr)
#^===============================================================================================
# import numpy as np
# arr = np.array([1,1,1,2,3,4,5,5,6,7])
# x = np.unique(arr)
# print(x,type(x))

#* 2d l flatten karte 
# import numpy as np
# arr = np.array([10, 10, 10, 20, 30, 20, 30, 10, 40,30])
# arr.shape=(2,5)
# print("Array")
# print(arr)
# print("----------------------------")
# x = np.unique(arr)
# print(x,type(x))


#^===============================================================================================

#! union1d()
#*syntax : np.union1d(ndarray1,ndarray2)
#^===============================================================================================
#! Find union of the following two set arrays:

# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("---------------------")
# print("Array-2")
# print(arr2)
# print("---------------------")
# newarr = np.union1d(arr1,arr2)
# print(newarr)
#^===============================================================================================


#!intersect1d()
#  #*syntax : np.intersect1d(ndarray1,ndarray2,assume_unique=True)
#^===============================================================================================
#! Find Intersection of the following two set arrays:
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("---------------------")
# print("Array-2")
# print(arr2)
# print("---------------------")
# newarr = np.intersect1d(arr1,arr2)
# print(newarr)


# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("---------------------")
# print("Array-2")
# print(arr2)
# print("---------------------")
# newarr = np.intersect1d(arr1,arr2,assume_unique=True)  #* just speed up the performance 
# print(newarr)
#^===============================================================================================

#!np.setdiff1d()
#  #*syntax : np.setdiff1d(ndarray1,ndarray2,assume_unique=True)
#^===============================================================================================
#! Find the difference of the set1 from set2:
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1 ")
# print(arr1)
# print("--------------")
# print("Array-2")
# print(arr2)
# print("---------------")
# newarr = np.setdiff1d(arr1,arr2,assume_unique=True)
# print(newarr)

#! Find the difference of the set2 from set1:
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("Arary-2")
# print(arr2)
# newarr = np.setdiff1d(arr2,arr1,assume_unique=True)
# print("Difference of array")
# print(newarr)

# print(arr1-arr2)
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2= np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("Array-2")
# print(arr2)
# print("Set diff array - substration")
# newarr = arr1-arr2
# print(newarr)

#^===============================================================================================
#!np.setxor1d()
#  #*syntax : np.setxor1d(ndarray1,ndarray2,assume_unique=True)
#^===============================================================================================
#! Find the symmetric difference of the set1 from set2:
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1 ")
# print(arr1)
# print("Array-2")
# print(arr2)
# print("Symmetric difference array")
# newarr = np.setxor1d(arr1,arr2,assume_unique=True)
# print(newarr)


#!Find the symmetric difference of the set1 from set2:
#*Formula1: np.setxor1d(set1, set2)-->for this use Bellow Statement
#* np.setdiff1d(np.union1d(set1,set2) , np.intersect1d(set1,set2) )
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("Array-2")
# print(arr2)
# print("Symmetric difference array")
# newarr = np.setdiff1d(np.union1d(arr1,arr2),np.intersect1d(arr1,arr2))
# print(newarr)

#& x
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("Array-2")
# print(arr2)
# print("Symmetric difference array")
# newarr = np.setdiff1d(np.intersect1d(arr1,arr2),np.union1d(arr1,arr2))   #& gives empty
# print(newarr)

#! Find the symmetric difference of the set1 from set2:
#* Formula1: np.setxor1d(set1, set2)-->for this use Bellow Statement
#* newarr = np.union1d(np.setdiff1d(set1,set2),np.setdiff1d(set2,set1))
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array-1")
# print(arr1)
# print("Array-2")
# print(arr2)
# newarr = np.union1d((np.setdiff1d(arr1,arr2)),(np.setdiff1d(arr2,arr1)))
# print("Symmetric difference array")
# print(newarr)

#^===============================================================================================