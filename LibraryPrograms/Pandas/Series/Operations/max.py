

#!max
#*syntax : seriesobj.max()
#^===============================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-------------------------------------")
# print("Series - 1 ")
# print(a)
# print("-------------------------------------")
# #* Find Max Element by using seriesobj.max()
# maxv = a.max()
# print("Max Element : ",maxv)
#^===============================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-------------------------------")
# print("Series - 1")
# print(a)
# print("-------------------------------")
# a.sort_values(inplace = True)
# print("Max ELement : ",a.values[-1])
#^===============================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("---------------------------")
# print("Series - 1 ")
# print(a)
# print("---------------------------")
# a.sort_values(ascending=False,inplace= True)
# print("Max Element  ",a.values[0])
#^===============================================================================================
#!one program 

import pandas as pd
a = pd.Series([10,2,-3,23,5,0,12,14])
print("-------------------------------------")
print("Series - 1 ")
print(a)
print("-------------------------------------")
# #* Find Max Element by using seriesobj.max()
# maxv = a.max()
# print("Max Element : ",maxv)

#*or
# a.sort_values(inplace = True)
# print("Max ELement : ",a.values[-1])

#*or 
# a.sort_values(ascending=False,inplace= True)
# print("Max Element  ",a.values[0])

#*OR
# a.sort_values(inplace= True)
# print("Min Element : ",a.values[a.size-1])

#^===============================================================================================

#!nlargest
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-----------------------")
# print("Series Object ")
# print(a)
# print("-----------------------")
# maxv = a.nlargest(1) 
# # *print("Max Element : ",maxv)   #*Max Element :  3    23   #*index sobat dete
# print("Max Element : ",maxv.values[0])


# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-----------------------")
# print("Series object")
# print(a)
# print("-----------------------")
# maxv = a.nlargest(2)
# print("Max ELement : ",maxv.values)



# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-------------------")
# print("Series -1")
# print(a)
# print("-------------------")
# maxv = a.nlargest()   #* # By default It Gives 5 Largest Elements
# print("Max ELements : ",maxv.values)    




#*!one PRogram

import pandas as pd
a = pd.Series([10,2,-3,23,5,0,12,14])
print("-----------------------")
print("Series Object ")
print(a)
print("-----------------------")
# maxv = a.nlargest(1) 
# # print("Max Element : ",maxv)   #*Max Element :  3    23   #*index sobat dete
# print("Max Element : ",maxv.values[0])


# maxv = a.nlargest(2)
# print("Max ELement : ",maxv.values)


# maxv = a.nlargest()   #* give 5 max element default 
# print("Max ELements : ",maxv.values)    


#^===============================================================================================