

#! 5.normal()
#* by default
#*r.normal(loc=0.0, scale=1.0, size=None)\
#^---------------------------------------------------------------------------------------
#* Syntax-1: numpy.random.randn()

# from numpy import random as r
# rv  = r.normal()
# print(rv,type(rv))  #op  1.3467374060474828 <class 'float'>

# from numpy import random as r
# rv  = r.normal()
# print(rv,type(rv))  #op  -1.7155371683504048 <class 'float'> 


#^---------------------------------------------------------------------------------------
#* Syntax-2: numpy.random.normal(loc=0.0,scale=1.0)
# from numpy import random as r 
# rv = r.normal(3)
# print(rv,type(rv))   #op  3.8456157825767754  <class 'float'> 

# from numpy import random as r 
# rv = r.normal(3)
# print(rv,type(rv))   #op 4.860960067821276 <class 'float'> 


# from numpy import random as r 
# rv = r.normal(3,4)
# print(rv,type(rv))  #op -8.931883424824782 <class 'float'>

#^---------------------------------------------------------------------------------------
#* Syntax-3: numpy.random.normal(loc=0.0,scale=1.0,size=None)

# from numpy import random as r 
# rv = r.normal(2,3,size=(3))
# print(rv,type(rv))      #op [ 2.24278783 -2.84013211 -0.20537968] <class 'numpy.ndarray'>


# from numpy import random as r 
# rv = r.normal(2,3,size=(3,3))
# print(rv,type(rv))  

# from numpy import random as r 
# rv = r.normal(2,3,size=(2,3,3))
# print(rv,type(rv))  