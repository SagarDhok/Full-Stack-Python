# s = {10,"sagar","100",4}
# print(s,id(s))

# s.add(90)
# print(s,id(s))
# s.remove(88)
# print(s,id(s))

# s.discard("sagar")
# print(s,id(s))

# s.discard(88)
# print(s,id(s))
# s.remove(88)
# print(s,id(s))





# s.clear()
# print(s,id(s))
# s = set().clear()
# print(s,id(s))



# print("_____Not Given insertion order_______")
# s = {"sagar",22,5.6,2+3j,True}
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

# print("_____insertion order_______")
# s1 = {10,"sagar",2+3j,True,22.5}
# print(s1,id(s1))
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())

# s1 = {10,"sagar",2+3j,True,22.5}
# # del s1[0:1]
# # print(s1,type(s1))
# del s1
# print(s1,type(s1))


# s1={10,27,47,57}
# s2={28,48,45,2}
# s3={27,10,49,9}

# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s3))
# print(s2.isdisjoint(s3))

# print(set().isdisjoint(set()))


# s1={10,27,47,57}
# s2 = s1.copy()

# print(s1,id(s1))
# print(s2,id(s2))

# s1.add(1000)
# s2.pop()
# print(s1,id(s1))
# print(s2,id(s2))

# s1={10,27,47,57}
# s2=s1
# print(s1,id(s1))
# print(s2,id(s2))

# s1 = {38,59,69,6}
# s2 = {6,38}
# s3= {89,9,34,66}
# s4={38,59,69,00}

# print(s1.issuperset(s2))
# print(s1.issuperset(s3))
# print(s2.issuperset(s3))
# print(s1.issuperset(s4))

# print({10,20,30}.intersection({10,15,25},{10,15,45,55}))

# print({10,20,30}.symmetric_difference(set()))


# s1={10,20,30}
# s2={10,20,30}
# s3=s1.update(s2)
# print(s1,type(s1))
# print(s3,type(s3))

# s1={10,20,30}
# s2={10,25,35}
# s3=s2.difference_update(s1)
# print(s2)
# print(s3)



# s1={10,20,30}
# s2={10,25,35}
# s2.difference_update(s1)
# print(s2)


# s1={10,20,30}
# s2={10,25,35}
# s3=s2.symmetric_difference(s1)
# print(s3)


# s1={10,20,30}
# s2={10,25,35}
# s3 = s1.union(s2)
# print(s3)

# s1={10,20,30}
# s2={10,20,30}
# s3 = s1.symmetric_difference(s2)
# print(s3)


# TypeError: unhashable type: 'set'
# s = {1,2,3,4,{47,595,50},"sa"}
# print(s)
# TypeError: unhashable type: 'list'subscriptable
# s = {0,4,4,4,[3,4,5],59,58}
# print(s,type(s))


 
# s = {0,4,4,4,(3,4,5),59,58}
# print(s,type(s))


