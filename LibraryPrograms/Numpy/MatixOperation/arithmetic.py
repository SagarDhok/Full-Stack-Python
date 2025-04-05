
#*#Matrix Operations OR Arithmetic Operations on ndarray objects
#^---------------------------------------------------------------------------------------
#! add()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix a")
# print(a)
# print("-"*20)
# print("Matrix b")
# print(b)
# print("-"*20)
# c = np.add(a,b)  #* c = np.add(b,a)
#*Add the Matrices A and B
# print("Addition Matrix")
# print(c)



# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix a")
# print(a)
# print("-"*20)
# print("Matrix b")
# print(b)
# print("-"*20)
#* Add the Matrices A and B with arithmetic Operator
# c = b+a  #*c = a+b
# print("Addition Matrix")
# print(c)
#^---------------------------------------------------------------------------------------
#! Subtract()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#* Substraction of the Matrices A and B
# c = np.subtract(a,b)  #* # c = np.subtract(b,a)
# print("Substraction - Matrix -c")
# print(c)


# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#*Substraction of the Matrices A and B with Minus--->  -
# c = b-a  #*c = a-b
# print("Substraction - Matrix -c")
# print(c)

#^---------------------------------------------------------------------------------------
#! multiply()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #* Elementwise Multiplication of the Matrices A and B 
# c = np.multiply(a,b)  #* # c = np.multiply(b,a)
# print("(Elementwise Multiplication) - Matrix -c")
# print(c)




# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#* Elementwise Multiplication of the Matrices A and B  with Arithmetic Operator *
# c = b*a  #*c = a*b
# print("(Elementwise Multiplication) - Matrix -c")
# print(c)



#!dot()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #*Find Actual Matrix Multiplication
# print("Matrix-C(Actual Matrix Multiplication)")
# c = np.dot(a,b)
# print(c)

#* 10*1+20*3   10*2+20*4
# *30*1+40*3   30*2+40*4

# 70  100
# 150 220


#! matmul()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #*Find Actual Matrix Multiplication
# print("Matrix-C(Actual Matrix Multiplication)")
# c = np.matmul(b,a)
# print(c)
#^---------------------------------------------------------------------------------------
#! divide()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #*Find Elementwise Division 
# c = np.divide(a,b)  #* # c = np.divide(b,a)
# print("(Elementwise division) - Matrix -c")
# print(c)



# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#* Find Elementwise Division by using  Arithmetic Op -->  /
# c = b/a  #*c = a/b
# print("(Elementwise division) - Matrix -c")
# print(c)

#^---------------------------------------------------------------------------------------
#! floor_divide()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #*Find Elementwise Division --Integer Quotient
# c = np.floor_divide(a,b)  #* # c = np.floor_divide(b,a)
# print("(Elementwise floor_division) - Matrix -c")
# print(c)



# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.5array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#*Find Elementwise Division with Arithmetic Operator //--Integer Quotient 
# c = b//a  #*c = a//b
# print("(Elementwise floor_division) - Matrix -c")
# print(c)
#^---------------------------------------------------------------------------------------
#! mod()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#*Find Elementwise Modulo Division --Remainder
# c = np.mod(a,b)  #* # c = np.mod(b,a)
# print("(modulo division) - Matrix -c")
# print(c)



# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
#*Find Elementwise Modulo Division with Arithmetic Operator %--Remainder
# c = b%a  #*c = a%b
# print("(modulo division) - Matrix -c")
# print(c)

#^---------------------------------------------------------------------------------------
#! power()
# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #*#Find Elementwise Exponentiation--Power-off Operator
# c = np.power(a,b)  # c = np.power(b,a)
# print("(Elementwise Exponentiation) - Matrix -c")
# print(c)



# import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# b = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix- a")
# print(a)
# print("-"*20)
# print("Matrix -b")
# print(b)
# print("-"*20)
# #*Find Elementwise Exponentiation-- with Arithmetic Operator ** ---Power-off Operator
# c = a**b  #*c = a**b
# print("(Elementwise Exponentiation) - Matrix -c")
# print(c)

#^---------------------------------------------------------------------------------------