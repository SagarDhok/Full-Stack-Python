


#! 4.randn()
#* positive or negative
#* Syntax-1: numpy.random.randn()
#^---------------------------------------------------------------------------------------
# from numpy import random as r
# rv = r.randn() 
# print(rv,type(rv))    # op -1.2972740892789987 <class 'float'>
 

# from numpy import random as r
# rv = r.randn() 
# print(rv,type(rv))   # op 1.015245721310732 <class 'float'>
 

#^---------------------------------------------------------------------------------------
#* Syntax-2: numpy.random.randn(value)
#* Generating Number of Random floating Values (Value times) 
#* for standard Normal Distribution and either +ve or -ve

# from numpy import random as r
# rv = r.randn(4)
# print(rv,type(rv))   #op = [1.62870629 1.72544495 0.91705791 0.27054963] <class 'numpy.ndarray'>
#^---------------------------------------------------------------------------------------
#* Syntax-3: numpy.random.randn(rows ,cols)
#* Syntax-4: numpy.random.randn(matrices,rows ,cols)

# import numpy.random as r
# a = r.randn(2,3)
# print(a,type(a))  # op [[-0.13462942  0.4330975  -1.59022803]
#  [-0.65584012  1.86181281  0.21311579]]  <class 'numpy.ndarray'> 
 
# import numpy.random as r
# rv = r.randn(2,3,3)

# for mn in range(len(rv)):
#     for rn in range(len(rv[0])):
#         for cn in range(len(rv[0])):
#             print(round(rv[mn,rn,cn],2),end="\t")
#         print()
#     print()


# import numpy.random as r
# for mn in rv:
#     for rn in mn:
#         for cn in rn:
#             print(round(cn,2),end="\t") 
#         print()
#     print()
