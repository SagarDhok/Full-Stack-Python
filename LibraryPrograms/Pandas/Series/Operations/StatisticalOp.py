
#! statistical operation 
#*                              Syntax:           seriesobj.sum()
#*										seriesobj.count()
#*										seriesobj.max()
#*										seriesobj.min()
#*										seriesobj.mean()
#*										seriesobj.median()
#*										seriesobj.var()
#*										seriesobj.std()
#*										seriesobj.mode()	#
#*										seriesobj.describe()
#*                                                seriesobj.product()
#*										seriesobj.cumprod()
#*										print(seriesobj.agg(["max","min","mean".........]))
#*										

# ^===============================================================================================
# import pandas as pd
# s = pd.Series([10,2,5,13,5,8])
# print("Series of values ")
# print(s)
# print("-------------------------------")
# print("Sum of series of elements : ",s.sum())
# print("Max of series of elements : ",s.max())
# print("Min of Series of Elements : ",s.min())
# print("Median of Series of ELemenst : ",s.median())
# print("Number of Elements in Series :",s.count())
# print("Mean of the Series : ",s.mean())
# print("Variance of Series : ",s.var())
# print("Standard Deviation of Series : ",s.std())
# print("Mode of Series : ",s.mode())


# ^===============================================================================================
# import pandas as pd
# s = pd.Series([2,5,3,4])
# print("series of values ")
# print(s)
# print("---------------------------------")
# print("Product of series : ",s.product())
# print("Cumulative product of series of element : \n",s.cumprod())


# ^===============================================================================================
# import pandas as pd
# s = pd.Series([10,2,5,13,5,8])
# print("Series of Values ")
# print(s)
# print("Summery of series of ELements ")
# print(s.describe())


# import pandas as pd
# s = pd.Series(["rs","tr","dr","rs","ss"])
# print("Series of values")
# print(s)
# print("Summery of Series of Elements ")
# print(s.describe())

# import pandas as pd
# s = pd.Series([10,20,"RS",30,"TR","DR",10,"RS","SS",30])
# print("Series of Values ")
# print(s)
# print("Summery of Series of Elements")
# print(s.describe(include="all"))  #*ignored in series available in dataframe
# ^===============================================================================================
