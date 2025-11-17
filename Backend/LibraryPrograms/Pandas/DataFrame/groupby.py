

#?================================================================================================
import numpy as np,pandas as pd
df = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\peoples.csv")
print("----------------------------------")
print(df)
print("----------------------------------")
#?================================================================================================
#* Get State-wise Data from DataFrame--apply groupby()
sg = df.groupby("STATE")
# print(sg)   #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000201449B63F0>
# print(type(sg)) #<class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# for groupname,groupdata in sg: #*or for groupname , groupdata in df.groupby("STATE"):
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()


# print("Number of groups :  ",sg.ngroups)
# print("Number of groups : ",len(sg))


#* Find Number of People in each group
# print(sg.count())


# print(sg.size())


#* Get the First Record in Each Group---first()
# print(sg.first())

#* Get the last Record in Each Group---last()
# print(sg.last())

#* Get the 3rd Record in Each Group---nth(3)
# print(sg.nth(3))


# print(sg.get_group("AP"))
# apg  = sg.get_group("AP")
# print(apg)
# print(type(apg))   #<class 'pandas.core.frame.DataFrame'>

# apsbg = sg.get_group("AP").groupby("DSG")
# print(apsbg)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000024267C77E90>
# print(type(apsbg))

# for groupname,groupdata in apsbg:  
#!or
# for groupname,groupdata in df.groupby("STATE").get_group("AP").groupby("DSG"):
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()



# print(sg.get_group("BANG"))

# print(sg.get_group("TS"))

# for groupname,groupdata in df.groupby("STATE").get_group("TS").groupby("DSG"):
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()

#?================================================================================================
#!xxx
#* Get State-wise Data from DataFrame--apply groupby()
#* sg=df.groupby("STATE")

# for groupname , groupdata in df.groupby("STATE"):
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()
#?================================================================================================
# for groupname,groupdata in df.groupby("DSG"):
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()