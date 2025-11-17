
# #?===============================================================================================
# import numpy as np, pandas as pd
# df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
# print("*"*70)
# df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
# df["percent"]=round((df["total"]/600)*100,2)
# print(df)
# print("-"*70)
# print("Number of Records=",df.shape[0])
# print("*"*70)


# #Give the Grade to Students with Following Conditions
# #Distinction Grade----->Percentage >=74
# #First Grade----------> 74>Percentage>=65
# #Second Grade--------->65>percentage>=60
# #Third Grade--------->60>percentage


# #Add Grade Column to data frame
# df["grade"] = None


# #Distinction Grade----->Percentage >=74
# df.loc[df["percent"]>=74,"grade"] = "Distinction".upper()

# #First Grade----------> 74>Percentage>=65
# df.loc[((df["percent"]>=65) & (df["percent"]<74)),"grade"]= "FIRST"

# #Second Grade--------->65>percentage>=60
# df.loc[((df["percent"]>=60)&(df["percent"]<65)),"grade"]="SECOND"

# #Third Grade--------->60>percentage
# df.loc[df["percent"]<60,"grade"] = "THIRD"

# print(df)



# #& Export DataFrame Object to the CSF File on the Name of StudentFinalResult.csv

# df.to_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\studentfinalresult.csv")
# print("DataFrame data exported verify")