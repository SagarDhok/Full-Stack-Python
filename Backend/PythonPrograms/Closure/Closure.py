
#^-----------------------------------------------------------------------------------------------
#! ClsEx1.py
# def greet():
#      sname = "Rossum"
#      inner_fun = lambda : "Hi "+sname
#      return inner_fun

# xyz = greet()
# print(type(xyz))
# # print(xyz())
# res = xyz()
# print(res)
#^-----------------------------------------------------------------------------------------------
#! ClsEx2.py
# def calculate():
#      num = 1
#      def inner_func():
#           nonlocal num
#           num = num+1
#           return num
#      return inner_func

# inner = calculate()
# print(inner())
# print(inner())
# print(inner())

# # res = inner()
# # print(res)
# # res = inner()
# # print(res)
# # res = inner()
# # print(res)
# print("--------------")
# inner1 = calculate()
# print(inner1())
# print(inner1())
# print(inner1())