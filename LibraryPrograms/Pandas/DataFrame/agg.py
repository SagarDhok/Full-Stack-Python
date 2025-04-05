
#?===============================================================================================
import numpy as np,pandas as pd
df= pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\population.csv")
print("---------------------------------")
print(df)
print("---------------------------------")
#?===============================================================================================
# ppgb = df.groupby("City")
# print("Type of ppgb",type(ppgb)) #<class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# for groupname,groupdata in ppgb:
#*or 
# for groupname,groupdata in df.groupby("City"):
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()

# print(df.groupby("City").size())

# print(df.groupby("City").ngroups)


# print(df.groupby("City").get_group("Delhi"))

# print(len(df.groupby("City").get_group("Delhi")))

# values = df.groupby("City").agg({"Age":"mean","Experience":"sum"})
# print(values)

# values = df.groupby("City").agg({"Age":"mean","Experience": "mean"})
# print(values)

# values = df.groupby("City")["Age"].agg(["size","sum","mean"])
# print(values)
#?===============================================================================================