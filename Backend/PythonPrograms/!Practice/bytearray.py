# lst = [34,5,7,0]
# # print(lst,type(lst))
# ba = bytearray(lst)
# print(ba,type(ba))
# for v in ba:
#      print(v)

# print(ba[-2])
# print(ba[-4:-2])

# print("_______________")
# for v in ba[-4:-2]:
#      print(v)
# print("_______________")
# for v in ba[1000:-1000:-1]:
#      print(v)

     


# ba[-1]=200

# print(ba[-1])
# print("_______________")
# for v in ba:
#      print(v)


list = [10,20,30,20,50]
ba = bytearray(list)
print(ba,type(ba),id(ba))


ba[0]=100

for v in ba:
     print(v)
print(ba,type(ba),id(ba))