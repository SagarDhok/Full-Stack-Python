# a = [0,1,2,3]
# for a[-1] in a:
#  print(a[-1])

# a,b= "25"   
# b,c = "18"
# print(a+b+c)

# a = [1,2,3,4,5]
# for i in a :
#      a.remove(i)
# print(a)

# t = (5,10,15)
# # print(type(t))
# x,_,y = t
# print(x,y)
# print(x,_,y)

# x,y = 0
# print(x)
# print(y)      
# TypeError: cannot unpack non-iterable int object


# a = 1_2
# b = a*2
# print(b)  #24

# x,y = 7,4
# z = (x--x)+(y--y)
# print(z)   

# a = 2
# b = 3
# print(a**b*a**b)

# print(pow(2,3,5))

# 2**3%5

# print(pow(2,3,5,4))   #error

# n = 6
# while n>0:
#      print(n)
#      n=n-2  if n%3 == 0 else n-1



# name = "python" 
# if name == "java" or name == "html" or name == "css":
#     print("Login Successfully")
# else: 
#     print("not valid")


from pathlib import Path
# print("current file",__file__)  #current file e:\FULL STACK PYTHON\DjangoPrograms\Rough.py

# fpath = Path(__file__)
# print(type(fpath))  #<class 'pathlib.WindowsPath'>
# print("current file",fpath)  #current file e:\FULL STACK PYTHON\DjangoPrograms\Rough.py

# complete_path = fpath.resolve()
# print("Complete path",complete_path)#Complete path E:\FULL STACK PYTHON\DjangoPrograms\Rough.py

# print("Complete path",Path(__file__).resolve())# Complete path E:\FULL STACK PYTHON\DjangoPrograms\Rough.py

# print(Path(__file__).resolve().parent) #E:\FULL STACK PYTHON\DjangoPrograms
# print(Path(__file__).resolve().parent.parent) #E:\FULL STACK PYTHON




