

#! new column pahijet asel tr transoform cha use hoto
#! imp agg transformation filter
#?===============================================================================================
# import pandas as pd,numpy as np
# df= pd.DataFrame({"team": ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
#                   "points":[30, 22, 19, 14, 14, 11, 20, 28]
#      })

# print("------------------------")
# print(df)
# print("------------------------")
#?===============================================================================================
# tgb = df.groupby("team")
# for groupname,groupdata in tgb:
#      print("Group Name : ",groupname)
#      print(groupdata)
#      print()

#* Calculate the Mean Points of each Time
# df["mean-points"]= df.groupby("team")["points"].transform("mean")

#* Calculate the sum Points of each Time
# df["sum-points"] = df.groupby("team")["points"].transform("sum")


#* create new column called percent_of_points
# df["percent_of_points"] = df.groupby("team")["points"].transform(lambda x : x/x.sum())
# print(df)

#!xxx
#*create new column called percent_of_points
# df["percent_of_points"] = df.groupby("team")["points"].transform(lambda x: (x/x.sum())*100 )
# print(df)

#?===============================================================================================
# print(df.groupby('team')["points"].agg(["sum"]))

# print(df.groupby("team")["points"].agg(["sum","mean"]))
#?===============================================================================================

# import pandas as pd,numpy as np
# df = pd.DataFrame({"Animal":['Falcon', 'Falcon', 'Parrot', 'Parrot'],
#                     "Max Speed": [380., 370., 24., 26],
#                     "Type":["Bird","Bird","Bird","Bird"]
#  })

# print("----------------------------")
# print(df)
# print("----------------------------")
# #! theory lihaychi
# print(df.groupby(["Animal","Type"]).mean())
#?===============================================================================================\
# import pandas as pd

# df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 
#                    'Max Speed': [380., 370., 24., 26.]})

# print("---------------------------------")
# print(df)
# print("---------------------------------")

# print(df.groupby(["Animal"]).agg(["mean","max","min"]))
#?===============================================================================================
#& Filtering Groups
# print(df.groupby('Animal').filter(lambda x : x["Max Speed"].mean()>100))

# print(df.groupby("Animal").filter(lambda x : x["Max Speed"].mean()<100))