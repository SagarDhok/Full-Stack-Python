
#! merged funtion is depricated on the name of concate


# import numpy as np,pandas as pd
# # List of Tuples
# data1 = [('Jack', 34, 'Sydney', 5),
#          ('Riti', 31, 'Delhi' , 7),
#          ('Aadi', 46, 'New York', 11)]

# # List of Tuples
# data2 = [('Mohit', 34, 'Tokyo', 11) ,
#         ('Veena', 31, 'London' , 10) ,
#         ('Shaun', 36, 'Las Vegas', 12)]

# # List of Tuples
# data3= [('Mark', 47, 'Mumbai',   13) ,
#         ('Jose', 43, 'Yokohama', 14) ,
#         ('Ramu', 49, 'Paris',    15)]

# # Convert data1 , data2 and data3 into DataFrame.
# df1= pd.DataFrame(data1,index=["a","b","c"],columns=["Name","Age","City","Exp"])
# df2 = pd.DataFrame(data2,index= ["d","e","f"],columns=["Name","Age","City","Exp"])
# df3 = pd.DataFrame(data3,index= ["g","h","i"],columns=["Name","Age","City","Exp"])

# print("------------------------------------------------")
# print("Dataframe - 1 ")
# print(df1)
# print("------------------------------------------------")
# print("Dataframe - 2 ")
# print(df2)
# print("------------------------------------------------")
# print("Dataframe - 3")
# print(df3)
# print("------------------------------------------------")


#& Concatenating DataFrames
# fdf= pd.concat([df1,df2,df3])
# #* or
# xdfd = pd.concat([df1,df2,df3],axis = 0) 

# print(fdf)
# print(xdfd)

#& Concatenating DataFrames
yfdf = pd.concat([df1,df2,df3],axis = 1)
print(yfdf)