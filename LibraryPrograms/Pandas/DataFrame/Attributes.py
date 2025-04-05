

#?================================================================================================
#! Attributes of DataFrame
import pandas as pd
d= {"Students":["Arvind","Aswin","Rossum","Travis"],
    "Marks": [85,92,78,83],
    "Sports ":["Cricket", "vollyball","Hockey","Shuttle"]
    }
df = pd.DataFrame(d)
print("----------------------------")
print(df)
print("----------------------------")

# import pandas as pd
# d= {"Students":["Arvind","Aswin","Rossum","Travis"],
#     "Marks": [85,92,78,83],
#     "Sports ":["Cricket", "vollyball","Hockey","Shuttle"]
#     }
# df = pd.DataFrame(d)
# print("----------------------------")
# print(df)
# print("----------------------------")

# import pandas as pd
# d = {"Students":["Arvind","Aswin","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#      "Sports":["Cricket", "vollyball","Hockey","Shuttle"]
#      }
# df = pd.DataFrame(d,index=["record1","record2","record3","Record4"])
# print(df)


#?================================================================================================
#& Attribute Name :  dataframeobj.index
# print(df.index)

# for indx in df.index:
#      print(indx)
#?================================================================================================
#& Attribute Name :  dataframeobj.columns
# # print(df.columns)
# for col in df.columns:
#      print(col)
#?================================================================================================
#& Attribute Name :  dataframeobj.dtypes
# # print(df.dtypes)
# # 
# for dt in df.dtypes:
#      print(dt)
#?================================================================================================
#& Attribute Name :  dataframeobj.axes
# print(df.axes)

# for ax in df.axes:
#      print(ax)

# print(df.axes[0])
# for ax in df.axes[0]:
#      print(ax)

# print(df.axes[1])
# for ax in df.axes[1]:
#      print(ax)
#?================================================================================================
#& Attribute Name :  dataframeobj.size
# print(df.size)
#?================================================================================================
#& Attribute Name :  dataframeobj.shape
# print(df.shape)
# print("Number of rows : ",df.shape[0])
# print("Number of cols : ",df.shape[1])
#?================================================================================================
#& Attribute Name :  dataframeobj.ndim
# print(df.ndim)
#?================================================================================================
#& Attribute Name :  dataframeobj.empty
# df1 = pd.DataFrame()
# print("-----------")
# print(df1,type(df1))
# print("-----------")
# print("Is Df is Empty : ",df.empty)
# print("Is Df1 is Empty : ",df1.empty)
#?================================================================================================
#& Attribute Name :  dataframeobj.values
# print(df.values)   #*gives in ndarray
# print(type(df.values))   #*gives in ndarray

# for record in df.values:
#      print(record,type(record))

# for record in df.values:
#      for val in record:
#           print(val,end="\t ")
#      print()
#?================================================================================================
#& Attribute Name :  dataframeobj.T
# print(df.T)

#?================================================================================================

# dict = {"Sales": {'Name': 'Rossum', 'Age': 67, 'Gender': 'Male'},
#         "Marketing": {'Name': 'Rossy',  'Age': 65, 'Gender': 'Female'}}
 
# # Creating a data frame object
# data_frame = pd.DataFrame(dict)
 
# # printing this data frame on output screen
# print(data_frame)

#?================================================================================================