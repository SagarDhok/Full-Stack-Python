


#! Note--Series Attributes are
#* 1. name
#* 2. values
#* 3. size
#* 4. empty
#* 5 dtype



#!name 
#* syntax  = pdobj.name = "name" - setting name
             #*print(pdobj.name)  - getting name
#^==============================================================================================
# import numpy as np, pandas as pd
# lst = ["Rossum","Travis","Ritchie","Dennis","Hunter"]
# s = pd.Series(lst)
# # print()
# print("Series object data",s)
# print("values",s.values,type(s.values))  

# print("Series Name : ",s.name) #* Series Name :  None

# lst = ["Rossum","Travis","Ritchie","Dennis","Hunter"]
# s = pd.Series(lst,name="Emp")
# print("Series object data")
# print(s,type(s))

# lst = ["Rossum","Travis","Ritchie","Dennis","Hunter"]
# s= pd.Series(lst,index = [100,200,300,400,500],name = "Emp")
# print(s,type(s))

# print("Values type in s: ",s.dtype)
# print("is s is empty : ",s.empty)

# #&get the Series Name-----Attribute name is name
# print("Series name : ",s.name)

# s.name = "Scientis"
# print("Series Name :",s.name)

#& get all the values Series by using 'values'
# print(s.values,type(s.values))  #* gives values in ndarray


# for val in s.values:
#      print(val)
#& Get Number of Values in series object--'size'
# print("Number of elements :",s.size)




# s1 = pd.Series([10,20,30,np.NAN,40,50,np.NAN])
# print(s1,type(s1))

# print("Number of elements with size ",s1.size)  #* attribute nan None value dharte

# print("Number of element with count : ",s1.count())  #* funtion and nan None chi value nahi dharat

# print("Value type in s1 : ",s1.dtype)

# print("Is s1 is empty :",s1.empty)

#&Create an empty Series object
# s2= pd.Series()
# print(s2,type(s2))

# print("is s2 is empty : ",s2.empty)
#^==============================================================================================