
#!sort() 
#*syntax = varname = np.sort(ndarrayobj)
#^=======================================================================================
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print(a)
# print(np.sort(a))
# print(a)


#* updating array itself
# import numpy as np
# a=np.array([10,2,13,14,25,16,-1,0,23])
# print(a)
# a = np.sort(a)
# print(a)

#* sorting  in decending order  and finding min and max
# import numpy as np
# a=np.array([10,2,13,14,25,16,-1,0,23])
# a = np.sort(a)[::-1]
# print(a)
# print("Max Element : ",a[0])
# print("Second Max Element : ",a[1])
# print("Min Element : ",a[-1])
# print("Second Min Element : ",a[-2]) 

#^-----------------------------------------------------------------------------------------
#*Sorting of 2-D Data 
#*statistics and this is same row  : axis = 1 and column axis :0 
# import numpy as np
# a=np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("GIVEN MATRIX ")
# print(a)
# print("-"*50)
# print("Sorted array ")
# a= np.sort(a)     #*sorting base on rows # By Deafult sort the 2D Array Data on the basis of Row
# print(a)


# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given Matrix ")
# print(a)
# print("-"*50)
# a= np.sort(a,axis = 1)  #*sorting base on rows 
# print("Sorted Array ")
# print(a)


#* By Deafult sort the 2D Array Data on the basis of Row
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,3]).reshape(3,3)
# print("Given Array") 
# print(a)
# print("-"*50)
# print("Sorted Array")
# a = np.sort(a,axis=0) #* sort the 2D Array Data on the basis of Column
# print(a)  


#^-----------------------------------------------------------------------------------------
#*Sorting complete data of 2-D Data 
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given Matrix")
# print(a)
# print("-"*50)
# print("Sorted Matrix ")
# a =a.flatten()
# a = np.sort(a)
# a.shape=(3,3)
# print(a)


#*Sorting complete data of 2-D Data in reverse order 
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given Matrix")
# print(a)
# print("-"*50)
# a = a.flatten()
# a = np.sort(a)[::-1].reshape(3,3)
# print("Sorted Arary ")
# print(a)

#^=======================================================================================
# import numpy as np
# a  = np.array(["banana","cherry","apple"])
# a = np.sort(a)
# print(a)

# import numpy as np
# a = np.sort([False,True,True,False])
# print(a)