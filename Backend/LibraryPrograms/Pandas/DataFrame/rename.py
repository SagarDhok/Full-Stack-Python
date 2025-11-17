
#?===============================================================================================

import pandas as pd,numpy as np
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6],"C": [7,8,9]})
print("----------------------------------")
print(df)
print("----------------------------------")

#?===============================================================================================
#* Change OR Rename the Column Names
# print(df.rename(columns={"A":"a","B":"b","C":"c"}))

#* for stoting in dataframe iteself
# df = df.rename(columns={"A":"a","B":"b","C":"c"})
# print(df)
#?===============================================================================================
#* Change OR Rename the Column Names
# print(df.rename(columns={"A":"Col-1","B":"Col-2","C":"Col-3"}))
#?===============================================================================================
#* Changing OR Renaming Indices (Row Indexes)
# print(df.rename(index={0:"index-1",1:"index-2",2:"index-3"}))

#?===============================================================================================

#* Change OR Rename the Column Names and Indices (Row Indexes)

# print(df.rename(index = {0:"row-1",1:"row-2",2:"row-3"},
#      columns={"A":"col-1","B":"col-2","C":"col-3"})
      )

#! access 1 
# print(df.values[0][0])