
#?===============================================================================================
import pandas as pd,numpy as np
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
print("*"*80)
print(df)
print(type(df))
print("*"*80)


# print(df.shape)
#?===============================================================================================
#& Get 5 Records from DataFrame
# recs = df.head()   #* gives default 5 top rows
# print(recs)
# print( type(recs))


#& Get 6 Records from DataFrame
# recs = df.head(6)
# print(recs)
# print( type(recs))
#?===============================================================================================
#& get Last 5  Records by using tail()
# recs = df.tail()   #* gives default 5 bottom rows
# print(recs)
# print(type(recs))

#& get Last 2  Records by using tail()
# recs = df.tail(2)
# print(recs)
# print(type(recs))

#!  xxxx
#& get Last 6  Records by using tail()  
# recs= df.tail(6)
# print(recs)
# print(type(recs))
#?===============================================================================================
#& Obtain the Stastistical Information abount studentmarks1.csv file
#& which is available in the form of DataFrame
# print(df.describe())
# print(type(df.describe()))
# print("-------------------------")
# x = df.describe(include="all")
# print(x)


# print(df["name"].describe())
# print(df["telugu"].describe())
#?===============================================================================================
#& Get Record by Record by using iterrows()
# print(df.iterrows())   #* <generator object DataFrame.iterrows at 0x00000159653DBBC0>


# for rec in df.iterrows():
#      print(rec)
#?===============================================================================================
#& Get the Records from 4th to 9th from DataFrame Object
# print(df[4:10])

#& Get the Records all Even  Indexed Records from DataFrame Object
# print(df[::2])

#& Get the Records all Odd  Indexed Records from DataFrame Object
# print(df[1::2])


# print(df[4:10:2])

# print(df[4:10:-1])   #!space  #begin>end in backward direction

# print(df[10:4:-1])


# print(df[::-1])
#?===============================================================================================
#& Get the Name of all students
# print(df["name"])


#&Get Name and Their Maths Marks
# print(df[["name","maths"]])     #*inner list madhe pass karna lagate dataframe madhe


#& Get Name and Their Maths Marks from 4th to 8th
# print(df[["name","maths"]][4:9])
# ! or
# print(df[4:9][["name","maths"]])


#!xxxxxx
#& Get Name and Their Maths Marks from 4th to 8th
# print(df[4:9:2][["name","maths"]])
#?===============================================================================================