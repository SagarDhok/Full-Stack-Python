

#!solve the following Linear Equations by using solve()
#! solve()
#*Syntax : varname = np.linalg.solve(ndarrobj1,ndarrayobj2)
#*2x+3y=4
#*6x+y=2   Find x and y Values
#^=======================================================================================
# import numpy as np
# a= np.array([[2,3],[6,1]]) #* OR a=np.array([2,3,6,1]).reshape(2,2)
# b = np.array([4,2])
# sol = np.linalg.solve(a,b)
# print(sol)
# print("Sol Set")
# print(f"x ={round(sol[0],2)}")
# print(f"y ={round(sol[1],2)}")

#^---------------------------------------------------------------------------------------
#*solve the following Linear Equations by using solve()
#*8x-3y=-3
#*5x-2y=-1   Find x and y Values
# import numpy as np
# a = np.array([8,-3,5,-2]).reshape(2,2)
# b = np.array([-3,-1])
# sol = np.linalg.solve(a,b)
# print(sol)
# print("Sol Set")
# print(f"x ={round(sol[0],2)}")
# print(f"y ={round(sol[1],2)}")
#^=======================================================================================
#*solve the following Linear Equations with 3 un-Known Var by using solve()
#* x-y+z=2
#* 2x-y-z=-6
#* 2x+2y+z=-3   find  x,y and z values
# import numpy as np
# a = np.array([1,-1,1,2,-1,-1,2,2,2]).reshape(3,3)
# b = np.array([2,-6,-3])
# sol = np.linalg.solve(a,b)
# print(sol)
# print("Sol Set")
# print(f"x ={round(sol[0],2)}")
# print(f"y ={round(sol[1],2)}")
# print(f"z ={round(sol[2],2)}")
