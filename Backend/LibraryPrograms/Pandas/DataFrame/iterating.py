
#?================================================================================================

# import numpy as np,pandas as pd
# lst = [[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
# df = pd.DataFrame(lst)
# print(df)

#      0    1    2    3    4
# 0   10   20   30   40   50
# 1   RS   TR   SS   DR   JH
# 2  1.2  2.3  4.5  5.6  6.7
#?================================================================================================
#& 1. Iterating the DataFrame Object Data by using Row Indices
# for rec in df.iterrows():
#      print(rec)   #& it gives tuple

# for rec in df.iterrows():
#      print(f"Row Index : {rec[0]}")
#      print(f"Record values  : {rec[1].values}")



#& 1. Iterating the DataFrame Object Data by using Row Indices
# for (rind,rvals)in df.iterrows():  #*or for rind,rvals in df.iterrows():
#      print(f"Row Index :  {rind}")
#      print(f"Row Values :{rvals.values}")


#& 1. Iterating the DataFrame Object Data by using Row Indices
# for i in range(df.shape[0]):
#      print("Row index value :",i)
#      print("Row values : ",df.iloc[i].values)

#& 1. Iterating the DataFrame Object Data by using Row Indices
# for i in range(df.shape[0]):
#      print("Row index value : ",i)
#      print("Row values : ",df.iloc[1].values)
#?================================================================================================
# import numpy as np,pandas as pd
# lst = [[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
# df = pd.DataFrame(lst,index=["ID","NAME","CGPA"])
# print(df)



#?================================================================================================
#& 2.Iterating the DataFrame Object Data by using Row Names
# for (rowname,rowvals) in df.iterrows():
#      print("Row index name : ",rowname)
#      print("Row values : ",rowvals.values)

#& 2.Iterating the DataFrame Object Data by using Row Names
# for rec in df.iterrows():
#  print("Row index Name  : ",rec[0])
#  print("Row values  : ",rec[1].values)
 
#?================================================================================================
#& 3.Iterating the DataFrame Object Data by using  Col Names
# import pandas as pd,numpy as np
# lst = [[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
# df = pd.DataFrame(lst,columns=["Rec1","Rec2","Rec3","Rec4","Rec5"])
# print(df)
#?================================================================================================
#& 3.Iterating the DataFrame Object Data by using  Col Names
# for colname in df.columns:
#      print(f"Column Name : {colname}")
#      print(f"Column Values  : {df[colname].values}")

#?================================================================================================
import pandas as pd,numpy as np
lst =[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
df = pd.DataFrame(lst)
print(df)

#?================================================================================================
#& 4. Iterating the DataFrame Object Data by using Column  Indices
for colindex in range(df.shape[1]):
     print(f"Column Index : {colindex}")
     print(f"Column data  : {df.iloc[:,colindex].values}")