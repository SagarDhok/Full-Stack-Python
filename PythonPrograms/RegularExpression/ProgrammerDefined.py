
#&Programmer defined character classes
#!Program for Searching A or B or C only
#!RegExpr4.py
# import re
# gd="Ak5#GnRp@7W&BYPQs6!CMx"
# sp = "[ABC]"
# matdet = re.finditer(sp,gd)
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()}")
#^==============================================================================================
#!Program for Searching A or B or C only
#!RegExpr5.py
# import re
# matdet = re.finditer("[ABC]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()}")
#^==============================================================================================
#! Program for Searching for all  except A or B or C only
#! RegExpr6.py
# import re 
# matdet = re.finditer("[^ABC]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t  Value:{mat.group()}")

#^==============================================================================================
#!Program for Searching for all Upper Case Alphabets
#!RegExpr7.py
# import re 
# matdet = re.finditer("[A-Z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()}")
#^==============================================================================================
#! Program for Searching for all  except Upper Case Alphabets
#! RegExpr8.py
# import re
# matdet = re.finditer("[^A-Z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t  Value:{mat.group()}")
#^==============================================================================================
#! Program for Searching for all Lower Case Alphabets
#! RegExpr9.py
# import re 
# matdet  = re.finditer("[a-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value: {mat.group()} ")
#^==============================================================================================
#^==============================================================================================
#! Program for Searching for Upper  and Lower Case Alphabets only
#! RegExpr11.py
# import re 
# matdet = re.finditer("[A-Za-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index: {mat.start()}\t End Index: {mat.end()} \t Value : {mat.group()}")

#^==============================================================================================
#! Program for Searching for all except Upper  and Lower Case Alphabets
#! RegExpr12.py
# import re 
# matdet = re.finditer("[^A-Za-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value : {mat.group()}")
#^==============================================================================================
#!Program for Searching only Digits
#!RegExpr13.py
# import re 
# matdet = re.finditer("[0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()} ")


# import re 
# matdet = re.finditer("[56]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()} ")
#^==============================================================================================
#!Program for Searching for all except  Digits
#!RegExpr14.py
# import re 
# metdata = re.finditer("[^0-9]","k5#GnRp@7W&BYPQs6!CMx")
# for mat in metdata:
#   print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()}")
#^==============================================================================================
#!Program for Searching for all Alpha-numerics only
#!RegExpr15.py
# import re 
# metdata = re.finditer("[A-Za-z0-9]","k5#GnRp@7W&BYPQs6!CMx")
# for mat in metdata: 
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t Value:{mat.group()}")
#^==============================================================================================
#!Program for Searching for all Special Symbols only
#!RegExpr16.py
# import re 
# nos = 0
# metdata= re.finditer("[^A-Za-z0-9]","k5#GnRp@7W&BYPQs6!CMx")
# for mat in metdata:
#      nos = nos+1
#      print(f"Start Index:{mat.start()}\t End Index:{mat.end()}\t Value:{mat.group()}")
# print("Number of special symbol : ",nos)
#^==============================================================================================
#!Program for Searching for Upper case Alphabets and Digits only
#!RegExpr17.py
# import re
# metdata= re.finditer("[A-Z0-9]","k5#GnRp@7W&BYPQs6!CMx")
# for mat in metdata:
#      print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t Value : {mat.group()}")
#^==============================================================================================
#!Program for Searching for all except  Upper case Alphabets and Digits only
#!RegExpr18.py
# import re 
# metdata = re.finditer("[^A-Z0-9]","k5#GnRp@7W&BYPQs6!CMx")
# for mat in metdata:
#      print(f"Start Index :{mat.start()} \t End Index : {mat.end()} \t Value : {mat.group()}")
#^==============================================================================================
#!Program for Searching for all Lower case Alphabets and Digits only
#!RegExpr19.py
# import re
# metdata= re.finditer("[a-z0-9]","k5#GnRp@7W&BYPQs6!CMx")
# for mat in metdata:
#      print(f"Start Index :{mat.start()} \t End Index :{mat.end()} \t Value:{mat.group()}")
#^==============================================================================================
#!Program for Searching for all  except Lower case Alphabets and Digits 
#!RegExpr20.py
# import re
# metdata= re.finditer("[^a-z0-9]","k5#GnRp@7W&BYPQs6!CMx")
#      print(f"Start Index :{mat.start()} \t End Index : {mat.end()} \t Value: {mat.group()}")
# for mat in metdata : 
#^==============================================================================================
