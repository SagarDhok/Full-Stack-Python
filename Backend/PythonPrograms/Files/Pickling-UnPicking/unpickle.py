
#*SYNTAX - 1
# import pickle
# try:
#  with open("Ex1.pick","rb") as fp:
#    obj = pickle.load(fp)         
#    print(type(obj))  - <class list>
#    print(obj)
#    obj = pickle.load(fp)
#    print(obj)
#    obj = pickle.load(fp)
#    print(obj)
#    obj = pickle.load(fp)
#    print(obj)
# except EOFError:
#  print("limit is exceed")

# except FileNotFoundError:
#  print("File does not exist ")
#^--------------------------------------------------------------------------------------------
#*SYNTAX - 2
# import pickle
# try:
#  with open("Ex1.pick","rb") as fp:
#    while True:
#     try:
#      obj = pickle.load(fp)
#      print(obj)  
#     except EOFError:
#      break
# except FileNotFoundError:
#  print("File does not exist ")
#^--------------------------------------------------------------------------------------------
#*SYNTAX - 3
# import pickle
# try:
#  with open("Ex1.pick","rb") as fp:
#    while True:
#     try:
#      obj = pickle.load(fp)
#      for val in obj:
#           print(val,end="\t")
#      print()
#     except EOFError:
#       break
    
# except FileNotFoundError:
#  print("File does not exist ")
#^--------------------------------------------------------------------------------------------