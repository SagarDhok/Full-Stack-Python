# lst1 = ["sagar","jay","karan","maroti"]
# print(lst1,id(lst1))
# lst2 =[1,2,3,6,4,5]
# print(lst2,id(lst2))
# lst1.extend(lst2)
# print(lst1,id(lst1))
# lst2.extend(lst1)
# print(lst2,id(lst2))

# ======================================
# NONE
# lst1 = ["sagar","jay","karan","maroti"]
# lst2 =[1,2,3,6,4,5]
# print(lst1,id(lst1))
# print(lst2,id(lst2))
# lst1.extend(lst2)
# print(x)



# lst1=["sagar","pythhon"]
# print(lst1,id(lst1))
# lst2=[2,3]
# lst3=[2+3j,33+4j]
# lst1.extend(lst2)
# lst1.extend(lst3)
# print(lst1,id(lst1))


# lst1=["sagar","pythhon"]
# lst2=[2,3]
# print(lst2,id(lst2))
# lst3=[2+3j,33+4j]
# lst2.extend(lst1)
# lst2.extend(lst3)
# print(lst2,id(lst2))


# lst1=["sagar","pythhon"]
# lst2=[2,3]
# lst3=[2+3j,33+4j]
# print(lst3,id(lst3))
# lst3.extend(lst1)
# lst3.extend(lst2)
# print(lst3,id(lst3))




# lst1=["sagar","pythhon"]
# print(lst1,id(lst1))
# lst2=[2,3]
# lst3=[2+3j,33+4j]
#                                            #lst1 is created in diiferent address
# lst1=lst1+lst2+lst3
# print(lst1,id(lst1))



# lst1=["sagar","pythhon"]
# lst2=[2,3]
# print(lst2,id(lst1))
# lst3=[2+3j,33+4j]
#                                          #lst1 is created in diiferent address
# lst2=lst1+lst2+lst3
# print(lst2,id(lst2))


lst1=[10,20,30]
print(lst1,id(lst1))
lst2=["RS","TR","DR"]
lst3=[1.2,2.3,4.5,4.5]
print(lst1,id(lst1))
lst1=lst1+lst2+lst3
print(lst1,id(lst1))