
#! drop
#*syntax = eriesobj.drop(['Label']) OR seriesobj.drop([index])
#^===============================================================================================
#& Droping the Series of Values
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index= ["a","b","c","d","e"])
# print("--------------------------------------------")
# print("Original Series ")
# print(a)
# print("-------------------------------------------")
# print("Series of  values after drop ")
# print(a.drop(["c"]))
# print("-------------------------------------------")
# print("Original Series")
# print(a)
#^===============================================================================================

#* to store in a 
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index = ["a","b","c","d","e"])
# print("---------------------------------")
# print("Original Series ")
# print(a)
# print("---------------------------------")
# #* Drop the C label Values
# print("Series of values after drop")
# a = a.drop(["c"])
# print(a)


#^===============================================================================================
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index= ["a","b","c","d","e"])
# print("-------------------------------")
# print("Original Series ")
# print(a)
# print("-------------------------------")
# print("Series of values after drop")
# a.drop(["a","b","d"],inplace=True)    #*multiple value also possible
# print(a)

#^===============================================================================================
# import pandas as pd
# a = pd.Series([100,200,300,400,500])
# print("------------------------------")
# print("Original Serie ")
# print(a)
# print("------------------------------")
# print("Serie of values after drop")
# a = a.drop([3])
# print(a)

# print("---------------")
 #^===============================================================================================
# import pandas as pd
# a = pd.Series([100,200,300,400])
# print("--------------------------")
# print("Original Series ")
# print(a)
# print("--------------------------")
# print("Series of value after drop")
# a.drop([1,3],inplace=True)
# print(a)
#^===============================================================================================
