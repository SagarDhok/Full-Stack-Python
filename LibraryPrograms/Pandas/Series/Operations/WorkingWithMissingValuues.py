
#*last
#^===============================================================================================
#& To Find the Nan Value, we have a Function Call seriesobj.isna()
# import numpy as np,pandas as pd
# a = pd.Series([100,200,np.NAN,400,None],index= ["a","b","c","d","e"])
# print("-----------------------------")
# print("Series-1")
# print(a)
# print("-----------------------------")
# print(a.isna())   #* Gives Boolean Array  
# print(a[a.isna()]) #* we can also view values also


#^===============================================================================================
#& finding total number of missing valuese 
# import pandas as pd ,numpy as np
# a = pd.Series([100,200,np.NAN,400,None],index = ["a","b","c","d","e"])
# print("---------------------------")
# print("Series -1 ")
# print(a)
# print("-----------------------------")
# print("Total Number of missing values : ",a.isna().sum()) #* Gives Number of Missing Values (NaN Values)
#^===============================================================================================
#& To Find the Nan Value, we have a Another Function seriesobj.isnull()
# import pandas as pd,numpy as np
# a = pd.Series([100,200,np.NAN,400,None],index = ["a","b","c","d","e"])
# print("---------------------------")
# print("Series - 1")
# print(a)
# print("---------------------------")
# print(a.isnull())  #* Gives Boolean Array 
# print("------------") 
# print(a[a.isnull()]) #* we can also view values also
#^===============================================================================================
#& finding total number of missing valuese 
# import pandas as pd,numpy as np
# a = pd.Series([100,200,np.NAN,400,None],index = ['a','b','c','d','e'])
# print("--------------------")
# print("Series - 1")
# print(a)
# print("-----------------")
# print("Number of Missing values : ",a.isnull().sum())
# print("Number of missing values : ",a.size-a.count())
#^===============================================================================================
# #*write in one

# import pandas as pd,numpy as np
# a = pd.Series([100,200,np.NAN,400,None],index = ['a','b','c','d','e'])
# print("--------------------")
# print("Series - 1")
# print(a)
# print("-----------------")
# # print(a.isna())   #* Gives Boolean Array  
# # print("Total Number of missing values : ",a.isna().sum()) #* Gives Number of Missing Values (NaN Values)


# #& To Find the Nan Value, we have a Another Function seriesobj.isnull()
# # print(a.isnull())  #* Gives Boolean Array 
# # print("Number of Missing values : ",a.isnull().sum())  #* Gives Number of Missing Values (NaN Values)


# #*or 

# # print("Number of missing values : ",a.size-a.count())