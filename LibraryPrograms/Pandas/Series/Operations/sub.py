
#! Subtracting the Series of Values
#*syntax = varname Seriesobj.2 = Seriesobj1.sub(Seriesobj2)
#^===============================================================================================
#& Subtracting the Series of Values
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b = pd.Series([10,20,30,40,50,],index = ["a","b","c","d","e"])
# print("------------------------------------")
# print("Sereis - 1")
# print(a)
# print("------------------------------------")
# print("Series - 2")
# print(b)
# print("------------------------------------")
# # * subtract the series of Values----we use   setobj3=serobj1.sub(serobj2)
# print("Serie - 3 ")
# c  = a.sub(b)
# print(c)
# print("------------------------")
# d  = b.sub(a)
# print(d)

#^===============================================================================================
#& Subtracting the Series of Values when Series object contains Different Label Names
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index= ["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50],index = ["a","b","f","c","e"])
# print("-----------------------------------")
# print("Series -1 ")
# print(a)
# print("-----------------------------------")
# print("Series - 2  ")
# print(b)
# print("-----------------------------------")
# #* add the series of Values----we use   setobj3=serobj1.sub(serobj2,fill_value=0)
# print("Sereis - 3 ")
# c = a.sub(b)
# print(c)
#^===============================================================================================
#& Subtracting the Series of Values when Series object contains Different Label Names
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index = ["a","b","h","d","e"])
# b= pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# print("----------------------------------------")
# print("Series - 1")
# print(a)
# print("----------------------------------------")
# print("Series - 2")
# print(b)
# print("----------------------------------------")
# #* add the series of Values----we use   setobj3=serobj1.sub(serobj2,fill_value=0)
# c = a.sub(b,fill_value= 0)
# print(c)


\