
#! HOW TO DEAL WITH MISSING VALUES

# import pandas as pd,numpy as np
# d = {"first score" : [100,90,np.nan,95],
#      "Second Score" : [30,45,56,np.nan],
#      "Third Score" : [np.nan,40,80,90]
# }

# #* convert dict data into dataframe object
# df = pd.DataFrame(d)
# print("------------------------")
# print(df)
# print("------------------------")

#?================================================================================================
#& To find Missing Values we use  isna(), isnull()
# print(df.isna())
# print(df.isnull())


#*or 

# print(df.isna().sum())   #* series sarkh dete
# print(df.isnull().sum())
#?================================================================================================
# print(df["first score"].isna())

# print(df["first score"].isna().sum())
#?================================================================================================
#!rowwise
# print(df.loc[1])
# print(df.iloc[1])


# print(df.loc[1].isna())
# print(df.iloc[1].isna())
# print(df.loc[1].isnull())
# print(df.iloc[1].isnull())

# print(df.loc[1].isna().sum())
# print(df.iloc[1].isna().sum())
# print(df.loc[1].isnull().sum())
# print(df.iloc[1].isnull().sum())
#?================================================================================================
#& Find Non-Missing Values by using notna() and notnull()

# print(df.notna())
# print(df.notnull())

# print(df.notna().sum())  #*series sarkh dete
# print(df.notnull().sum())
#?================================================================================================
#!rowwise

# print(df.loc[0].notna())
# print(df.loc[0].notna().sum())

# print(df.loc[1].notnull())
# print(df.loc[1].notnull().sum())
#?================================================================================================

#& Fill 0 value for NaN in entire DataFrame Object
# print(df.fillna(0))

#*for saving in dataframe itself
# df = df.fillna(0)
# print(df)
#?================================================================================================
# import numpy as np, pandas as pd
# d= {"first score " : [100,90,np.nan,95],
#     "second score" : [30,45,56,np.nan],
#     "third score"  :[np.nan,40,80,90]
# }

# #* Convert Dict Data into DataFrame
# df = pd.DataFrame(d)
# print("----------------------")
# print(df)
# print("----------------------")
#?================================================================================================
#& Fill 0 value for NaN in entire DataFrame Object
# df.replace(to_replace=np.nan,value=0,inplace=True)
# print(df)

# df.replace(to_replace=0.0,value=11.11,inplace=True)   #*kontayhi value replace karnaysathi use hoto
# print(df)

#?================================================================================================
# import numpy as np, pandas as pd
# d= {"first score" : [100,90,np.nan,95],
#     "second score" : [30,45,56,np.nan],
#     "third score"  :[np.nan,40,80,90]
# }

# #* Convert Dict Data into DataFrame
# df = pd.DataFrame(d)
# print("----------------------")
# print(df)
# print("----------------------")
#?================================================================================================
#& replace Nan Values of 'First Score'
#!xxxx
# print(df["first score"].fillna(0.0))
# print(df)


# df["first score"].fillna(0.0,inplace=True)   #* warning yete    #inplace = true is depricated in pandas 3.0
# print(df)
#! so use
# df["first score"] = df["first score"].fillna(0.0)
# print(df)


#* replace Nan Values of 'Second Score'
# df["second score"].replace(to_replace=np.nan,value=0.1,inplace=True)   #* warning dete  #inplace = true is depricated in pandas 3.0
# print(df)

#! so use
# df["second score"]=df["second score"].replace(to_replace=np.nan,value=0.1)
# print(df)
#?================================================================================================
# import numpy as np, pandas as pd
# d= {"first score" : [100,90,np.nan,95],
#     "second score" : [30,45,56,np.nan],
#     "third score"  :[np.nan,40,80,90]
# }

# #* Convert Dict Data into DataFrame
# df = pd.DataFrame(d)
# print("----------------------")
# print(df)
# print("----------------------")

#*replace Nan Values of Second Score and Third Score

# print(df[["first score","second score"]].fillna(11.11) )
# print(df)

#* for storing in dataframe itself
# df[["first score","second score"]].fillna(11.11,inplace=True)     #* warning dete  #inplace = true is depricated in pandas 3.0
# print(df)

#! so we use
# df[["first score","second score"]] = df[["first score","second score"]].fillna(11.11)
# print(df)


#?================================================================================================
# import numpy as np, pandas as pd
# d={'First Score':[100,90,np.nan,95],
#    "Second Score":[30,45,56,np.nan],
#    "Third Score":[np.nan,40,80,90]}
# #Convert Dict Data into DataFrame
# df=pd.DataFrame(d)
# print("------------------------------------------------")
# print(df)
# print("------------------------------------------------")
#?================================================================================================
#! Filling Row based Missing Values
# df.loc[0] = df.loc[0].fillna(0)
# print(df)


# print(df.loc[[2,3]])

# df.loc[[2,3]].fillna(0.0,inplace=True)   #!updata nahi hot
# print(df)

#! as karan lagete
# df.loc[[2,3]] = df.loc[[2,3]].fillna(11.11)
# print(df)


# df.loc[2:3] = df.loc[2: 3].fillna(11.11)   #!2:3 puran ghete
# print(df)
#?================================================================================================
# import numpy as np, pandas as pd
# d={'First Score':[100,90,np.nan,95],
#    "Second Score":[30,45,56,np.nan],
#    "Third Score":[np.nan,40,80,90]}
# #Convert Dict Data into DataFrame
# df=pd.DataFrame(d)
# print("------------------------------------------------")
# print(df)
# print("------------------------------------------------")
#?================================================================================================
# df.iloc[0:3] = df.iloc[0:3].replace(to_replace=np.nan,value=11.11)
# print(df)

#?================================================================================================
# import numpy as np,pandas  as pd
# d={'First Score':[100,90,np.nan,95],
#    "Second Score":[30,45,56,np.nan],
#    "Third Score":[np.nan,40,80,90]}
# #Convert Dict Data into DataFrame
# df=pd.DataFrame(d)
# print("------------------------------------------------")
# print(df)
# print("------------------------------------------------")
#?================================================================================================
# df.iloc[0:4] = df.iloc[0:4].replace(to_replace=np.nan,value=11.11)
# print(df)
#?================================================================================================
#! Consider the Following Problem
# import numpy as np, pandas as pd
# d={"Courses":["SPARK","JAVA","SCALA","PYTHON"],
#               "Fees":[20000,np.nan,26000,28000],
#                "Duration":["30days","40days",pd.NA,"40days"],
#                "Discount":[1000,np.nan,2500,None]}
# df=pd.DataFrame(d)
# print("--------------------------------------------------------")
# print(df)
# print("--------------------------------------------------------")
#?================================================================================================
#& Provide OR Give Discount Rs:500 for Python Course
# df.loc[3] = df.loc[3].fillna(500)
# print(df)

# print("----")
# df["Duration"] = df["Duration"].replace(to_replace=pd.NA,value=50)
# print(df)
#?================================================================================================
#! Consider the Following Problem
# import numpy as np, pandas as pd
# d={"Courses":["SPARK","JAVA","SCALA","PYTHON"],
#               "Fees":[20000,np.nan,26000,28000],
#                "Duration":["30days","40days",pd.NA,"40days"],
#                "Discount":[1000,np.nan,2500,None]}
# df=pd.DataFrame(d)
# print("--------------------------------------------------------")
# print(df)
# print("--------------------------------------------------------")
#?================================================================================================
# df.loc[1,"Fees"] = 15000
# df.loc[1,"Discount"] = 1000
# df["Duration"] = df["Duration"].fillna(35)
# df["Discount"] = df["Discount"].fillna(500)


# print(df)

#?================================================================================================
#! Consider the Following Problem
# import numpy as np, pandas as pd
# d={"Courses":["SPARK","JAVA","SCALA","PYTHON"],
#               "Fees":[20000,np.nan,26000,28000],
#                "Duration":["30days","40days",pd.NA,"40days"],
#                "Discount":[1000,np.nan,2500,None]}
# df=pd.DataFrame(d)
# print("--------------------------------------------------------")
# print(df)
# print("--------------------------------------------------------")
#?================================================================================================
# df.loc[1,["Fees","Discount"]] = [15000,"35Day"]  #!xxx
# print(df)

# df.loc[1,["Fees","Discount"]] = [15000,1000]
# print(df)
#?================================================================================================
# #!Dropping missing values


# import numpy as np,pandas as pd
# dict = {"First Score": [100,90,np.nan,95],
#         "Second Score" : [30,np.nan,45,56],
#         "Third Score" : [52,40,80,98],
#         "Fourth Score" : [np.nan,np.nan,np.nan,65]
# }
# df = pd.DataFrame(dict)
# print("------------------------------------------")
# print(df)
# print("-------------------------------------------")
#?================================================================================================
# print(df.dropna())     #*By deafult axis is 0
# print(df)

#*or

# print(df.dropna(axis=0))
# print(df)

#! for updating in dataframe itself
# df.dropna(inplace=True)    #*By deafult axis is 0
# print(df)
#*or
#!for updating in dataframe itself
# df.dropna(axis=0,inplace=True)
# print(df)

# print(df.dropna(axis=1))    #* Here axis=1 Represents Columns
# print(df)
#!for updating in dataframe itself
# df.dropna(axis=1,inplace=True)   #* Here axis=1 Represents Columns
# print(df)
#?================================================================================================
# import numpy as np,pandas as pd
# dict = {"First Score": [100,90,np.nan,95],
#         "Second Score" : [30,55,np.nan,56],
#         "Third Score" : [52,40,np.nan,98],
#         "Fourth Score" : [np.nan,np.nan,np.nan,65]
# }
# df = pd.DataFrame(dict)
# print("------------------------------------------")
# print(df)
# print("-------------------------------------------")
#?================================================================================================
# df.dropna(how="any",inplace=True)    #*default Value of 'how' argument is 'any' and default axis is 0 (row)
# print(df)

# df.dropna(how="all",inplace=True)   #!all asl tr delete hote 
# print(df)
#?================================================================================================
# import numpy as np
# import pandas as pd
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score':[52, 40, 80, 98],
#         'Fourth Score':[np.nan, np.nan, np.nan, np.nan]}
# df=pd.DataFrame(dict)
# print("---------------------------------------------------------")
# print(df)
# print("---------------------------------------------------------")
#?================================================================================================
# df.dropna(how="all",inplace=True)
# print(df)

# df.dropna(axis=1,how="all",inplace=True)
# print(df)
