
#^ --------------------------------------------------------------------------------------------
#! Write a Python program that declares a global variable and modifies its value inside a function. Explain why you need to use the global keyword.
# a = 10
# b = 20

# def calc():
#     global a
#     a = a+20
#     print("funtion body",a)

# print("og a ",a)
# calc()
# print("modified a ",a)

#^ --------------------------------------------------------------------------------------------
# a = 10
# b= 20
# def func ():
#      print("GLOBAL VARIBLE")
#      # if we didnt define global keyword then it will give localunbound error 
#      global a ,b
#      a= a+40
#      b = b+30
#      print("a = ",a)
#      print("b = ",b)

#      print("LOCAL VARIBLES ")
#      c ,d = 30,40
#      c = c+20
#      d = d+10
#      print("c = ",c)
#      print("d = ",d)
#      #Local variables cannot define outside of function

# print("original val of a = ",a)
# print("original val of b = ",b)
# func()
# print("updated val of a = ",a)
# print("updated val of b = ",b)
#^ --------------------------------------------------------------------------------------------
# a = 10
# b = 20

# def fun():
#      a = 1
#      b = 2

     # x = globals()
     # for k,v in globals().items():
     #   print(k,"-->",v)
     
     # res = a+b+x["a"]+x["b"]
     # res = a+b+x.get("a")+x.get("b")
     # res = a+b+globals().get("a")+globals().get("b")
     # res = a+b+globals()["a"]+globals()["b"]
     # print(res)
# fun()
#^ --------------------------------------------------------------------------------------------













