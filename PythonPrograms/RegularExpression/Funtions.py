
#*applied only on str data

#!findall()
#^==============================================================================================
# import re
# gd = "Python is oop langauge.Python is fun lang"
# sp = "Python"
# kvr = re.findall(sp,gd)
# print(kvr,type(kvr))    #* ['Python', 'Python'] <class 'list'>
   

# import re
# gd = "Python is oop langauge.Python is fun lang"
# sp = "kvr"
# kvr = re.findall(sp,gd)
# print(kvr,type(kvr))   #*[] <class 'list'>

#^==============================================================================================
#!search()
#& gives the first occurence 

# import re
# gd = "Python is oop langauge.Python is fun lang"
# sp = "Python"
# mat = re.search(sp,gd)   #*endindex +1
# print(mat)               #* <re.Match object; span=(0, 6), matdet='Python'>
# print(type(mat))         #*<class 're.Match'>

# import re
# gd = "Python is oop langauge.Python is fun lang"
# sp = "kvr"
# mat = re.search(sp,gd)   
# print(mat)           #* None
# print(type(mat))     #*class 'NoneType'>


# import re
# gd = "Python is oop langauge.Python is fun lang"
# sp = "Python"
# mat = re.search(sp,gd)   #*endindex +1
# if mat != None:
#      print("Search is successfull")
#      print("start value : ",mat.start())
#      print("end value : ",mat.end())
#      print("value : ",mat.group())

# else:
#      print("Seach is unsuccesfull")
#^==============================================================================================
#! finditer()
#& gives the all occurence
# import re
# gd = "Python is an oop lang.Python is also fun lang"
# sp = "Python"
# x = re.finditer(sp,gd)

# # print(x)        #*<callable_iterator object at 0x000001B1D1E07F10>
# # print(type(x))    #*<class 'callable_iterator'>

# for k in x:
#      # print(k,type(k))   #* type of k <class 're.Match'> 

#      print(f"Start Index:{k.start()} \t End Index:{k.end()} \t value:{k.group()}")


#! if no then no output
# import re
# gd = "Python is an oop lang.Python is also fun lang"
# sp = "kvr"
# x = re.finditer(sp,gd)
# for k in x:
#      print(f"Start Index:{k.start()} \t End Index:{k.end()} \t value:{k.group()}")
#^==============================================================================================
