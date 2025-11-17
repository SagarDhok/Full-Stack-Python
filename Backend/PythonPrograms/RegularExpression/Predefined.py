
#& Predefined Character Class
#^==============================================================================================
#!Program for Searching the digits  
#! RegExpr21.py
#* "[0-9]"
# import re
# metdet = re.finditer(r"\d","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in metdet:
#      print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value: {mat.group()}")

#* d+ one or more than one 
#* \dd two digits
#* \ddd {3}
#* \d{4}
#* \d{2,4} minimum 2 and maximum 4 
#* "[A-za-z]{3}"
#* \dd.\dd decimal number

# import re
# metdet = re.finditer("[A-Za-z0-9]{5}","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in metdet:
#      print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value: {mat.group()}")


# import re
# metdet = re.finditer(r"\d\d.\d\d","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in metdet:
#      print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value: {mat.group()}")


#^==============================================================================================
#! Program for Searching  for all  except the digits
#! RegExpr22.py
#*"[^0-9]"
# import re
# metdet = re.findall(r"\D","Ak5Y#GnRp@7W&bP)s6!CMx")
# print(metdet)  
# for mat in metdet:
#      print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value : {mat.group()}")
#^==============================================================================================
#!Program for Searching  for  Word Characters ( Alphabets+Digits) Only
#!RegExpr23.py  
#* "[A-Za-z0-9]"
# import re 
# metdet = re.finditer(r"\w","Ak5Y#GnRp@7W&bP)s6!CMx")
# for mat in metdet : 
#      print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t Value : {mat.group()}")

#^==============================================================================================
#!Program for Searching  for all special Symbols
#!RegExpr24.py
#* "[^A-Za-z0-9]"
# import re
# metdet = re.finditer(r"\W","Ak 5Y#GnRp@7W&bP) s6!CMx")
# for mat in metdet:
#      print(f"Start Index:{mat.start()} \t End Index: {mat.end()} \t Value : {mat.group()} ")
#^==============================================================================================
#! Program for Searching  Space Characetr Only
#! RegExpr25.py
#* Here r means raw
# import re
# metdet = re.finditer(r"\s", "A k5Y#GnRp @7W&bP)s6!CMx")
# for met in metdet:
#     print(f"Start Index: {met.start()}  End Index: {met.end()}  Value: {met.group()}")
#^==============================================================================================
#!Program for Searching  Except Space Characetr Only
#!RegExpr26.py
# import re
# metdet = re.finditer(r"\S","A k5Y#GnRp @7W&bP)s6!CMx")
# for met in metdet : 
#      print(f"Start Index:{met.start()} \tEnd Index:{met.end()}\t Value : {met.group()}")
#^==============================================================================================
#& Quantifiers in Regular  Expression 
#^==============================================================================================
#!Program for Searching  One Char exactly 'K'
#!RegExpr27.py
# import re
# metdet= re.finditer("K","KVKKVKKKVKV")
# for met in metdet:
#      print(f"Start Index:{met.start()} \t End Index : {met.end()} \t Value:{met.group()}")
#^==============================================================================================
#!Program for Searching  One K OR More K's
#!RegExpr28.py
# import re
# metdet = re.finditer("K+","KVKKVKKKVKV")
# for met in metdet:
#      print(f"Start Index : {met.start()} \t End Index : {met.end()} \t {met.group()}")
#^==============================================================================================
#!Program for Searching  Zero K or One K OR More K's
#!RegExpr29.py
#* place vaar k nasal ki space dete 
# import re
# metdet = re.finditer("K*","KVKKVKKKVKV") 
# for met in metdet : 
#      print(f"Start Index:{met.start()} \t End Index : {met.end()} \t Value:{met.group()} ")

#^==============================================================================================
#!Program for Searching  Zero K or One K 
#!RegExpr30.py
#* one k asl tr nasla tr space 
# import re 
# metdet = re.finditer("K?","KVKKVKKKVKV")
# for met in metdet:
#      print(f"Start Index:{met.start()} \t End Index :{met.end()} \t Value :{met.group()}")
#^==============================================================================================
#!Program for Searching  Each and Every Character
#!RegExpr31.py
# import re 
# metdet = re.finditer(".","KVKKVKKKVKV")
# for met in metdet:
#      print(f"Start Index:{met.start()} \t End Index:{met.end()} \t Value:{met.group()}")
#^==============================================================================================