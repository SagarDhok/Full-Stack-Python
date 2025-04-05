
#^----------------------------------------------------------------------------------------
# import numpy as np
# a = np.random.randint(10,200,size=(2,3,3))
# print(a)
# print(a.ndim)
# print(a.shape)

# a.shape = (18,)
# print(a)
# print(a.ndim)
# print(a.shape)
#^----------------------------------------------------------------------------------------
#! flatten()
#* similar to shallow copy different id and does not affect each other 
# import numpy as np
# a = np.random.randint(10,200,size=(2,3,3))
# print(a,id(a),type(a))
# print(a.ndim)
# print(a.shape)

# #*flatten the 3arrayobj into 1darray object
# #*varname=ndarrayobj.flatten()
# print("-"*20)
# b = a.flatten()
# print(b,id(b),type(b))
# print(b.ndim)
# print(b.shape)

# print("Base of flattend object  (copied object): ",b.base)



# import numpy as np
# a  = np.random.randint(20,100,size= (2,3,3))
# print(a,id(a))

# b = a.flatten()
# print(b,id(b))

# a[0,0,0] = 1000
# print(a,id(a))
# print(b,id(b))


# import numpy as np
# a  = np.random.randint(20,100,size= (2,3,3))
# print(a,id(a))

# b = a.flatten()
# print(b,id(b))

# b[0] = 2000
# print(a,id(a))
# print(b,id(b))
#^----------------------------------------------------------------------------------------



