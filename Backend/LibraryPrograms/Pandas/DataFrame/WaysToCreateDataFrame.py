
#* We can't create DataFrame Object with Fundamental Traditional Python Object.
#* We must create Fundamental Traditional Python Object into Iterable Objects by 
#* using Type Casting Functions
#?================================================================================================
#! Fundamental data types
#?================================================================================================
#!int
# import pandas as pd
# a= 10
# df = pd.DataFrame([a])
# print("Content of dataframe")
# print(df,type(df))

#?================================================================================================
#!float
# import pandas as pd
# a = 10.4
# df= pd.DataFrame([a])
# print("Content of dataframe")
# print(df,type(df))
#?================================================================================================
#!bool
# import pandas as pd
# a = True
# df = pd.DataFrame([a])
# print("Content of dataframe")
# print(df,type(df))
#?================================================================================================
#!complex
# import pandas as pd
# a = 2+3j
# df= pd.DataFrame([a])
# print("Conternt of a")
# print(df,type(df))
#?================================================================================================
#!Sequential data types
#?================================================================================================
#!str
# import pandas as pd
# s = "python"
# df  = pd.DataFrame([s])
# print("Content of a")
# print(df,type(df))

# import pandas as pd
# s = "python"
# df  = pd.DataFrame(list(s))
# print("Content of dataframe")
# print(df,type(df))
#?================================================================================================
#! range
# import pandas as pd
# r = range(10,21,2)
# df = pd.DataFrame(r)
# print("COntent of dataframe")
# print(df)
#?================================================================================================
#!list category
#?================================================================================================
#& Create an object of DataFrame By using list
# import pandas as pd
# lst = [100,200,300,400,500,600]
# df = pd.DataFrame(lst)
# print("Contern of lst")
# print(df,type(df))

# import pandas as pd
# lst =  [100,200,300,400,500,600]
# df = pd.DataFrame(lst,dtype=float)
# print("Content of dataframe")
# print(df,type(df))


# import pandas as pd
# lst = [100,"Rossum",45.67,"Python"]
# df = pd.DataFrame(lst)
# print("Content of dataframe")
# print(df,type(df))

import pandas as pd
# lst =[100,"Rossum",45.67,"Python"]
# df = pd.DataFrame(lst,index=["ID","NAME","MARKS","SUBJECT"])
# print("Content of a ")
# print(df,type(df))

# import pandas as pd
# lst = [100,"Rossum",45.67,"Python"]
# df = pd.DataFrame(lst,columns=["Records"])
# print("Content of dataframe")
# print(df)

# import pandas as pd
# lst  = [100,"Rossum",45.67,"Python"]
# df = pd.DataFrame(lst,index=["ID","NAME","MARKS","SUBJECTS"],columns=["Records"])
# print("Content of Dataframe")
# print(df,type(df))
# print(df.ndim)
# print(df.shape)

# import pandas as pd
# lst = [[100],["Rossum"],[45.67],["Python"]]
# df = pd.DataFrame(lst)
# print("Content of dataframe")
# print(df,type(df))

# import pandas as pd
# lst = [[100,"Rossum",45.67,"Python"]]
# df = pd.DataFrame(lst)
# print("Content of dataframe")
# print(df,type(df))

# import pandas as pd
# lst = [[100,"Rossum",45.57,"Python"]]
# df = pd.DataFrame(lst,index = ["Records"],columns=["ID","NAME","MARKS","SUBJECTS"])
# print("Content of Dataframe")
# print(df,type(df))

# import pandas as pd
# lst = [[100,"Rossum",45,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"Matplolib"]]
# df = pd.DataFrame(lst,index=["Record1","Record2","Record3"],columns=["NAME","ID","MARKS","SUBJECTS"])
# print("Content of dataframe")
# print(df,type(df))
# print(df.ndim)
# print(df.shape)
# print("Number of rows : ",df.shape[0])
# print("Number of colums : ",df.shape[1])


# import pandas as pd
# lst = [[100,"Rossum",45,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"Matplolib"]]
# df  = pd.DataFrame(lst,index=["Record1"+str(val) for val in range(1,len(lst)+1)])
# print("Content of df")
# print(df)

# import pandas as pd
# lst = [[100,"Rossum",45,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"Matplolib"]]
# df = pd.DataFrame(lst,index=["Record"+str(i) for i in range(1,len(lst)+1)],
#                       columns=["Column"+str(j) for j in range(1,len(lst[0])+1)]
#                   )
# print("Content of  dataframe")
# print(df)
#?================================================================================================
#!tuple
# import pandas as pd
# tpl = ((10,"Rs"),(20,"Dr"),(30,"Jh"),(40,"Ss"))
# df = pd.DataFrame(tpl,index = ["Record"+str(i) for i in range(1,len(tpl)+1)],
#                   columns=["ID","NAME"]
#                   )
# print("Content of dataframe")
# print(df)


# import pandas as pd
# tpl = ([10,20,30,40],["TR","DR","SS","JH"])
# df = pd.DataFrame(tpl)
# print("COntent of dataframe")
# print(df,type(df))


#* Implement the Following  with dataframe object
#*		      CL		HL		PL
#* SBI		8.2		7.8		11.2 
#* HDFC         7.8		8.8		12.4
#* ICICI		8.5		8.7		10.5

# import pandas as pd
# loans =[[8.2,7.8,11.2 ],[7.8,8.8,12.4],[8.5,8.7,10.5]]
# df = pd.DataFrame(loans,index= ["SBI","HDFC","ICICI"],columns=["CL","HL","PL"])
# print("Content of dataframe")
# print(df,type(df))

# import pandas as pd
# loans = [{8.2,7.8,11.2},(7.8,8.8,12.4),[8.5,8.7,10.5]]
# df = pd.DataFrame(loans,index = ["SBI","HDFC","ICICI"],columns=["CL","HL","PL"])
# print("Content of dataframe")
# print(df)
#?================================================================================================
#! Converting set object into DataFrame
# import pandas as pd
# s={8.2,7.8,11.2}
# df = pd.DataFrame(s)
# print("Content of df")
# print(df,type(df))
#?================================================================================================
#! Converting frozenet  object into DataFrame
# import pandas as pd
# s= frozenset({8.2,7.8,11.2})
# df = pd.DataFrame(s)
# print("Content of dataframe")
# print(df,type(df))
#?================================================================================================
#! Converting Dict  object into DataFrame 
#*keys becomes rows here 
#* in numpy keys becomes colums

#& "Pandas DataFrame requires dictionary values to be iterables. Since I passed single integers instead of lists, Pandas couldn't form rows, which caused the error. Wrapping values in lists fixes the issue." ✅💡

# import pandas as pd
# dictobj = {"Python":1,"C":2,"C++":3,"Java":4}
# df = pd.DataFrame(dictobj,index=[1])      #*plane normal error if index is not given
# print("Content of dataframe")    
# print(df,type(df))

# import pandas as pd 
# dictobj = {"ID":[100,200,300],"Name" :["Rossum","Travis","Hunter"],"AGE":[99,78,88]}
# df = pd.DataFrame(dictobj)
# print("Content of dataframe")
# print(df,type(df))

# import pandas as pd 
# dictobj = {"ID":[100,200,300],"Name" :["Rossum","Travis","Hunter"],"AGE":[99,78,88]}
# df= pd.DataFrame(dictobj,index=["Record1","Record2","Record3"])
# print("Content of dataframe")
# print(df,type(df))



#?================================================================================================
#! Create DataFrame Object from Series Object
# import pandas as pd
# lst= [100,200,300,400,500]
# s = pd.Series(lst)
# print("Serises of data")
# print(s,type(s))
# # print("----------------------------------")
# df= pd.DataFrame(s)
# print(df,type(df))
#?================================================================================================
#! Create DataFrame Object from ndarray
# import numpy as np,pandas as pd
# lst = [100,200,300,400,500]
# a= np.array(lst)
# print("Ndarray data")
# print(a,type(a))
# print("----------------------------------")
# df = pd.DataFrame(a)
# print("Content of dataframe")
# print(df,type(df))
#?================================================================================================
#! Create NDArray Object by using CSV File
# import pandas as pd
# df= pd.read_csv("E:\\FULL STACK PYTHON\\PythonPrograms\\Files\\CsvFile\\stud1.csv")
# print(df,type(df))

# print("----------------")
# print(df["Name"],type(df["Name"]))


#! Create an object of DataFrame by using CSV File
# import pandas as pd
# df= pd.read_csv("E:\FULL STACK PYTHON\LibraryPrograms\Pandas\DataFrame\population.csv")
# print(df)
#?================================================================================================