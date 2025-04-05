



import numpy as np, pandas as pd
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
print("*"*70)
df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
df["percent"]=round((df["total"]/600)*100,2)
print(df)
print("-"*70)
print("Number of Records=",df.shape[0])
print("*"*70)
#?===============================================================================================
#!WITH COLUMN NAMES
#& remove the Percent Column from DataFrame
# print(df.drop(columns="percent"))
# print(df)

#!for storing in dataframe itself
# df.drop(columns = "percent",inplace=True)
# print(df)

#& remove Multiple Columns from datafarme object
# df.drop(columns=["name","maths"])
# print(df)

#! for storinf in dataframe itself
# df.drop(columns=["name","maths"],inplace=True)
# print(df)

#?===============================================================================================
#!COLUMN NUMBER

#& Remove the column 'percent' based on Column Number
# print(df.drop(columns=df.columns[9]))
# print(df)


#!for storing in dataframe itself
# df.drop(columns=df.columns[9],inplace=True)
# print(df)

# df.drop(columns=df.columns[[1,5,9]],inplace=True)
# print(df)

#?===============================================================================================
#!REMOVING ROW
#& remove the Row 10 from dataframe object

# df.drop(labels = 10,axis=0,inplace=True)
# print(df)



#& remove the Row 2 5 and 7 from dataframe object
# df.drop(labels=[2,5,7],axis= 0 , inplace=True)
# print(df)
# print("Number of Records=",df.shape[0])


#& remove the Rows from 12 to 16from dataframe object
# df.drop(labels=[12,13,14,15,16],axis=0,inplace= True)
# print(df)