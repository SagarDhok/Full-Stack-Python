
import pandas as pd,numpy as np
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Pandas\\DataFrame\\studentmarks.csv")
#& Add the New Column Total
df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]


#& Add and Cal percentage of Marks
df["percent"] = round(df["total"]/600*100,2)
print("*"*70)
print(df)
print("*"*70)
#?===============================================================================================



#& Get Name of the Student whose maths Marks is more than 90

# print(df["maths"]>=90)      #*boolean array dete pencil
# print(df.loc[df["maths"]>90,["name"]])


#& Get Name and maths marks of the Student whose maths Marks is more than 90
# print(df.loc[df["maths"]>=90,["name","maths"]])


#& Get Student whose maths Marks is are between 80 and 90
# print(df[(df["maths"]>=80) & (df["maths"]<=90)])

#& Get Name and maths marks of the Student whose maths Marks between 80 and 90
# x = df[(df["maths"]>=80) & (df["maths"]<=90)][["name","maths"]]
# print(x,type(x))

#*or 

# x= df.loc[(df["maths"]>=80) & (df["maths"]<=90)][["name","maths"]]
# print(x)

#or
# x= df.loc[(df["maths"]>=80) & (df["maths"]<=90)][["name","maths"]]
# print(x)


#& Get the students whose Total marks whose Total Marks ranges between 410 and 430
# print(df[(df["total"]>=410) & (df["total"]<=430)])

#& Get the Names and Total marks whose Total Marks ranges between 410 and 430
# print(df[(df["total"]>=410) & (df["total"]<=430)][["name","total"]])


# print("Number of people whose secured total marks between 410 and 430 : ",df[(df["total"]>=410) & (df["total"]<=430)].shape[0])
#?===============================================================================================
