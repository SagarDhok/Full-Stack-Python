

#! <7>.identity()
#* Syntax:    varname=numpy.identity(N,dtype)
#*dtype default float aste
#^----------------------------------------------------------------------------------------
#*Create 2x2 Identity OR Unit Matrix
# import numpy as np
# lst = [1,0,0,1]
# a = np.array(lst).reshape(2,2)
# print(a)

# import numpy as np
# lst = [[1,0],[0,1]]
# a = np.array(lst)
# print(a)


#* Create ndarray object with 2 x 2 identity OR Unit Matrix
# import numpy as np
# a = np.identity(2)
# print(a)
# print(type(a))
# print(a.dtype)

# import numpy as np
# a = np.identity(2,dtype=int)
# print(a)
# print(type(a))
# print(a.dtype)


# import numpy as np
# a = np.identity(2,int)
# print(a)
# a.shape=(4,)
# print(a)

#* Create ndarray object with 3 x 3 identity OR Unit Matrix
# import numpy as np
# a = np.identity(3,dtype= int)
# print("Unit Matrix")
# print(a)
# print("Dim of a=",a.ndim)
# print("Shape of a=",a.shape)


#* Create ndarray object with 6 x 6 identity OR Unit Matrix
# import numpy as np
# a = np.identity(6,dtype= int)
# print("Unit Matrix")
# print(a)
# print("Dim of a=",a.ndim)
# print("Shape of a=",a.shape)

#* Create ndarray object with 10 x 10 identity OR Unit Matrix
# import numpy as np
# a = np.identity(10,dtype=int)
# print("unit matrix")
# print(a)
# print("Dimension of a = ,",a.ndim)
# print("Shape of a = ",a.shape)
# print("Size of a = ",a.size)

# p = 1
# for i in range(len(a)):
#      p = p*a[i,i]
# print(f"Product of principle diagonal element = {p}")



# a.shape = (100,)
# print(a)
# print("Dimension of a = ",a.ndim)
# print("Shape of a = ",a.shape)
# print("Size of a = ",a.size)






# import numpy as np
# p = 1
# lst = [[1,0,0],[0,1,0],[0,0,1]]
# a  = np.array(lst)
# for i in range(len(a)):
#      p = p*a[i,i]
# print("product = ",p)

# import numpy as np
# p = 1
# lst = [[1,0,0],[0,1,0],[0,0,1]]
# for i in range(len(a)):
#      # p = p*lst[i][i]
#      print(lst[i][i])
# # print("product = ",p)

# import numpy as np
# lst = [10,20,30,40,50,60]
# a = np.array(lst).reshape(2,3)
# a.shape=(6,)
# print(a)



# import numpy as np
# a = np.identity(3,dtype=int)
# print("unit matrix")
# print(a)
# print("Dimension of a = ,",a.ndim)
# print("Shape of a = ",a.shape)
# print("Size of a = ",a.size)


# a.shape = (9,)
# print(a)
# print("Dimension of a = ",a.ndim)
# print("Shape of a = ",a.shape)
# print("Size of a = ",a.size)