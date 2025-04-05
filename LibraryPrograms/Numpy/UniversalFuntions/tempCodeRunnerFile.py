import numpy as np
arr1 = np.array([1, 2, 3, 4]).reshape(2,2)
arr2 = np.array([5, 6, 7, 8]).reshape(2,2)
print(arr1)
print("---------")
print(arr2)
print("---------")
newarr = np.prod([arr1,arr2],axis=1)  #*Here axis=1 Represents Row Product
print(newarr)
