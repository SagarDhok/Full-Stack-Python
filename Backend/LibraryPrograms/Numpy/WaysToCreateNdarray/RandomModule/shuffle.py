


#! 7.shuffle()
#* Syntax:  numpy.random.shuffle(ndarrayobject)
#* a la update karte 
#^---------------------------------------------------------------------------------------
# import numpy as np
# from numpy import random as r
# a= np.arange(10)
# print("Original content of ndarray")
# print(a,id(a))
# print("Shuffled content of ndarray ")
# r.shuffle(a)
# print(a,id(a))


#^---------------------------------------------------------------------------------------
#*what are various shuffled Values of ndarray
# import numpy as np
# from numpy import random as r
# a= np.arange(10)
# print("Original content of ndarray")
# print(a)
# for i in range(1,len(a)+1):
#      r.shuffle(a)
#      print(f"Combination : {i} -> {a}   ")
#^---------------------------------------------------------------------------------------
#*Show the Number of Re-arragment Values of "MISSISSIPPI"
# import numpy as np
# from numpy import random as r
# a = np.array(list("MISSISSIPPI"))
# print("Original Content of a ")
# print(a)

# for i in range(1,len(a)+1):
#      r.shuffle(a)
#      print(f"Combination : {i} -> {a}")

#^---------------------------------------------------------------------------------------
#*Shuffling 2-D Data--shuffles--Rows
# import numpy as np
# from numpy import random as r
# a = r.randint(1,100,size=(3,2))
# print("Orgininal Matrix")
# print(a)
# print("Reshuffled Matrix")
# r.shuffle(a)
# print(a)
#^---------------------------------------------------------------------------------------
#*Shuffling n-D Data--shuffles--Matrix Numbers
# from numpy import random as r
# a = r.randint(1,100,size=(4,3,2))
# print("Original Matrix")
# print(a)
# print("Reshuffled Matrix")
# r.shuffle(a)
# print(a)
#^---------------------------------------------------------------------------------------
#* Shuffling n-D Data--shuffles--Matrix Numbers
# import numpy as np
# from numpy import random as r
# a=np.arange(24).reshape(3,2,2,2)
# print("Original Matrix")
# print(a)
# print("Reshuffled Matrix")
# r.shuffle(a)
# print(a)

#^---------------------------------------------------------------------------------------
# import numpy as np
# from numpy import random as r
# a=np.array([10,20,30,40,50,60,70])
# print("Original array before permutation")
# print(a)
# print("-------------------------------")
# b=r.shuffle(a)
# print("Val of b=",b)
# print("-------------------------------")
# print("Original array after Shuffle")
# print(a)
