
#^----------------------------------------------------------------------------------------
#*Basic Indexing in 1-D---Obtains Single Element
#*Syntax: ndarrayobj[Index]
 
# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90])
# print(a)

# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[len(a)-1])
# print(a[-2])
# print(a[-len(a)])

#^----------------------------------------------------------------------------------------
#* Basic Indexing in 2-D(Matrix)---Obtains Single Element
#* Syntax-2: ndarraytobj[RowIndex][ColIndex]
#*  Here RowIndex and ColIndex can be either +ve or -ve

# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,47,67,43])
# a.shape=(3,4)
# print(a)


#*get the element 20
# print(a[0,1])
# print(a[-3,-3])
# print(a[0,-3])
# print(a[-3,1])
# print(a[0][1])
# print(a[-3][-3])
# print(a[0][-3])
# print(a[-3][1])


# print(a[0])
# print(a[-1])
# print(a[2])

#^----------------------------------------------------------------------------------------
#*Basic Indexing in n-D(MatrixNumber, Rows, Cols)---Obtains Single Element
#*Syntax-3: ndarraytobj[MatrixIndex,RowIndex][ColIndex]
#* Here Matrix Index , RowIndex and ColIndex can be either +ve or -ve

# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,47,67,43]).reshape(2,3,2)
# print(a)

#* Get the Element 40
# print(a[0,1,1])
# print(a[-2,-2,-1])
# print(a[0,-2,-1])
# print(a[-2,1,1])
# print(a[0][1][1])
# print(a[-2][-2][-1])
# print(a[0][-2][-1])
# print(a[-2][1][1])
# print(a[0,1][1]) 
# print(a[-2][-2,-1])
# print(a[0,-2][-1])
# print(a[-2][1,1])

#*Get Complete First Matrix with Indexin
# print(a[0])
# print(a[-2])

#* Get Complete Second  Matrix with Indexing
# print(a[1])
# print(a[-1])

#^----------------------------------------------------------------------------------------
