

import pandas as pd,numpy as np
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
df["percent"] = round(df["total"]/600*100)
print("*"*80)
print(df)
print("*"*80)
#?===============================================================================================
#& Give the Grade to Students with Following Conditions
#& Distinction Grade----->Percentage >=74
#& First Grade----------> 74>Percentage>=65
#& Second Grade--------->65>percentage>=60
#& Third Grade--------->60>percentage


#& Add Grade Column to data frame
df["grade"] = None
# print(df)

# print(df.loc[df["percent"]>=74])

#& Distinction Grade----->Percentage >=74
# df.loc[df["percent"]>=74,["grade"]]= "DISTINCTION"
# print(df)


#& First Grade----------> 74>Percentage>=65
# print(df.loc[(df["percent"]<74) & (df["percent"]>=65)])

# df.loc[(df["percent"]<74) & (df["percent"]>=65) ,["grade"] ]   = "FIRST"
# df[(df["percent"]<74) & (df["percent"]>=65) ,["grade"] ]   = "FIRST"   #! without loc and iloc updation is not possible
# print(df) 



#& Second Grade--------->65>percentage>=60
# print(df.loc[((df["percent"]>=60) & (df["percent"]<65))])

# df.loc[((df['percent']>=60) & (df['percent']<65)),["grade"]] = "SECOND"
# print(df)


#& Third Grade--------->60>percentage
# print(df.loc[df["percent"]<60])

# df.loc[df["percent"]<60,["grade"]] = "THIRD"
# print(df)


#& Count Number Students who got Distinction

# print("Number of student who passed in DISTINCTION : ",df[df["grade"]=="Distinction".upper()].shape[0])

#& Find the Name of the student who got Highest Percentage
# print(df[df["percent"].max()==df["percent"]][["name"]])


#& Find the Name and also marks of the student who got Highest Percentage
# print(df[df["percent"].max()==df["percent"]][["name","percent","total"]])






#?===============================================================================================

# import pandas as pd,numpy as np
# df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
# df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
# df["percent"] = round(df["total"]/600*100)
# print("*"*80)
# print(df)
# print("*"*80)


# df["grade"]=None

# print(df[df["percent"]>=74])

# df.iloc[(df["percent"]>=74),[10]] = "DISTINCTION"
# print(df)

# print(df.iloc[1:2,[1]])
