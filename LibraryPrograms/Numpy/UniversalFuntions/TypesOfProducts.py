

#!Prod()
#*all element multiplication
#*syntax : np.prod(ndarrayobj)
#*syntax : np.prod([ndarrayobj1,ndarrobj2],axis=none)
#*here similar like statisics operation  column : axis - 0 and row : axis = 1
#^========================================================================================
#* 1D array
# import numpy as np
# a = np.array([1,2,3,4])   
# b = np.prod(a)
# print(b)

#* 1D array
# import numpy as np
# a = np.array([1,2])   
# b = np.array([1,2])   
# c = np.prod([a,b])
# print(c)

#* 2D array
# import numpy as np
# arr1 = np.array([1, 2, 3, 4]).reshape(2,2)
# arr2 = np.array([5, 6, 7, 8]).reshape(2,2)
# newarr = np.prod([arr1,arr2])
# print(newarr)


#* 2D array axis wise row
# import numpy as np
# arr1 = np.array([1, 2, 3, 4]).reshape(2,2)
# arr2 = np.array([5, 6, 7, 8]).reshape(2,2)
# print(arr1)
# print("---------")
# print(arr2)
# print("---------")
# newarr = np.prod([arr1,arr2],axis=1)  #*Here axis=1 Represents Row Product
# print(newarr)


#* 2D array
# import numpy as np
# arr1 = np.array([1, 2, 3, 4]).reshape(2,2)
# arr2 = np.array([5, 6, 7, 8]).reshape(2,2)
# print(arr1)
# print("---------")
# print(arr2)
# print("---------")
# newarr = np.prod([arr1,arr2],axis=0)  #*Here axis=1 Represents col Product
# print(newarr)


#*Product Over an Axis
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5]])
# print("----------------------------------")
# print("Given Array")
# print(arr)
# print("----------------------------------")
# x = np.prod(arr,axis=0) #*Here axis=0 Represents Column Product
# print(x)


#*Product Over an Axis
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5]])
# print("----------------------------------")
# print("Given Array")
# print(arr)
# print("----------------------------------")
# x = np.prod(arr,axis=1) # Here axis=1 Represents Row Product
# print(x)
#^========================================================================================


#! cumulative product - cumprod()
#*syntax  : varname = np.cumprod(ndarrayobj1)
#^========================================================================================
#* 1D array
# import numpy as np
# arr = np.array([5, 6, 7, 8])
# newarr = np.cumprod(arr)
# print(newarr)


#*2D array
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.cumprod(arr)
# print(newarr)



#*2D array - axis wise 
# import numpy as np
# arr = np.array([ [1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.cumprod(arr,axis=1)  #*Here axis=1 Represents Cumulative Row Product 
# print(newarr)

#*2D array - axis wise 
# import numpy as np
# arr = np.array([ [1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.cumprod(arr,axis=0)    #*Here axis=o Represents Cumulative Col Product 
# print(newarr)


# import numpy as np
# a  = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# c = np.cumprod([a,b],axis = 1)    #*Here axis=1 Represents Cumulative Row Product 
# print(c)


# import numpy as np
# a  = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# c = np.cumprod([a,b],axis = 0) #*Here axis=o Represents Cumulative Col Product 
# print(c)

#^========================================================================================

# import numpy as np
# arr = np.array([ [1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.prod(arr,axis=0)    #*Here axis=o Represents Cumulative Col Product 
# print(newarr)



# import numpy as np
# arr = np.array([ [1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.prod(arr,axis=0)    #*Here axis=o Represents Cumulative Col Product 
# print(newarr)


# import numpy as np
# arr = np.array([ [1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.sum(arr,axis=1) #row      
# print(newarr)          


# import numpy as np
# arr = np.array([ [1,2,3],[3,4,5],[2,3,5]])
# print(arr)
# newarr= np.sum(arr,axis=0) #col      
# print(newarr)          
