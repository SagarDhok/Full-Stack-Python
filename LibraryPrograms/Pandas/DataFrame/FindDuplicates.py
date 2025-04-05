  
#! NP.NAN - REPRESENTATION OF MISSING VALUE


import numpy as np, pandas as pd
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
print("*"*70)
print(df)
print("-"*70)
print("Number of records : ",df.shape[0])
print("*"*70)
#?===============================================================================================
#& Find Duplicate Entry
print(df.duplicated())   #* gives boolean array

# print(df[df.duplicated()])
#?===============================================================================================
# #& remove the Duplicated Entry and place data without duplicates in same DataFarme
# df.drop_duplicates(inplace=True)  #* or df = df.drop_duplicates()
# print(df)
# print("Number of records : ",df.shape[0])

#?===============================================================================================
#& Adding row
#! dataframe madhe lastla ch data add hote
# df.loc[len(df)+1] = [122,"hanuman",55,66,77,88,99,44]
# print(df)

# print("Number of records : ",df.shape[0])
#?===============================================================================================
#& Sorting values 
# print(df.sort_values(["maths"]))
# print(df)

# print(df.sort_values(["maths"],ascending=False))

#!dataframe madhi store karaych asel tr
# df = df.sort_values(["maths"])
#* or
# df.sort_values(["maths"],inplace=True)
# print(df)

# df.sort_values(["maths"],ascending=False,inplace=True)
# print(df)

# df.sort_values(["name"],inplace=True)
# print(df)

