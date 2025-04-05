
#! <1>.arange()
#*numpy.arange(Value)----------------> 0 to Value-1 with Default Step     +1
#*numpy.arange(Start,Stop)---------->Start to Stop-1 with Default Step  +1
#*numpy.arange(Start,stop,Step)----> Start to Stop-1 with Programmer Choice Step
#^----------------------------------------------------------------------------------------
#* numpy.arange(Value)----------------> 0 to Value-1 with Default Step     +1
#* genarte range of values from 0 to 10

# import numpy as np
# a = np.arange(9)
# a.shape= (3,3)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# import numpy as np
# a = np.arange(11,dtype = float)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)
#^----------------------------------------------------------------------------------------
#* numpy.arange(Value)----------------> 0 to Value-1 with Default Step     +1
#* genarte range of values from 0 to 6
# import numpy as np
# a = np.arange(0,6,dtype =float)
# a.shape = (3,2)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

# import numpy as np
# a = np.arange(0,6,dtype =float)
# a.shape = (3,2)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#^----------------------------------------------------------------------------------------
#* numpy.arange(Start,Stop)---------->Start to Stop-1 with Default Step  +1
#*generate the values from 10 to 20

# import numpy as np
# a = np.arange(10,21,dtype=float)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# import numpy as np
# a = np.arange(10,21,dtype = float)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#^----------------------------------------------------------------------------------------
#* numpy.arange(Start,stop,Step)----> Start to Stop-1 with Programmer Choice Step
#* Generate the range of values as 10 12 14 16 18 20 22 24 26

# import numpy as np
# a = np.arange(10,27,2)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)
#^----------------------------------------------------------------------------------------
#*Generate the range of values as 10 12 14 16 18 20 22 24 26 with Matrix Format
# import numpy as np
# # a = np.arange(10,27,2).reshape(3,3)
# a = np.arange(10,27,2)
# a.shape = (3,3)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)
#^----------------------------------------------------------------------------------------
#*Generate the range of values as 10 to 15 with Interval value 0.25 with Matrix Format

# import numpy as np
# a = np.arange(10,15,0.25)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)


# import numpy as np
# a = np.arange(10,15,0.25,dtype = float)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)
#^----------------------------------------------------------------------------------------
#* Generate the range of values as 10 to 15 with Interval value 0.25 with Matrix Format

# import numpy as np
# a = np.arange(10,15,0.25,dtype = float).reshape(5,4)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#^----------------------------------------------------------------------------------------
#*Generate the range of values as 10 to 15 with Interval value 0.25 with 3-D Matrix Format
# import numpy as np
# a = np.arange(10,15,0.25,dtype = float).reshape(2,5,2)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)