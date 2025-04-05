
#! Adding the Series of Values
#*syntax = Seriesobj.2 = Seriesobj1.add(Seriesobj2)
#^===============================================================================================
#&wtite
# import pandas as pd ,numpy as np
# a = pd.Series([100,200,300,400,500],index = ["a","b","c","d","e"])
# b = pd.Series([10,20,30,40,50],index = ['a','b','c',"d","e"])
# print("-----------------------------------")
# print("Series - 1 ")
# print(a)
# print("-----------------------------------")
# print("Series - 2 ")
# print(b)
# print("-----------------------------------")
# # * add the series of Values----we use   setobj3=serobj1.add(serobj2)
# c = a.add(b)
# print("Series - 3")
# print(c)

#^===============================================================================================
#!
#*e - nan 
# import pandas as pd ,numpy as np
# a = pd.Series([100,200,300,400,500],index = ["a","b","c","d","e"])
# b = pd.Series([10,20,30,40],index = ['a','b','c',"d"])
# print("-----------------------------------")
# print("Series - 1 ")
# print(a)
# print("-----------------------------------")
# print("Series - 2 ")
# print(b)
# print("-----------------------------------")
# c = a.add(b)
# print("Series - 3")
# print(c)
#^===============================================================================================

# import pandas as pd
# a = pd.Series([100,200,300,400,500],index = ["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50]     ,index = ["a","b","f","c","e"])
# print('--------------------------------------')
# print("Series - 1")
# print(a)
# print('--------------------------------------')
# print("Series-2")
# print(b)
# print("--------------------------------------")
# #& add the series of Values----we use   setobj3=serobj1.add(serobj2)
# c= a.add(b)
# print("Series-3")
# print(c)

#& Adding the Series of Values when Series object contains Different Label Names
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index = ["a","b","h","d","e"])
# b= pd.Series([10,20,30,40,50]      ,index = ['a',"b","f","c","e"])
# print("--------------------------------------")
# print("Series - 1 ")
# print(a)
# print("--------------------------------------")
# print("Serie - 2")
# print(b)
# print("--------------------------------------")
# #* add the series of Values----we use   setobj3=serobj1.add(serobj2,fill_value=0) #kontihi fill value ghevu shakto
# c= a.add(b,fill_value=0)
# print("Series - 3")
# print(c)
#^===============================================================================================
#& Adding the Series of Values when Series object contains Different Label Names
# import pandas as pd
# a = pd.Series([100,200,300],index = ["a","b","c"])
# b = pd.Series([10,20,30],index = ["x","y","z"])
# print("---------------------------------------")
# print("Series -1")
# print(a)
# print("---------------------------------------")
# print("Series - 2")
# print(b)
# print("---------------------------------------")
# c= a.add(b)
# print('Series - 3')
# print(c)

#^===============================================================================================
#& Adding the Series of Values when Series object contains Different Label Names
#*wtite
# import pandas as pd
# a = pd.Series([100,200,300],index= ["a","b","c"])
# b= pd.Series([10,20,30],index= ["x","y","z"])
# print("-------------------------------")
# print("Series - 1")
# print(a)
# print("-------------------------------")
# print("Series - 2")
# print(b)
# print("-------------------------------")
# print("Series - 3")
# c = a.add(b,fill_value=0)
# print(c)
#^===============================================================================================
# import pandas as pd
# a = pd.Series([100,200,300],index = ['a','b','c'])
# b = pd.Series([10,20,30],index = ["x","y","z"])
# print("-------------------------------")
# print("Series - 1 ")
# print(a)
# print("-------------------------------")
# print("Series-2 ")
# print(b)
# print("-------------------------------")
# print("Sereis - 3")
# c = a.add(b,fill_value=10)
# print(c)
#^===============================================================================================