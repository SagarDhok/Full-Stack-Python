
#! 6.choice()
#^---------------------------------------------------------------------------------------
# import numpy as np
# import numpy.random as r
# a = np.array([10,20,30,40,50,60])
# print(a,type(a)) #op [10 20 30 40 50 60] <class 'numpy.ndarray'>

# cv = r.choice(a)
# print(cv,type(cv))  #30 <class 'numpy.int32'>

# cv = r.choice(a)
# print(cv,type(cv))  #50 <class 'numpy.int32'>
#^---------------------------------------------------------------------------------------
# import numpy as np
# from numpy import random as r 
# a = np.array(list("python"))

# cv  = r.choice(a)
# print(cv,type(cv))  #y <class 'numpy.str_'>


# cv  = r.choice(a)
# print(cv,type(cv))   # o <class 'numpy.str_'>

#^---------------------------------------------------------------------------------------
# import numpy as np
# from numpy import random as r
# a = np.array(list("1234567890abcdfeghijklmnopqrstuvwxyzABCDFEGHIJKLMNOPQRSTUVWXYZ"))

# cv = r.choice(a)
# print(cv,type(cv))  #j <class 'numpy.str_'>

# cv = r.choice(a)
# print(cv,type(cv))  #D <class 'numpy.str_'>

# cv = r.choice(a)
# print(cv,type(cv))  #0 <class 'numpy.str_'>
#^---------------------------------------------------------------------------------------
# import numpy as np
# from numpy import random as r
# a = np.array(list("1234567890abcdfeghijklmnopqrstuvwxyzABCDFEGHIJKLMNOPQRSTUVWXYZ"))

# cv = r.choice(a,size=4)
# print(cv,type(cv))  

# cp = " "
# for ch in cv:
#      cp = cp+ch
# print("Captcha code : ",cp)
#*or 
# lst = []
# for ch in cv:
#      lst.append(ch)
# print("Captcha code : ","".join(lst))
#^---------------------------------------------------------------------------------------
# import numpy as np
# from numpy import random as r
# a=np.array([10,20,30,40,50,60,60,70,12,15,25,35,56,78,23,89,56])
# cv=r.choice(a,size=(2,2))
# print(cv,type(cv))

# import numpy as np
# from numpy import random as r
# a=np.array([10,20,30,40,50,60,60,70,12,15,25,35,56,78,23,89,56])
# cv=r.choice(a,size=(3,3))
# print(cv,type(cv))

# import numpy as np
# from numpy import random as r
# a=np.array([10,20,30,40,50,60,60,70,12,15,25,35,56,78,23,89,56])
# cv=r.choice(a,size=(2,3,3))
# print(cv,type(cv))

#^---------------------------------------------------------------------------------------
#* I want 2x2  Random Matrix between the values 10 to 99 
# from numpy import random as r
# a=r.randint(10,100,size=50)
# cv=r.choice(a,size=(2,2))
# print("2x2  Random Matrix")
# print(cv,type(cv))

# from numpy import random as r
# a=r.randint(10,100,size=50)
# cv=r.choice(a,size=(2,2,3))
# print("2x2  Random Matrix")
# print(cv,type(cv))

# from numpy import random as r
# a=r.randint(10,100,size=50)
# cv=r.choice(a,size=(2,2,2,2))
# print("2x2  Random Matrix")
# print(cv,type(cv))
#^---------------------------------------------------------------------------------------
# import numpy as np
# import numpy.random as r
# sc = np.array(["MH","TG","MP","UP","AP"])
# cc = np.array(["12","34","65","76","23"])
# cn = np.array(["AG","FG","XC","TD"])
# a = r.choice(sc)
# b= r.choice(cc)
# c = "".join(r.choice(cn,size=2))

# print(a+b+c)

# import numpy as np
# from numpy import random as r
# sa = np.array(["MH","AP","TG","MP","UP","UK"])
# tc = np.array(["08","09","10","07","30","15"])
# alpha = np.array(list("ABCDFEGHIJKLMNOPQRSTUVWXYZ"))
# nums = np.array(list("1234567890"))

# csa = r.choice(sa)
# ctc = r.choice(tc)
# calpha= "".join(r.choice(alpha,size = 2))
# cnums = "".join(r.choice(nums,size=4))

# nop = csa+ctc+calpha+cnums
# print(nop)


# import numpy as np
# from numpy import random as r
# sa = np.array(["MH","AP","TG","MP","UP","UK"])
# tc = np.array(["08","09","10","07","30","15"])
# alpha = np.array(list("ABCDFEGHIJKLMNOPQRSTUVWXYZ"))
# nums = np.array(list("1234567890"))

# csa = r.choice(sa)
