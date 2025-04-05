
#^========================================================================================
#!Program for Demonstrating the need of Iterators
#!IterEx1.py

lst = [10,20,30,40,50,60,"Rossum","Python"]
print("Content of the list : ",lst)
print("Type Of the list : ",type(lst))
#* To Convert Iterable object into Iterator Object, we use iter()
itrobj = iter(lst)

# print("Content of the itrobj : ",itrobj)   #* <list_iterator object at 0x0000019D15D5AE00>
# print("Type Of the itrobj : ",type(itrobj))  #* <class 'list_iterator'>

# print(next(itrobj))
# print(next(itrobj))
# print(next(itrobj))

# print("Content of List Iterator by using while")
# while True:
#    try:
#      print(next(itrobj))
#    except StopIteration:
#       break



# lst = [10,20,30,40,50,60,"Rossum","Python"]
# itrobj = iter(lst)
# for val in itrobj:
#      print(val)
#^========================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx2.py
# t = (10,20,30,40,50,60,"Rossum","Python")
# print("Content Of the tuple : ",t)
# print("Type of the tuple : ",type(t) )
# #To Convert Iterable object into Iterator Object, we use iter()
# itrobj = iter(t)
# print("Content of itrobj : ",itrobj)  #*<tuple_iterator object at 0x00000203F875AE00>
# print("Type of itrobj : ",type(itrobj)) #*<class 'tuple_iterator'>
# print("Content of the iterobj using while loop")
# while True:
#      try:
#           print(next(itrobj))
#      except StopIteration:
#           break
#^========================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx3.py

# s1={10,20,30,40,50,60,"Rossum","Python"}
# print("Content of the set : ",s1)
# print("Type of the set : ",type(s1))

# itrobj= iter(s1)
# print("Content of itrobj : ",itrobj)   #*<set_iterator object at 0x0000026277CA65C0>
# print("Type of itrobj : ",type(itrobj))   #*<class 'set_iterator'>

# print("Content of the itrobj using for loop ")
# for val in itrobj:
#      print(val)

#^========================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx4.py
# fs1=frozenset({10,20,30,40,50,60,"Rossum","Python"})
# print("Content of fs1 : ",fs1)
# print("Type of fs1 : ",type(fs1))

# itrobj = iter(fs1)
# print("Content of itrobj : ",itrobj)
# print("Type of itrobj : ",type(itrobj))

# print("Content of the frozentset by using for loop ")
# for val in itrobj:
#      print(val)
#^========================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx5.py
# d1={1:"Python",2:"C",3:"C++",4:"Java",5:"DSA"}
# print("Content of the d1 : ",d1)
# print("Type of the d1 : ",type(d1))

# itrobj = iter(d1)
# print("Content of the itrobj : ",itrobj)
# print("Type of itrobj : ",type(itrobj))

# print(next(itrobj))
# print(next(itrobj))
# print(next(itrobj))

# k = next(itrobj)
# print(k,d1.get(k))
# k = next(itrobj)
# print(k,d1.get(k))


# for val in itrobj:
#      print(val,d1[val])

# while True:
#      try:
#           k = next(itrobj)
#           print(k,d1[k])
#      except StopIteration:
#           break
#^========================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx6.py
# s="PYTHON"
# print("Content of s : ",s)
# print("Type of s : ",type(s))

# itrobj = iter(s)
# print("Content of itrobj : ",itrobj)    #*<str_ascii_iterator object at 0x0000020C6CACAE00>
# print("Type of itrobj : ",type(itrobj))  #*<class 'str_ascii_iterator'>


# print("Content of itrobj by for loop")
# for val in itrobj:
#      print(val)
#^========================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx7.py
# r = range(10,21,2)
# print("Content of r : ",r)
# print("type of r : ",type(r))

# itrobj= iter(r)
# print("Content of itrobj : ",itrobj)   #* <range_iterator object at 0x000001B2588AAEF0>
# print("Type of itrobj : ",type(itrobj))    #*<class 'range_iterator'>

# print("Content of itrobj using for loop ")
# for val in itrobj:
#      print(val)
#^========================================================================================
#!Program for Demonstrating ---It is not possible to apply on Non-Iterable Objects like int,float, bool,complex and NoneType
#! IterEx8.py

# a = 0 
# print("COntern of a : ",a)     # * Here a object is called Non-Iterable Object
# print("Type of a : ",type(a))

# itrobj=iter(a) ----------------TypeError: 'int' object is not iterable
# print(itrobj)

#^========================================================================================



