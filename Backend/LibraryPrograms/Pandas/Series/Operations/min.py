

#!min
#*syntax : seriesobj.min()
#^===============================================================================================
#& Find Min Element by using seriesobj.min()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("----------------------")
# print("Series -1 ")
# print(a)
# print("----------------------")
# minv = a.min()
# print("Min Element : ",minv)
#^===============================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("------------------------")
# print("Series - 1 ")
# print(a)
# print("------------------------")
# a.sort_values(inplace=True)
# print("Min Element : ",a.values[0])

#^===============================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("------------------------")
# print("Series - 1 ")
# print(a)
# print("------------------------")
# a.sort_values(ascending=False,inplace=True)
# print("Min ELement : ",a.values[-1])
#^===============================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("--------------------")
# print("Series -1")
# print(a)
# print('----------------------------')
# a.sort_values(ascending= False,inplace= True)
# print("Min Element : ",a.values[a.size-1])


#!  ONE PROGRAM

# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("----------------------")
# print("Series -1 ")
# print(a)
# print("----------------------")
# minv = a.min()
# print("Min Element : ",minv)



# a.sort_values(inplace=True)
# print("Min Element : ",a.values[0])

# # *OR

# a.sort_values(ascending=False,inplace=True)
# print("Min ELement : ",a.values[-1])

# # *OR 
# a.sort_values(ascending= False,inplace= True)
# print("Min Element : ",a.values[a.size-1])
#^===============================================================================================

#!nsmallest 
#& Find Min Element by using seriesobj.nsmallest()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("----------------------")
# print('SERIES - 1')
# print(a)
# print("----------------------")
# minv = a.nsmallest(1)
# # #* print("Smallest Element : ",minv)   Smallest Element :  2   -3
# print("Smallest Element ",minv.values[0])


# import pandas as pd
# a= pd.Series([10,2,-3,23,5,0,12,14])
# print("--------------------------")
# print("series -1")
# print(a)
# print("---------------------")
# minv = a.nsmallest(2)
# print("Min ELement : ",minv.values)

# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("--------------------")
# print("Series - 1 ")
# print(a)
# print("----------------")
# minv = a.nsmallest()        #* By default It Gives 5 smallest Elements
# print("Min ELements : ",minv.values)



#! one Program 

# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("----------------------")
# print('SERIES - 1')
# print(a)
# print("----------------------")
# minv = a.nsmallest(1)
# #* print("Smallest Element : ",minv)   Smallest Element :  2   -3
# print("Smallest Element ",minv.values[0])


# minv = a.nsmallest(2)
# print("Min ELement : ",minv.values)


# minv = a.nsmallest()        #* By default It Gives 5 smallest Elements
# print("Min ELements : ",minv.values)

