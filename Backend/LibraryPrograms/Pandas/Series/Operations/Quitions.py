

# ^===============================================================================================

# import pandas as pd
# import numpy as np
# s=pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of Elements")
# print(s,type(s))

# for val in s:
#      print(str(val).lower())

# lowerlst= [str(val).lower() for val in s]
# print(lowerlst)

# print("-----------------------")
# sl = [str(val).lower() for val in s if str(val)!="nan"]
# print(sl)

# print("--------------------------")
# ul =   [str(val).upper() for val in s if str(val)!="nan"]
# print(ul)


                                                         
# dictobj = {str(val).lower():len(val) for val in s if str(val)!="nan"}
# print(dictobj)
# for k , v in dictobj.items():
#      print(f"{k}: {v}")
# ^===============================================================================================
#* 6.2: From the raw data below create a Pandas Series ' Atul', 'John ', ' jack ', 'Sam'
#* a) Print all elements after stripping spaces from the left and right
#* b) Print all the elements after removing spaces from the left only
#* c) Print all the elements after removing spaces from the right only
# import pandas as pd
# series_2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
# print(series_2)


# strp   = [str(val).strip() for val in series_2 ]
# print(strp)

# lstrp = [str(val).lstrip() for val in series_2]
# print(lstrp)

# rstrp = [str(val).rstrip() for val in series_2]
# print(rstrp)
# ^===============================================================================================
# import pandas as pd,numpy as np
# series_3 = pd.Series(
#     ['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
# print(series_3)

# lst = [str(val).split("_") for val in series_3]
# print(lst)

# clst = [ ]
# for  sulst in lst:
#   for val in sulst:
    
#    clst.append(val)
# print(" ".join(clst))

# s = ""
# for sublst in lst:
#    for val in sublst:
#      s = s + " " + val


# ^===============================================================================================

# import pandas as pd
# x = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit2.csv")
# print(x,type(x))
# print(x.shape)
# print("--------")
# s=  x["Name"]
# print(s,type(s))

# import pandas as pd
# x = pd.read_csv("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit2.csv")["Name"]
# print(x,type(x))
# print(x.shape)
# ^===============================================================================================