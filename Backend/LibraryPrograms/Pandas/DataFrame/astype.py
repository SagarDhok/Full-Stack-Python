

#! how to typecast muliple columns - imp in the form of dict
#?================================================================================================
#!Create a dataframe from dicttionary
# import pandas as pd,numpy as np
# technologies = {"Fee":["2000","25000","26000"],"Discount":["1000","2300","1500"]}
# df = pd.DataFrame(technologies)
# print(df)
# print(df.dtypes)
#?================================================================================================
#*Cast all columns to int
# df = df.astype(np.int64)
# print(df)
# print(df.dtypes)
#?================================================================================================
#* Cast all columns to string
# df = df.astype("string")
# print(df.dtypes)
#?================================================================================================
#* Cast all columns to string
# df = df.astype('str')
# print(df.dtypes)
#?================================================================================================
#* Cast all columns to float
# df= df.astype("float")
# print(df.dtypes)
#?================================================================================================
# df["Fee"] = df["Fee"].astype("int")
# print(df.dtypes)
#?================================================================================================
import numpy as np,pandas as pd
technologies = {"Courses" : ["Spark","PySpark","Hadoop"],
                "Fee": ["20000","25000","26000"],
                "Duration": ["30day","40day","35day"],
                "Discount": ["1000","2300","1500"]
                }

df = pd.DataFrame(technologies)
print("-----------------------------------")
print(df)
print("-----------------------------------")
print(df.dtypes)
#?================================================================================================
#* Apply cast type for multiple columns 
#!multiple column sathi dictionary use karn lagte
df2= df.astype({"Courses":"string","Fee":"int","Discount":"float"})
print("-------------------------------------")
print(df2)
print("-------------------------------------")
print(df2.dtypes)


#?================================================================================================
#*Raise error when unable to cast
# df["Courses"] = df["Courses"].astype("int") #* ValueError   "STRING alphabets int madhe convert hot nahit"
#?================================================================================================
#* Ignore error when unable to cast    
# !Error ignore karte an update nahi karat tech tevte
# df.Courses = df.Courses.astype("int",errors="ignore")
# print("---------------------------------")
# print(df)
# print("---------------------------------")
# print(df.dtypes)
# print("----------------------------------")
#?================================================================================================
#* Ignore error when unable to cast
# df2.Courses = df2.Courses.astype("int",errors = "ignore")
# print("----------------------------------")
# print(df2)
# print("----------------------------------")
# print(df2.dtypes)