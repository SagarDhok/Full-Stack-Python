
#^----------------------------------------------------------------------------------------
#! appending the Data to ndarray object by using append()
# import numpy as np
# a = np.array([10,20,30,40,50,60])
# print(a)
# print(np.append(a,100))
# print(a)

#*a madhi store karaych asel tr
# import numpy as np
# a = np.array([10,20,30,40,50,60])
# print(a)
# a = np.append(a,200)
# print(a)

# #!Appending More than One Value
# a = np.append(a,[55,66,77])
# print(a)
#^----------------------------------------------------------------------------------------
#*Here axis=0 Represents Row 
#*Here axis=1 Represents column

# import numpy as np
# a = np.array([10,20,30,40,50,60]).reshape(3,2)
# print("Before Appending  : \n",a)
# #* Adding row
# a = np.append(a,[[15,25]],axis = 0)
# print("After Appending  : \n",a)

# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)
# print("Before Appending : \n",a)

# #* Adding row
# a = np.append(a,[[11,22,33]],axis = 0)
# print(a)


# # #*Adding Column
# a = np.append(a,[[15],[15],[15],[15]],axis = 1)
# print(a)

# # #* Adding row
# a = np.append(a,[[99,88,77,66]], axis=0)
# print(a)

# # #*Adding Column
# a = np.append(a,[[11],[12],[13],[14],[16]],axis = 1)
# print(a)
#^----------------------------------------------------------------------------------------