# ^--------------------------------------------------------------------------------------
#! Steps for Advanced Indexing on 1-D
# *Step-1: Identify the Indices of Elements and taken them in Traditional object of Python or ndarray obj
# *Step-2: Pass the Traditional Object OR Ndarray Object with Idices of Elements to the NDArray Object

# import numpy as np
# a=np.array([10,20,30,40,50,60,70])
# print("content of a")
# print(a)

# Step-1: Identify the Indices of 10 40 50
# lst=[0,3,4]  # OR tpl=(0,3,4)
# Step-2: Pass [0,3,4] to ndarray object--a
# print(a[lst])

# or

# #OR
# Step-1: Identify the Indices of 10 40 50
# b=np.array([0,3,4])
# Step-2: Pass ndarray object b to ndarray object--a
# a[b]


# print(a[[0,3,4]])


# * get 70 60 and 20 and 10
# print(a[[-1,-2,1,2]])

# print(a[np.array([-1,-2,1,2])])


# &--------------------------------------------------------------------------------------
# import numpy as np
# a=np.arange(0,25)
# print(a)


# 0,10,13,15,24-----Indices are 0,10,13,15,24
# print(a[[0,10,13,15,24]])

# import numpy as np
# a=np.random.randint(1,100,size=25)
# print(a)

# for i,v in enumerate(a):
#      print(i,"-->",v)

# &--------------------------------------------------------------------------------------
# ^--------------------------------------------------------------------------------------

# Steps for Advanced Indexing with 2-D
# Step-1: Identify the Row Indices of Elements and places them in Traditional Python Object/ndarray object
# Step-2: Identify the Column Indices of Elements and places them in Traditional Python Object/ndarray object
# Step-3: Pass Row Indices and Column Indices to ndarray Object

# import numpy as np

# a = np.array([
#     [57, 61, 98, 52, 94],
#     [90, 27, 28, 17, 37],
#     [69, 31, 27, 16, 64],
#     [98, 71, 85, 86, 60],
#     [49, 45, 33, 84, 31]
# ])
# print(a)

# * Get the Elements 98 and 31
# rowindex = [0,4]
# colindex = [2,4]
# print(a[rowindex,colindex])

# print(a[(0,4),(2,4)])

# * Get the Principle Diagnol Elements---57,27,27,86 and 31
# print(a[[0,1,2,3,4],[0,1,2,3,4]])

# * Get the Elements 49,71,27,17 and 94
# print(a[np.array([4,3,2,1,0]),np.array((0,1,2,3,4))])
# print(a[np.array([-1,-2,-3,-4,-5]),np.array((0,1,2,3,4))])

# *Get the Elements 57,17,45
# print(a[[-5,-4,-1],[-5,-2,-4]])
# print(a[[0,1,4],[0,3,1]])

# ^--------------------------------------------------------------------------------------

# import numpy as np

# a = np.array(
#     [
#         [[47, 98, 63], [78, 42, 41], [97, 98, 74]],
#         [[20, 20, 18], [3, 27, 86], [11, 60, 99]],
#         [[67, 97, 83], [4, 75, 6], [14, 36, 87]],
#     ]
# )

# print(a)

#* get 47 3,14
# print(a[[0,1,2],[0,1,2],[0,0,0]])

#*Get 47 , 74 , 83 and 14
# print(a[np.array([0,0,2,2]),np.array((0,2,0,2)),np.array([0,2,2,0])])