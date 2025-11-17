
import pandas as pd,numpy as np

#^==============================================================================================
lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
s = pd.Series(lst)
print("Series object data")
print(s,type(s),id(s))

#&Accessing single the Element of Series by using indices
# print(s[0])
# print(s[6])

# print(s[-1])  #* keyerror -ve indexing is not possible in pandas

#& Accessing the Multiple Elements of Series by using Indices

# print(s[0:5])  #*end -1 -> 0 to 4 deter
print(":----------")
# print(s[::2])
# print(s[-1:-5:-1])
# print(s[1::2][::-1])   #* reverse is possible not negative indexing

#& Accessing the  Random Element of Series by using Random Indices
# print(s[[2,5,6]])
# print(s[[0,2,6]])


#& changing Single Element by using Index
# s[0] = "Guido van rossum"
# s[3]  = "Rexon"
# print(s,id(s))


#& changing Multiple Elements by using slicing
# s[0:3] = "Ronaldo","Messi","Neymar"
# print(s,id(s))

#& changing Random Multiple Elements by using Random Indices
# s[[0,5,1]] = "AK","VK","RX"
# print(s,id(s))

#^==============================================================================================
#* it is case sensitive
#! X
# lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# index= ["name"+str(val) for val in range(1,len(lst)+1) ]
# s = pd.Series(lst,index)
# print(s,type(s))


# lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# s = pd.Series(lst,index=["name1","name2","name3","name4","name5","name6","name7"])
# print(s,type(s),id(s))



#& Accessing the  Element of Series by using Label
# print(s["name1"])     
# print(s['name6'])


#& Accessing the Multiple Elements of Series by using Label names
# print(s["name1":"name5"])   #* name1 to name5 not-1 
# print(s["name3": ])
# print(s['name1'::2])
# print(s["name2"::2])

# print(s["name1":"name4"][::-1])   #* reverse is  possible


#& Accessing the  Random Element of Series by using Random Label Name
# print(s[["name1","name2","name7"]])
# print(s[["name2","name5"]])



#& changing Single Element by using Label
# s["name3"] = "Rowdy Rathoe"
# s["name7"] = "Bhavesh Joshi"
# print(s,id(s))

#& changing Multiple Elements by using slicing
# s["name1":"name3"] = "karan","arjun","jay"
# print(s,id(s))



#&changing Random Multiple Elements by using Random Labels
# s[["name2","name7"]] = "salman" ,"shahrukh"
# print(s,id(s))


# s[["name3","name6"]] = "bhim","chutki"
# print(s,id(s))
#^==============================================================================================

# import pandas as pd
# # Create a Series object from a list
# names = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
#                     index = ['a', 'b', 'c', 'd', 'e', 'f'])
# print(names)
# names['a' : 'd'] = 'Smriti'
# # Display the Series
# print(names)