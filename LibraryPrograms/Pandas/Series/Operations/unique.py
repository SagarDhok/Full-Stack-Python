

#! unique()
# * series = s.unique()
# ^===============================================================================================
# & Finding Unique Values from series object
# import numpy as np, pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of valeus ")
# print(s)
# print(s.unique(),type(s.unique()))

# &Our Code for Finding Unique Values from series object
# import numpy as np, pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of valeus ")
# print(s)
# lst = []
# for val in s:
#      if val not in lst:
#           lst.append(val)
# print("--------------------")
# a = np.array(lst)
# print("Unique Values  ")
# print(a,type(a))
# ^===============================================================================================
# & Finding Number of Occuences of Series of Elements
# import numpy as np, pandas as pd
# a= pd.Series([0,20,10,20,30,10,30,20,10,15,25])
# print("Series of values ")
# print(a)

# print("------------------------------")
# x= a.value_counts()
# print(x,type(x))

# & Our Own Code for Finding Number of Occurences of Series of Elements

# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of Values")
# print(s)

# dictobj = {}
# for val in s:
#      if val not in dictobj:
#           dictobj[val] = 1
#      else:
#           dictobj[val]  = dictobj[val]+1

# print(dictobj)

# print("-----------------------------")
# for key, value in  dictobj.items():
#      print(f"{key} : {value}")
# print("-----------------------------")
# ^===============================================================================================

#& To Find Number of Unique Values of Series Object---we use nunique()
# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of values ")
# print(s)

# nou = s.nunique()
# print("Number of unique values : ",nou)

# print("Number of Uniue values : ",s.value_counts().size)

# print("Number of uniue value : ",s.value_counts().count())
# ^===============================================================================================

#! one program

# import numpy as np, pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of valeus ")
# print(s)
# print("----------------------")

#& using unique funtion
# print(s.unique(),type(s.unique()))
# &Our Code for Finding Unique Values from series object
# lst = []
# for val in s:
#      if val not in lst:
#           lst.append(val)
# print("--------------------")
# a = np.array(lst)
# print("Unique Values  ")
# print(a,type(a))

# & Finding Number of Occuences of Series of Elements
# x= s.value_counts()
# print(x,type(x))


# & Our Own Code for Finding Number of Occurences of Series of Elements
# dictobj = {}
# for val in s:
#      if val not in dictobj:
#           dictobj[val] = 1
#      else:
#           dictobj[val]  = dictobj[val]+1

# print("-----------------------------")
# for key, value in  dictobj.items():
#      print(f"{key} : {value}")
# print("-----------------------------")


#& To Find Number of Unique Values of Series Object---we use nunique()
# nou = s.nunique()
# print("Number of unique values : ",nou)

# print("Number of Uniue values : ",s.value_counts().size)

# print("Number of uniue value : ",s.value_counts().count())