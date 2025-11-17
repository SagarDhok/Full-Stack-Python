

#* SYNTAX-1
# def getval():
#       return 5

# def square():
#     #   val = getval()
#       print(f"Square of {getval()}  is : {getval()**2}")
# def cube():
#       val = getval()
#       print(f"Cube of {val} is : {val**3}")

# print("Calling getval funtion ")
# getval()
# print("Calling square function")
# square()
# print("Calling cube function")
# cube()
#^----------------------------------------------------------------------------------------------
#* SYNTAX-2
# def getval (n):
#       return n 

# def square(n):
#      n = getval(n)
#      print(f"SQUARE OF GIVEN VALUE IS : {n*n}")
# def cube(n):
#       n = getval(n)
#       print(f"CUBE OF GIVEN VALUE IS : {n**3}")

# n = int(input("ENTER A VALUE : "))
# res = getval(n)
# square(res)
# cube(res)
#^----------------------------------------------------------------------------------------------
#* SYNTAX-3
# def getval (n):
#  return n 

# def square(n):
#      n = getval(n)
#      return n 
# def cube(n):
#       n = getval(n)
#       return n 

# n = int(input("ENTER A VALUE : "))
# res = getval(n)
# square(res)
# print(f"SQUARE OF GIVEN VALUE IS : {res*res}")
# cube(res)
# print(f"CUBE OF GIVEN VALUE IS : {res**3}")
#^----------------------------------------------------------------------------------------------

# def square(getval):
#     def operation():
#         n = getval()
#         square_res = n ** 2
#         return n, square_res
#     return operation

# def sqrt(getval):
#     def operation():
#         n, square_res = getval()  # Expecting two values from the previous function
#         sqrt_res = n ** 0.5
#         return n, square_res, sqrt_res
#     return operation

# def cube(getval):
#     def operation():
#         n, square_res, sqrt_res = getval()  # Expecting three values from the previous function
#         cube_res = n ** 3
#         return n, square_res, sqrt_res, cube_res
#     return operation

# @square
# @sqrt
# @cube
# def getval():
#     return int(input("ENTER A NUMERICAL VALUE : "))

# n, square, sqrt, cube = getval()
# print(f"Original Number: {n}")
# print(f"Square: {square}")
# print(f"Square Root: {sqrt}")
# print(f"Cube: {cube}")



# def square(getval):
#     def operation():
#         n = getval()
#         square_res = n ** 2
#         return n, square_res
#     return operation

# def sqrt(getval):
#     def operation():
#         n, square_res = getval()  # Unpack the values from the previous decorator
#         sqrt_res = n ** 0.5
#         return n, square_res, sqrt_res
#     return operation

# def cube(getval):
#     def operation():
#         n, square_res, sqrt_res = getval()  # Unpack the values from the previous decorator
#         cube_res = n ** 3
#         return n, square_res, sqrt_res, cube_res
#     return operation

# @cube
# @sqrt
# @square
# def getval():
#     return int(input("ENTER A NUMERICAL VALUE: "))

# n, square, sqrt, cube = getval()  # Correct unpacking
# print(f"Original Number: {n}")
# print(f"Square: {square}")
# print(f"Square Root: {sqrt}")
# print(f"Cube: {cube}")



# def box():
#      def new_display():
#       print("******************")
#       display()
#       print("******************")
#      return new_display
# @box
# def display():
#      return "Sagar Dhok"
# box()


    