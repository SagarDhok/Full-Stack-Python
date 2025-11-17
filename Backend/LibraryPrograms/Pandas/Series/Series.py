
#^===============================================================================================
#! Number of approaches to create an object of Series
#!int

# import pandas as pd
# a = 10
# s = pd.Series(a)
# print(s) #*dtype automatically print hote

# import pandas as pd
# a = 10
# s = pd.Series(a)
# print(s,type(s))

#!float
# import pandas as pd
# a = 10.4
# s = pd.Series(a)
# print(s,type(s))

#!bool
# import pandas as pd
# a = True
# s =  pd.Series(a)
# print(s,type(s))

#!complex
# import pandas as pd
# a = 2+3j
# s = pd.Series(a)
# print(s,type(s))

#^===============================================================================================
#!str
# import pandas as pd
# a  = "Python"
# s = pd.Series(a)
# print(s,type(s))

#!range
# import pandas as pd
# r = range(11,16)
# s = pd.Series(r)
# print(s,type(s))

#^===============================================================================================
#!list
# import pandas as pd
# lst = [100,200,300]
# s = pd.Series(lst)
# print(s,type(s))

# import pandas as pd
# lst = [100,200,300]
# s = pd.Series(lst,dtype= float)
# print(s,type(s))

#* internaly contains object type
# import pandas as pd
# lst = [100,"Rossum",45.67,"Python",True]
# s = pd.Series(lst)
# print(s,type(s))

# print(lst[0])

#& Creating Series Object with Index Names
# import pandas as pd
# lst= [100,"Rossum",45.67,"Python",True]
# s  = pd.Series(lst,index = ["EID","ENAME","SAL","LANG","STATUS"])
# print(s,type(s))

# print(s["EID"])
# # print(s[0])    #* gives warining

# print(s["ENAME"])
# print(s[1])    #* gives warining


#& Creating Series Object with Index Names
# import pandas as pd
# lst  =  [100,"Rossum",45.67,"Python",True]
# s = pd.Series(lst,index = [1,2,3,4,5])
# print(s,type(s))

# print(s[1])
# print(s[0])   #*KeyError


# import pandas as pd
# lst  =  [100,"Rossum",45.67,"Python",True]
# s= pd.Series(lst,index= [111,222,333,444,555])
# print(s,type(s))

# print(s[444])
# print(s[4])  #*KeyError: 4

# import pandas as pd
# lst = [[10,"RS"],[20,"TR"],[30,"DR"]]
# s= pd.Series(lst)
# print(s)

# print(s[0])


# import pandas as pd
# lst  = [[10,"RS"],[20,"TR"],[30,"DR"]]
# s = pd.Series(lst,index=["Rec1","Rec2","Rec3"])
# print(s,type(s))
# print(s["Rec1"])
# print(s[0])   #* gives warining


# print(s[::-1])

# import pandas as pd
# tpl= ([10,"Rs"],[20,"TR"],[30,"DR"])
# s= pd.Series(tpl,index = ["h","f","t"])
# print(s,type(s))

#& Creating an object of Series w.r.t set 
#* set and frozenset are not possible
# import pandas as pd
# st = {10,20,30,40,50}
# s  = pd.Series(st)
# print(s,type(s))


#* keys are treated as index
# import pandas as pd
# d = {10:10.5,2:20.5,3:30.6,4:40.3}
# s = pd.Series(d)
# print(s,type(s))
# print(s[10])


#*dict gives nan if indexes are changed it takes only keys as indexes
# import pandas as pd
# d = {10:10.5,2:20.5,3:30.6,4:40.3}
# s = pd.Series(d,index = ["a","b","c","d"])
# print(s,type(s))



#^=============================================================================================
#! converting ndarray object into Series
# import numpy as np
# import pandas as pd
# a = np.array([10,20,30,40,50])
# print("Content of a ")
# print(a,type(a))
# print("----------------------------")
# s= pd.Series(a)
# print(s,type(s))


# import numpy as np
# import pandas as pd
# a = np.array([10,20,30,40,50])
# print("Content of a")
# print(a,type(a))
# print("----------------------------")
# s = pd.Series(a,index = ["ID1","ID2","ID3","ID4","ID5"])
# print(s,type(s))

# print(s["ID1"])
# print(s[0])    #* gives warning

#^=============================================================================================

import pandas as pd
dict = {1:"sagar",2:"jay",3:"karan"}