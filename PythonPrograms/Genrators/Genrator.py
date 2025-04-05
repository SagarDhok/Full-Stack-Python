

#^-----------------------------------------------------------------------------------------------
#* LOGIC - 1 :
# def kvrrange(val):
#   s = 0
#   while s<=val:
#     yield s   
#     s = s+1


# r = kvrrange(6)
# print(r,type(r))  #<generator object kvrrange at 0x000001D849E120C0> <class 'generator'>
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))


#* LOGIC - 2 :
# def kvrrange(val):
#   s = 0
#   while s<=val:
#     yield s   
#     s = s+1


# r = kvrrange(100)
# #print(r,type(r))  #<generator object kvrrange at 0x000001D849E120C0> <class 'generator'>
# while True:
#      try:
#       print(next(r))
#      except StopIteration:
#           break 


# def frange(x):
#      s = 0
#      while s<x:
#           yield s
#           s = s+1

#* LOGIC - 3 :
# r= frange(6)
# print(next(r))
# print(next(r))
# print("----------------------------")
# for val in r:
#      print(val)
# print("----------------------------")
# r1= frange(10)
# for v in r1:
#      print(v)
#^-----------------------------------------------------------------------------------------------
#* LOGIC - 1 :
# import sys
# def getcourse():
#   yield "PYTHON"
#   yield "JAVA"
#   yield "DSA"
#   yield "20"

# r = getcourse()
# try:
#  print(next(r))
#  print(next(r))
#  print(next(r))
#  print(next(r))
#  print(next(r))
# except StopIteration:
#      sys.exit()

#* LOGIC - 2 :
# def getcourse():
#   yield "PYTHON","java"
#   yield "JAVA"
#   yield "DSA"
#   yield "20"

# r = getcourse()
# while True:
#  try:
#   print(next(r))
#  except StopIteration:
#       break


#* LOGIC - 3 :
# def getcourse():
#   yield "PYTHON","java"
#   yield "JAVA"
#   yield "DSA"
#   yield "30",30

# r = getcourse()
# for val in r:
#      print(val)
#^-----------------------------------------------------------------------------------------------
# def kvrrange(start,stop=0,step = 1):
#      if start > stop:
#       stop = start
#       start = 0
#      while start<=stop:
#       yield start
#       start = start + step
     


# r = kvrrange(10,100,10)
# for val in r:
#  print(val)

# print("----------------")

# r1 = kvrrange(100,106)
# for val in r1:
#     print(val)

# print("----------------")
# r2 = kvrrange(5)
# for val in r2:
#    print(val)
#^-----------------------------------------------------------------------------------------------
