
#^--------------------------------------------------------------------------------------------
# def funtionA(val):
#      print("This is Outer Funtion")
#      def funtionB():
#           print("This is Inner Funtion")
#           print(val)
#      funtionB()
# funtionA(10)
#^---------------------------------------------------------------------------------------------
# def outer_fun(x):
#      y = 10
#      def inner_fun(z):
#           return x+y+z
#      return inner_fun

# inner_fun=outer_fun(10)
# res = inner_fun(5)
# print(res)
#^---------------------------------------------------------------------------------------------
# def functionA(name):
#    def functionB():
#       print (name)
#    return functionB

# #Main Program
# myfunction = functionA("Allu Arjun")
# myfunction()
#^---------------------------------------------------------------------------------------------
#! NonLocal Keyword
#* modify karte immutable value inside of outer funtion means in the inner funtion
# def outer_fun():
#      val = 1
#      def inner_fun():
#           nonlocal val
#           val= val+1
#           return val
#      return inner_fun
# inner=outer_fun()
# print(inner())
# print(inner())
# print(inner())

