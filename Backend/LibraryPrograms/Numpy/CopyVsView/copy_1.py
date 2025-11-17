
#! copy() - shallow copy
#^-----------------------------------------------------------------------------------------
#* Syntax -1
# import numpy as np
# a= np.array([10,20,30,40])
# print(a,id(a),type(a))

# b= a.copy()
# print(b,id(b),type(b))

# a = np.append(a,1000)
# b = np.append(b,2000)

# print(a,id(a),type(a))
# print(b,id(b),type(b))

# print(b.base)
#^-----------------------------------------------------------------------------------------
#* syntax -2 
# import numpy as np
# a = np.array([10,20,30,40])
# print(a,id(a),type(a))

# b = np.copy(a)
# print(b,id(b),type(b))

# a[0]= 500
# b[0] = 1000

# print(a,id(a),type(a))
# print(b,id(b),type(b))

# print(b.base)
#^-----------------------------------------------------------------------------------------
#!Deep copy 

# import numpy as np
# a = np.array([10,20,30,40])
# print(a,id(a),type(a))

# b = a
# print(b,id(b),type(b))

# a[0] = 200
# b[-1] = 300


# print(a,id(a),type(a))
# print(b,id(b),type(b))

# print(b.base)

#^-----------------------------------------------------------------------------------------