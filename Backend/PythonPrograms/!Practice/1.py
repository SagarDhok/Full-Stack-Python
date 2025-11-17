# What is the difference between list.append() and list.extend()?

# list = ["sagar",2+3j,2.44,90]
# list.append([2,3,4])
# print(list)

# list1 = ["sagar",2+3j,2.44,90]
# list2 = ["sagar",2+3j,2.44,90]
# list2.extend(list1)
# print(list1,id(list1))
# print(list2,id(list2))


# list1 = ["sagar",2+3j,2.44,90]
# list2 = ["sagar",2+3j,2.44,90]
# list3 = ["sagar",2+3j,2.44,90]
# list3.extend(list1)
# list3.extend(list2)
# print(list1,id(list1))
# print(list2,id(list2))
# print(list3,id(list3))

# list1 = [0,1,2,3,4]
# list2 = [5,6,7,8,9]
# list3 = [10,11,12,13,14]

# list3= list3+list1+list2
# print(list1,id(list1))
# print(list2,id(list2))
# print(list3,id(list3))


# How can you sort a list in Python?
# list3 = [348,4,2980,0,49949,9]
# list3.sort()
# list3.sort(reverse=False)
# print(list3)

# list3.sort(reverse=True)
# print(list3)

# How do you create a tuple with only one element?
# t = ([2],)
# print(t,type(t))


# How can you concatenate two tuples?
# t = (1,2,3,4)
# t1 = (5,6,7,8)
# t2 = t +t1
# print(t,type(t),id(t))
# print(t1,type(t1),id(t1))
# print(t2,type(t2),id(t2))

# How can you unpack a tuple into individual variables?
# t = (10,20,30,40,50,60)
# a,b,c,*rest=t
# print(a,b,c)
# print(*rest)


# print(2**6)
# print(2**4)

# lst=[10,20,30]
# print(lst,id(lst))
# lst=[10,20,30]
# print(lst,id(lst))

# lst1=[10,20,30]
# lst2=lst1 
# print(lst2 is lst1)

# a = 10
# b=10
# id(a)
# id(b)
# print(a is b)
# print(a is not b)

# list = [12,12]
# print(list)


# a= 0
# print(a,type(a))

# a= "10383"
# print(a[0])

# s = 'python'
# print(s[:2])
# print(s[:3])

# list = [10,"rs",23.5]
# list.insert(2,"python")
# print(list)


# list = ["sagar",1,3,1,5,"sagar"]
# print(list.index("sagar"))
# print(list.index(1))
# print(list.index("sagar"))


# list = [10,"rs",23.5]
# list1 = list.reverse()
# print(list) 
# print(list1) 
# or
# list = [10,"rs",23.5]
# list.reverse()
# print(list) 

# t = 39,49,47,40
# x = sorted(t)
# print(x,type(x))
# t1 = tuple(x)
# print(t1,type(t1))


# t = 39,49,47,40
# x = tuple(sorted(t))[::-1]
# print(x,type(x))

# t = (48,30,27,["a","e","i"],41,7)
# del t[3] [1:3]
# print(t) 

# s = 100
# s = set((s,))
# print(s,type(s))




# s = {10,20,30,4,59}
# print(s,type(s),id(s))
# s.pop()
# s.pop()
# s.pop()
# print(s,type(s),id(s))



# s = {10,20,30,4,59}
# s.pop()
# s.pop()
# s.pop()
# print(s,type(s),id(s))

# s= 100
# print(s,id(s))
# s= s+100
# print(s,id(s))

# s  = "sagar"
# print(s,id(s))
# x= s.upper()
# print(x,id(x))


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print( set1.union(set2))
# set3 = set1.union(set2)
# print(set3,type(set3))

# set3 = set1.update(set2)
# print(set1,type(set1))
# print(set3,type(set3))

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2))
# set3 = set1.intersection(set2)
# print(set3,type(set3))


# small_set = {1, 2, 3}
# large_set = {1, 2, 3, 4, 5}
# # x = small_set.issubset(large_set)
# # print(x,type(x))
# # print(small_set.issubset(large_set))

# y = large_set.issubset(small_set)
# print(y,type(y))
# print(large_set.issubset(small_set))

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.symmetric_difference(set2)
# print(set3,type(set3))
# print(set1.symmetric_difference(set2))


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = {5, 6, 7, 8, 9}
# print(set1.intersection(set2,set3))
# print(set2.intersection(set1,set3))
# print(set2.intersection(set1,set3))

# A = {2, 4, 6, 8, 10, 12}
# B = {1, 2, 3, 4, 5, 6}
# C = {6, 7, 8, 9, 10}
# print(A.symmetric_difference(B))
# print(B.symmetric_difference(C))

# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 10]
# set = set(numbers)
# print(set)

# dept_A = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
# dept_B = {'Eve', 'Frank', 'George', 'Hannah', 'Ivy'}
# dept_AB = dept_A.intersection(dept_B)
# print("{} works in both department".format(dept_AB))

# dept_One = dept_A.symmetric_difference(dept_B)
# print("{} work in only one of the two departments".format(dept_One))



# math_students = {1001, 1002, 1003, 1004, 1005}
# science_students = {1003, 1005, 1006, 1007}
# english_students = {1002, 1004, 1008, 1009}
# EAC = math_students & science_students & english_students
# print(EAC)


# math_students = {1001, 1002, 1003, 1004, 1005}
# science_students = {1003, 1005, 1006, 1007}
# english_students = {1002, 1004, 1008, 1009}
# x = math_students.intersection(science_students & english_students)
# print(x)


# store_A = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
# store_B = {'fig', 'grape', 'honeydew', 'cherry', 'banana'}
# store_AB = store_A.intersection(store_B)
# print(store_AB)

# x = store_A.difference(store_B)
# print(x)

# y = store_B.difference(store_A)
# print(y)


# set1 = {x for x in range(1, 21) if x % 2 == 0}
# set2 = {x for x in range(1, 21) if x % 3 == 0}
# print(set1)
# print(set2)

# set3 = set1.union(set2)
# print(set3)

# set4 = set1.difference(set2)
# print(set4)

# s1 = {10,30,40}
# s2 = {20,10,50}
# s3 = s1.union(s2)
# print(s3)
# print(s1)



# s1 = {10,30,40}
# s2 = {20,10,50}
# s3 = s1.union(s2)
# print(s3)
# print(s1|s2)

# s1 = {10,30,40}
# s2 = {20,10,50}
# s3 = s1.update(s2)
# print(s3)
# print(s1)

# s = { 47,29, 39, (1, 'apple', 3.5) ,"rossum" }
# print(s,type(s))
# for val in s:
#      print(val, type(val),type(s))


# list = [1,2,3]
# tuple = (4,5,6)
# list.extend(tuple)
# print(list)

# list = [1,35,57,8]
# print(list,id(list))
# set = {"fsk",49,60}
# list.extend(set)
# print(list,id(list))



# l1 = [1,3,4,5] 
# l2 = [54,43,90,44]          +
# l3 = l1+l2
# print(l3)

# l1 = frozenset({1,3,4,5}) 
# l2 = frozenset({54,43,90,44,5})         - and | & ^
# l3 = l1^l2
# print(l3)

# d1= {1:2}
# d2= {2:4}            #|
# print(d1|d2)





