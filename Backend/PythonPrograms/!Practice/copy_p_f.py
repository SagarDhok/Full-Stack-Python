# 1.shallow copy

# lst1 = [0,1,2,3]
# lst2= lst1.copy()
# lst1.append("sagar")
# lst2.append("python")
# lst1.remove(2)
# lst2.remove(0)
# print(lst1,type(lst1),id(lst1))
# print(lst2,type(lst2),id(lst2))


# 2.deep copy

# lst1 = [0,1,2,3]
# lst2=lst1[0:2]
# lst2.append("sagar")
 # lst2.remove(1)
# print(lst1,type(lst1),id(lst1))
# print(lst2,type(lst2),id(lst2))


# 3.sliced based copy

# lst1 = [0,1,2,3,4,5,6]
# lst2 = lst1[::2]
# print(lst1,id(lst1))
# print(lst2,id(lst2))

# lst1 = [0,1,2,3,4,5,6]
# lst2 = lst1[::3]
# print(lst1,id(lst1))
# print(lst2,id(lst2))

# lst1 = [0,1,2,3,4,5,6]
# lst2 = lst1[::]
# print(lst1,id(lst1))
# print(lst2,id(lst2))

