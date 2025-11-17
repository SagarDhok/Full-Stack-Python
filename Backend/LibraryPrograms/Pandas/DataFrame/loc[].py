
#* indexing is not possible in dataframe without these funtions
#!loc[] and iloc[] are attribytes.



import pandas as pd
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
print("*"*80)
print(df)
print(type(df))
print("*"*80)
#?===============================================================================================
#todo===============================================================================================
#!loc[]
#todo===============================================================================================
#?===============================================================================================
#& get 7th Record by using loc[]
# print(df.loc[7])

#& get 10th record
# print(df.loc[10])

#?===============================================================================================
#& Get 14th Record Name
# print(df.loc[14,["name"]])


#& Get 10th Record Name and Maths
# print(df.loc[10,["name","maths"]])
#*or 
# print(df.loc[14][["name","maths"]])

#!xxxx
#& Get 10th Record Name Maths, social Marks
# print(df.loc[10,["name","maths","social"]])

#& Get 10th Record htno Name Maths, social Marks
# print(df.loc[10,["htno","name","maths","social"]])
#?===============================================================================================
#& Applyinbg the slicing Operation by using loc[]
#& Get the Records from 3 to 6
# print(df.loc[3:6])

#& Get the Records from 10 to Last
# print(df.loc[10::2])

#?===============================================================================================
#& Get the Records from 10 to Last with Name and Maths Marks
# print(df.loc[10:][["name","maths"]])

#*or 
#& Get the Records from 10 to Last with Name and Maths Marks
# print(df.loc[10:,["name","maths"]])

#?===============================================================================================
#& By using loc[] , Display all Names of Rows
# print(df.loc[::1,["name"]])

# print(df.loc[::1,["name"]].count())
# print(df.loc[::1,["name"]].size)

#?===============================================================================================
#& get the Random records from DataFrame
# print(df.loc[[1,6,9]])

# print(df.loc[[1,6,9],["name","science","maths"]])
# #or 
# print(df.loc[[1,6,9]][["name","science","maths"]])

#?===============================================================================================
#& get all the Records from dataFrame with Name, to Maths
# print(df.loc[::,['name','telugu','hindi','english','maths']])

#*or direct with slicing
#& get all the Records from dataFrame with Name, to Maths with Column Slicing
# print(df.loc[::,'name':'maths'])  #* without bracets in for col slicing


#& get all the Records alternatively from dataFrame with Name, to Maths with Column Slicing
# print(df.loc[::2,"name":"maths"])


#& get all the Records from dataFrame with Name, to Maths with Column Slicing column alternativaly

# print(df.loc[::2,"name":"maths":2])
#?===============================================================================================





















#Get 3 8 14 Records