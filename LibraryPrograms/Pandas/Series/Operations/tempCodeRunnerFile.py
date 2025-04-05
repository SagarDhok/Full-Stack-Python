import pandas as pd,numpy as np
a = pd.Series([100,200,np.NAN,400,None],index = ["a","b","c","d","e"])
print("---------------------------")
print("Series - 1")
print(a)
print("---------------------------")
print(a.isnull()) 