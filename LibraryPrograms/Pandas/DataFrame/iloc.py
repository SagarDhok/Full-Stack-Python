

#* indexing is not possible in dataframe without these funtions
#!loc[] and iloc[] are attribytes.



# import pandas as pd
# df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
# print("*"*80)
# print(df)
# print(type(df))
# print("*"*80)

#?===============================================================================================
#todo===============================================================================================
#!iloc[]
#todo===============================================================================================
#?===============================================================================================
#& get 13 Record by using iloc[]
# print(df.iloc[13])

#& get 10Record by using iloc[]
# print(df.iloc[10])
#?===============================================================================================
#&Get 3 Record and name
# print(df.iloc[3,[1]])

#& Get 3 Record name and maths and science
# print(df.iloc[3,[1,5,6]])

#?===============================================================================================
#& Get 3rd record to 6th  Record
# print(df.iloc[3:7])

#& Get the Records from 10 to Last
# print(df.loc[10::2])

#?===============================================================================================
#& Get 3rd record to 6th  Record and Need Name and Social
# print(df.iloc[3:7,[1,7]])

#& Get 3rd record to 6th  alternatively Record and Need Name and Social
# print(df.iloc[3:7:2,[1,7]])

#?===============================================================================================
#& Get all  Record and Need Name 
# print(df.iloc[::,[1]])

# print(df.iloc[::,[1]].size)
# print(df.iloc[::,[1]].count())
#?===============================================================================================
#& get the Random records from DataFrame
# print(df.iloc[[1,6,9]])

# print(df.iloc[[1,6,9],[1,6,7]])
#?===============================================================================================
#& get all the Records from dataFrame with Name, to Maths
# print(df.iloc[::,[1,2,3,4,5]])
#
#*or direct with slicing
#& get all the Records from dataFrame with Name, to Maths with Column Slicing
# print(df.iloc[::,1:6])   #* without bracets in for col slicing


#& get all the Records alternatively from dataFrame with Name, to Maths with Column Slicing
# print(df.iloc[::2,1:6])

#& get all the Records from dataFrame with Name, to Maths with Column Slicing column alternativaly
# print(df.iloc[::2,1:6:2])
#?===============================================================================================
