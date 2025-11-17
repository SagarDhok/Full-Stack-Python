

#^ ---------------------------------------------------------------------------------------------
#! 1. Write a Python program to sum all the items in a list. 
# # lst = [1,3,5,48,27,4]

# #*LOGIC-1
# # # print(sum(lst))

# #*LOGIC-2
# # lst = lst[0]+lst[1]+lst[2]+lst[3]+lst[4]+lst[5]
# # print(lst)

# #*LOGIC-3
# # s = 0
# # for i in lst:
# #  s = s+i
# # print(s)

# #*LOGIC-4
# # i = 0
# # s = 0
# # while(i<len(lst)):
# #      s = s+lst[i]
# #      i = i+1
# # print(s)
#^ ---------------------------------------------------------------------------------------------
#! 2. Write a Python program to multiply all the items in a list.
#*LOGIC-1
# n = int(input("ENTER HOW MANY VALUES YOU TO ENTER "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = int(input(f"ENTER {i} VALUES : ")) 
#           lst.append(val)
#      print(lst)
#      mul = 1
#      for j in lst:
#           mul = mul*j
     
# print(f"MULTIPLICATION IS {mul}")

#*LOGIC-2
# n = int(input("ENTER HOW MANY VALUES YOU TO ENTER "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = int(input(f"ENTER {i} VALUES : ")) 
#           lst.append(val)
#      print(lst)
#      mul = 1
#      for j in range(0,len(lst)):
#              mul = mul*lst[j]
     
# print(f"MULTIPLICATION IS {mul}")

#*LOGIC-3
# n = int(input("ENTER HOW MANY VALUES YOU TO ENTER : "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN")
# else:
#      lst =[]
#      i = 1
#      while(i<=n):
#           val = int(input(f"ENTER {i} VALUE : "))
#           lst.append(val)
#           i = i+1
#      print(lst)
#      j = 0
#      mul = 1
#      while(j<len(lst)):
#           mul *=lst[j]
#           j+=1
#      print(f"MULTIPLICATION IS {mul}")
#^ ---------------------------------------------------------------------------------------------
#! 3. Write a Python program to get the largest number from a list.
#*LOGIC-1
# lst  = [33,84,48,34,38,35]
# print(max(lst))

#*LOGIC-2
# n = int(input("ENTER HOW MANY VALUES YOU TO ENTER :  "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = int(input(f"ENTER {i} VALUES : ")) 
#           lst.append(val)
#      max = lst[0]
#      for i in lst:
#           if i >= max: 
#             max = i
#      print(max)
#  
# #*LOGIC-3
# n = int(input("ENTER HOW MANY NUMBERS YOU WANT : "))
# if n <= 0:
#      print("INVALID INPUT! PLEASE ENTER AGAIN ")
# else:
#      lst = []
#      i= 1
#      while(i<=n):
#           val = int(input(f"enter {i} value : "))
#           lst.append(val)
#           i = i+1

#      i = 0
#      max = lst[0]
#      while(i<len(lst)):
#           if lst[i] >=max:
#              max = lst[i]
#           i = i+1
# print(max) 
     
#^ ---------------------------------------------------------------------------------------------
#! 4. Write a Python program to get the smallest number from a list.
#*LOGIC-1
# lst = [43,59,28,20,38,13,40,38,] 
# print(min(lst))

#*LOGIC-2
# n = int(input("ENTER HOW MANY VALUES YOU TO ENTER :  "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN")
# else:
#      lst = []
#      for i in range(1,n+1):
#           val = int(input(f"ENTER {i} VALUES : ")) 
#           lst.append(val)
#      min = lst[0]
#      for i in lst: 
#            if i<=min:
#              min = i
#      print(min)
      
#*LOGIC-3
# n = int(input("ENTER HOW MANY VALUES YOU TO ENTER :  "))
# if n<=0:
#      print("IT IS INVALID INPUT ! ENTER AGAIN")
# else:
#      lst = []
#      i = 1
#      while(i<=n):
#           val =int(input(f"ENTER {i} VALUES : ")) 
#           lst.append(val)     
#           i = i+1 
     
#      min = lst[0]
#      i = 0
#      while(i<len(lst)):
#           if lst[i] <= min:
#                min = lst[i]
#           i = i+1
# print(min)
#^ ---------------------------------------------------------------------------------------------
#! 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
#*	Sample List : ['abc', 'xyz', 'aba', '1221']
#*	Expected Result : 2

#*LOGIC-1
# lst = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for  i in lst:
#      if  len(i)>=2 and i[0]==i[-1]:
#       count = count+1

#       print(i)
# print("THE COUNT IS : ",count)

#*LOGIC-2
# lst = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for i in lst:
#      if len(i):
#       if i[-1] == i[0]:
#        count = count+1
#        print(i)
# print("count is : ",count)
           
#*LOGIC-3
# lst = ['abc', 'xyz', 'aba', '1221']
# for i in lst:
#      if i.startswith(i[0]) and i.endswith(i[0]):
#              print(i)

#*LOGIC-4
# lst = ['abc', 'xyz', 'aba', '1221']
# i = 0
# count = 0
# while i<len(lst):
#      if lst[i][0]==lst[i][-1] and len(lst[i])>=2:
#           count+=1
#           print(lst[i])
#      i = i+1
# print("count is : ",count)
#^ ---------------------------------------------------------------------------------------------
#! 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
#* 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# *	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#^ ---------------------------------------------------------------------------------------------
#! 7. Write a Python program to remove duplicates from a list. 
#*LOGIC-1
# lst = [1,1,2,2,3,3,4,4,5,5]
# lst = list(set(lst))
# print(lst)

#*LOGIC-2
# lst = [1,1,2,2,3,3,4,4,5,5]
# newlst= []
# for i in lst:
#      if i not in newlst:
#           newlst.append(i)
# print(newlst)

#*LOGIC-3
# lst = [1,1,2,2,3,3,4,4,5,5]
# lst = list(frozenset(lst))
# print(lst)

#^ ---------------------------------------------------------------------------------------------
#! 8. Write a Python program to check a list is empty or not. 
# lst = []
# if len(lst)==0:
#      print("it is empty list")
# else:
#      print("it is not a empty list")
#^ ---------------------------------------------------------------------------------------------
#! 9. Write a Python program to clone or copy a list.
#*LOGIC-1
# lst = [487,49,58,43,40]
# lst1 = []
# for i in lst:
#     lst1.append(i)
# print(lst1) 

#*LOGIC-2
# lst = [487,49,58,43,40]
# lst1=lst.copy()
# print(lst1)

#*LOGIC-3
# lst = [487,49,58,43,40]
# lst1= lst
# print(lst1)
#^ ---------------------------------------------------------------------------------------------
#! 10. Write a Python program to find the list of words that are longer than n from a given list of words. 

# list = ["sagar","jay","hanuman","karan","maroti"]
# n=int(input("enter number "))
# for i in list:
#      if len(i)==n:
#       print(i,len(i))
#^ ---------------------------------------------------------------------------------------------
#! 11. Write a Python function that takes two lists and returns True if they have at least one common member.
#*LOGIC-1
# def common(lst1,lst2):
#  res = "NO COMMON"
#  for i in lst1:
#       for j in lst2:
#               if i == j:
#                res ="COMMON"
#                break
#  if res == "COMMON":
#    print("it has common")
#  else:
#    print("it has no common")
# lst1 = [12,13,11,14,15]
# lst2 = [21,19,22,11,199,88]
# common(lst1,lst2)

#*LOGIC-2
# def common(lst1,lst2):
#  for i in lst1:
#       for j in lst2:
#               if i == j:
#                return True
#  return False
# lst1 = [12,13,11,14,15]
# lst2 = [21,19,22,11,199,88]
# res = common(lst1,lst2)
# print(f"is is common : {res}")

#^ ---------------------------------------------------------------------------------------------
#! 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
#* 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#* 		Expected Output : ['Green', 'White', 'Black']

# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# lst.remove('Red')
# lst.remove('Pink')
# lst.remove('Yellow')
# print(lst)
#^ ---------------------------------------------------------------------------------------------
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *

#^ ---------------------------------------------------------------------------------------------
#! 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
#*LOGIC-1
# lst = [0,1,2,3,4,5,6,7,8,9]
# new_lst = []
# for i in lst:
#      if i%2!=0:
#       new_lst.append(i)
# print(new_lst)

#*LOGIC-2
# lst = [0,1,2,3,4,5,6,7,8,9]
# new_lst = []
# for i in lst:
#      if i%2==0:
#           continue
#      else:
#           new_lst.append(i)
# print(new_lst)

#*LOGIC-3
# lst = [0,1,2,3,4,5,6,7,8,9]
# new_lst = []
# for i in lst:
#      if i%2==0:
#           pass
#      else:
#           new_lst.append(i)
# print(new_lst)
#^ ---------------------------------------------------------------------------------------------
#! 15. Write a Python program to shuffle and print a specified list.
#*LOGIC-1
# lst = [23,56,29,47,13,4]
# lst[0],lst[1],lst[2]=lst[3],lst[4],lst[5] 
# print(lst)

#*LOGIC-2 
# lst = [23,56,29,47,13,4]
# lst.sort()
# print(lst)

#*LOGIC-3 
# import random
# lst = [23,56,29,47,13,4]
# random.shuffle(lst)
# print(lst)

# lst = [23,56,29,47,13,4]
# lst.sort(reverse=True)
# print(lst)
#^ ---------------------------------------------------------------------------------------------
#! 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
#*LOGIC-1
# lst = []
# for i in range(1,31):
#        x= i*i
#        lst.append(x)
       
# print(lst)
# print(lst[0:5] )
# print(lst[-5:])

#*LOGIC-2
# lst = []
# for i in range(1,31):
#      lst.append(i*i)
# print(lst)

# first_elements = []
# for i in lst[0:5]:
#        first_elements.append(i)

# last_elements = []
# for j in lst[-5:]:
#      last_elements.append(j)

# new_lst = first_elements+last_elements
# print(new_lst)
#^ ---------------------------------------------------------------------------------------------
#! 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 
# lst = []
# for i in range(1,31):
#      lst.append(i*i)
# print(lst[5:])
#^ ---------------------------------------------------------------------------------------------
#! 18. Write a Python program to generate all permutations of a list in Python.



#^ ---------------------------------------------------------------------------------------------
#! 19. Write a Python program to get the difference between the two lists.
#* LOGIC-1 
# lst1 = [10,20,30,40,48,6]
# lst2 = [10,50,60,20,56,6]
# lst = []
# for i in lst1:
#      if i not in lst2:
#           lst.append(i)
# print(lst)

# * SYMMETRIC DIFFERENCE 
# lst1 = [1,3,4]
# lst2 = [1,3,4,5]
# lst = []
# for i in lst1:
#      if i not in lst2 :
#           lst.append(i)
# for j in lst2:
#      if j not in lst1:
#           lst.append(j)
# print(lst)

#* LOGIC-2
# lst1 = [10,20,30,40,44]
# lst2 = [10,40,44,55,1]
# set3 = set(lst1).difference(lst2)
# print(list(set3))
#^ ---------------------------------------------------------------------------------------------

#! 20. Write a Python program access the index of a list. 
#* LOGIC-1
# lst = [23,45,56,57]
# for i,v in enumerate(lst):
#      print(i,v)

#* LOGIC-2
# lst = [23,45,56,57]
# for i in range(len(lst)):
#      print(i,lst[i])

#^ ---------------------------------------------------------------------------------------------
#! 21. Write a Python program to convert a list of characters into a string. 
#* LOGIC-1
# lst = ["sagar","jay","sahil","maroti"]
# x = " ".join(lst)
# print(x,type(x)) 

# lst = ["sagar","jay","sahil","maroti"]
# for i in lst:
#    for j in i:
#      print("".join(j),type("".join(j)))

# lst = ["sagar","jay","sahil","maroti"]
# s = " "
# for i in lst:
#      print(s+i,type(s+i))


#^ ---------------------------------------------------------------------------------------------
#! 22. Write a Python program to find the index of an item in a specified list. 
#* LOGIC-1
# lst = [23,43,45,56]
# print(lst.index(43))

#* LOGIC-2
# lst = [23,43,45,56]
# val= 45
# for i in range(len(lst)):
#         if lst[i]==val:
#           print(i)

#* LOGIC-3
# lst = [23,43,45,56]
# i = 0
# val = 45
# while(i<len(lst)):
#      if lst[i]==val:
#       print(i)
#      i = i+1

#^ ---------------------------------------------------------------------------------------------
#! 23. Write a Python program to flatten a shallow list. 
#* given list [[1,2,3],[4,5,6],[7,8,9]]
#* expected list [1,2,3,4,5,6,7,8,9]

# lst =  [[1,2,3],[4,5,6],[7,8,9]]
# lst2 = []
# for i in lst:
#      for j in i:
#        lst2.append(j)
# print(lst2)


#^ ---------------------------------------------------------------------------------------------
#! 24. Write a Python program to append a list to the second list. 
# lst = [10,20,30,40]
# new_lst = []
# for i in lst:
#   new_lst.append(i)
# print(new_lst)
#^ ---------------------------------------------------------------------------------------------
#! 25. Write a Python program to select an item randomly from a list.
# import random 
# lst = [10,20,30,40]
# x = random.choice(lst)
# print(x)
#^ ---------------------------------------------------------------------------------------------
# 26. Write a python program to check whether two lists are circularly identical.

#^ ---------------------------------------------------------------------------------------------
# 27. Write a Python program to find the second smallest number in a list. 
#^ ---------------------------------------------------------------------------------------------

# 28. Write a Python program to find the second largest number in a list. 
#^ ---------------------------------------------------------------------------------------------
#! 29. Write a Python program to get unique values from a list. 
#* LOGIC-1
# lst = [4,4,5,5,3,5,5,1,0,7,6,6,9,9]
# lst1 = []
# for i in lst:
#      if i not in lst1:
#           lst1.append(i)
# print(lst1)

#* LOGIC-2
# lst = [4,4,5,5,3,5,5,1,0,7,6,6,9,9]
# lst1 = []
# for i in lst:
#      if i in lst1:
#           continue #pass
#      else:
#           lst1.append(i)
# print(lst1)

#* LOGIC-3
# lst = [4,4,5,5,3,5,5,1,0,7,6,6,9,9]
# lst = list(set(lst))
# print(lst)
#^ ---------------------------------------------------------------------------------------------
#! 30. Write a Python program to get the frequency of the elements in a list. 
#* LOGIC-1
# lst = [4,4,5,5,3,5,5,1,0,7,5,4,6,6,9,9]
# print(lst.count(4))

#* LOGIC-2
# lst = [4,4,5,5,3,5,5,1,0,7,5,5,4,6,6,9,9]
# count = 0
# for i in lst:
#      if i == 5:
#       count +=1
# print(count)

#^ ---------------------------------------------------------------------------------------------
#! 31. Write a Python program to count the number of elements in a list within a specified range. 
#*LOGIC-1
# sn = int(input("enter where you to start :"))
# en = int(input("enter where you to end : "))
# count = 0
# for i in range(sn,en+1):
#      count = count +1
# print("count = ",count)

#*LOGIC-2
# sn = int(input("enter where you to start :"))
# en = int(input("enter where you to end : "))
# count = en - sn + 1
# print("Count = ", count)

#^ ---------------------------------------------------------------------------------------------
#32. Write a Python program to check whether a list contains a sublist.
# lst = [1, 2, 3, 4, 5]
# sublist = [2, 3, 4]






#^ ---------------------------------------------------------------------------------------------
#! 33. Write a Python program to generate all sublists of a list. 
#* For example, for the list [1, 2], the possible sublists are:
# * [] (empty sublist)
# *[1]
# *[2]
# *[1, 2]



#^ ---------------------------------------------------------------------------------------------
#! 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
#* 	Sample list : ['p', 'q']
#* 	n =5
#* 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# lst =  ['p', 'q']
# n = 5
# newlst = []
# for i in range(1,n+1):
#      newlst.append( lst[0]+str(i))
#      newlst.append( lst[1]+str(i))
# print(newlst)
     
#^ ---------------------------------------------------------------------------------------------
#! 36. Write a Python program to get variable unique identification number or string. 
# n = 78 
# if type(n) is str:
#      print("IT IS STRING  ")
# elif type(n) is int or type(n) is float:
#      print("IT IS NUMBER ")
# else:
#      print("IT IS NOT STRING OR NOT NUMBER ")


# n = "sagar"
# if  isinstance(n,str):
#      print("it is string")
# elif isinstance(n,int) or (n,float):
#      print("it is number ")
# else:
#      print("it is not a string or not a number ")

#^ ---------------------------------------------------------------------------------------------
#! 37. Write a Python program to find common items from two lists.
# lst1 = [10,20,30,40,50,90]
# lst2 = [10,60,30,70,80,90]
# lst3= []
# for i in lst1:
#      if i in lst2:
#           lst3.append(i)
# print(lst3)
#^ ---------------------------------------------------------------------------------------------
#! 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
#* 	Sample list: [0,1,2,3,4,5]
#*	Expected Output: [1, 0, 3, 2, 5, 4]
# lst = [0,1,2,3,4,5]
# for i in range(0,len(lst)-1,2):
#      lst[i],lst[i+1]=lst[i+1],lst[i]
# print(lst)
#^ ---------------------------------------------------------------------------------------------
#! 39. Write a Python program to convert a list of multiple integers into a single integer. 
#* 		Sample list: [11, 33, 50]
#* 		Expected Output: 113350

# lst = [11,33,50]
# for i in lst:
#      print(int(i),end="")

#*LOGIC-1
# lst = [11, 33, 50]
# res = ""
# for i in lst:
#       res = res+str(i)

# print(res,type(res))
# res1 = int(res)
# print(res1,type(res1))
#^ ---------------------------------------------------------------------------------------------
#! 40. Write a Python program to split a list based on first character of word. 


#^ ---------------------------------------------------------------------------------------------
#! 41. Write a Python program to create multiple lists.
# while True:
#  n = input("ENTER VALUES : ").split()
#  lst = [int(i) for i in n ]      
# print(lst)

# while True:
#  n = input("enter values : ").split()
#  lst = []
#  for i in n:
#     lst.append(i)
#  print(lst)

# while True:
#   n = int(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER : "))
#   lst = []
#   for i in range(1,n+1):
#        val = int(input(f"ENTER {i} VALUE : ")) 
#        lst.append(val)
#   print(lst)
  
# while True:
#   n = input("ENTER VALUE : ").split()
#   i = 0
#   lst = []
#   while i<len(n):
#        lst.append(int(n[(i)]))
#        i = i+1
#   print(lst)

# while True:  
#     n = int(input("ENTER HOW MANY VALUES YOU WANT TO ENTER : "))
#     i = 1
#     lst = []
#     while i<=n:
#          val = int(input(f"ENTER {i} VALUE : "))
#          lst.append(val)
#          i = i+1
#     print(lst)
           
     
#^ ---------------------------------------------------------------------------------------------
#! 42. Write a Python program to find missing and additional values in two lists.      
#* 	Sample data : Missing values in second list: b,a,c
#* 	Additional values in second list: g,h
# lst1 = ["a","b", "c", "d", "e", "f"]
# lst2 = ["d", "e", "f", "g", "h"]
# for i in lst1:
#         if i not in lst2:
#             print(i)
# for j in lst2:
#     if j not in lst1:
#         print(j)
#^ ---------------------------------------------------------------------------------------------
#! 43. Write a Python program to split a list into different variables. 
# lst = [11,22,33,44]
# a,b,c,d= lst
# print(a,b,c,d)
#^ ---------------------------------------------------------------------------------------------
#! 44. Write a Python program to generate groups of five consecutive numbers in a list.
# lst = [ list(range(i,i+5)) for i in range(1,25,5) ]
# print(lst)

# lst  = []
# for i in range(1,25,5):
#      lst.append(list(range(i,i+5)))
# print(lst)


#^ ---------------------------------------------------------------------------------------------
#! 45. Write a Python program to convert a pair of values into a sorted unique array. 
# lst = [50,4,10,20,10,30,30,50]
# nlst = []
# for i in lst:
#     if i not in nlst:
#         nlst.append(i)

# for j in range(len(nlst)):
#     for k in range(j+1,len(nlst)):
#      if nlst[j]>nlst[k]:
#       nlst[j],nlst[k]=nlst[k],nlst[j]
# print(nlst)
#^ ---------------------------------------------------------------------------------------------
#! 46. Write a Python program to select the odd items of a list. 
# lst = [1,2,3,4,5,6,7,8,9]
# olst = [val for val in lst if val%2!=0]
# print(olst)
#^ ---------------------------------------------------------------------------------------------
#! 47. Write a Python program to insert an element before each element of a list.
# lst= [1,2,3,4,5,6,7,8,9]
# s = input("Enter a letter : ")
# newlst = []
# for i in lst:
#      newlst.append(s)
#      newlst.append(i)
# print(newlst)

#^ ---------------------------------------------------------------------------------------------
#! 48. Write a Python program to print a nested lists (each list on a new line) using the print() function. 
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in lst:
#      print(i)
# print()


#^ ---------------------------------------------------------------------------------------------
#! 49. Write a Python program to convert list to list of dictionaries.
#* Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
#* Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# lst1 =["Black", "Red", "Maroon", "Yellow"]
# lst2 =  ["#000000", "#FF0000", "#800000", "#FFFF00"]
# nlst = [{"color_name":k,"color_code":v } for k,v in zip(lst1,lst2)]
# print(nlst)

#^ ---------------------------------------------------------------------------------------------
#! 50. Write a Python program to sort a list of nested dictionaries. 
#* my_collection = {
# *						'KEY1':{'name':'foo','data':1351,'completed':100},
# *						'KEY2':{'name':'bar','data':1541,'completed':12},
#* 						 'KEY3':{'name':'baz','data':58413,'completed':18}
#* 					    }
#* sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x]['completed']))
#* print(sorted_keys)

#^ ---------------------------------------------------------------------------------------------
#! 51. Write a Python program to split a list every Nth element. 
#* 	Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# *	Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i','l']]

     

#^ ---------------------------------------------------------------------------------------------
#! 52. Write a Python program to compute the difference between two lists.      
#* Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
#* Expected Output:
#* 	Color1-Color2: ['white', 'orange', 'red']
#* 	Color2-Color1: ['black', 'yellow']

# l1= ["red", "orange", "green", "blue", "white"] 
# l2 = ["black", "yellow", "green", "blue"]
# color1_color2 = []
# color2_color1 = []
# for i in l1:
#      if i not in l2:
#           color1_color2.append(i)
# for j in l2:
#      if j not in l1:
#           color2_color1.append(j)
# print(color1_color2)
# print(color2_color1)


#^ ---------------------------------------------------------------------------------------------
#! 53. Write a Python program to create a list with infinite elements. 
# s = 0
# while True:
#  print(s)
#  s = s+1

# def infinite():
#      s = 0
#      while True:
#           yield s
#           s = s+1
# res = infinite()
# for val in res :
#      print(next(res))

#^ ---------------------------------------------------------------------------------------------
#! 54. Write a Python program to concatenate elements of a list. 
# lst = ["my", "name", "is", "anthony", "gunjalwish"]
# print(" ".join(lst))

# s = ""
# for char in lst:
#      s = s+ char+" "
# print(s)
#^ ---------------------------------------------------------------------------------------------
#! 55. Write a Python program to remove key values pairs from a list of dictionaries. 
# lst = [
#     {"name": "John", "age": 25, "city": "New York"},
#     {"name": "Jane", "age": 28, "city": "Los Angeles"},
#     {"name": "Mike", "age": 32, "city": "Chicago"}
# ]
# remove = ["name","age"]
# for dict in lst:
#      for key in remove:
#           if key in dict:
#                del dict[key]
# print(lst)
#^ ---------------------------------------------------------------------------------------------
#! 56. Write a Python program to convert a string to a list. 
# s = "my name is anthony gunjalwish"
# print(s.split())


# lst = []
# for char in s:
#    lst.append(char)
# print(lst)


#^ ---------------------------------------------------------------------------------------------
#! 57. Write a Python program to check if all items of a given list of strings is equal to a given string. 
# def fun():
#  lst = [i for i in input("Eneter list values : ").split() ]
#  n = input("Enter your word : ")
#  for i in lst:
#       if i != n:
#           return False       
#       else: 
#          return False
# res = fun()
# print(f"all items of a given list of strings is equal to a given string : {res}")
#^ ---------------------------------------------------------------------------------------------
#! 58. Write a Python program to replace the last element in a list with another list. 
# 	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
# l1= [1, 3, 5, 7, 9, 10]
# l2 = [2, 4, 6, 8]
# for i in l2:
#      l1.append(i)
# print(l1)

# l1= [1, 3, 5, 7, 9, 10]
# l2 = [2, 4, 6, 8]
# l1[-1:] = l2
# print(l1)

#^ ---------------------------------------------------------------------------------------------
#! 59. Write a Python program to check whether the n-th element exists in a given list.

# lst=[10,20,30,40]
# n= 4
# lst = [10, 20, 30, 40]
# n = 4
# if n-1 < len(lst):
#     print(f"{n} element exists in the given list")
# else:
#     print(f"{n} element does not exist in the given list")


#^ ---------------------------------------------------------------------------------------------
# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
#^ ---------------------------------------------------------------------------------------------
#! 61. Write a Python program to create a list of empty dictionaries.
# lst = []
# for i in range(10):
#      lst.append({})
# print(lst) 

#^ ---------------------------------------------------------------------------------------------
#! 62. Write a Python program to print a list of space-separated elements.
# lst = ["my","name","is","anthony","gunjalwidh"]
# print(" ".join(lst))

#^ ---------------------------------------------------------------------------------------------
#! 63. Write a Python program to insert a given string at the beginning of all items in a list.
#* 	Sample list : [1,2,3,4], string : emp
#* 	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
# lst = [1,2,3,4]
# nlst= []
# for i in lst:
#      nlst.append("emp"+str(i))
# print(nlst)

#^ ---------------------------------------------------------------------------------------------
#! 64. Write a Python program to iterate over two lists simultaneously.
# l1 =["a","b","c","d"]
# l2 = [1,2,3,4]
# for k,v in zip(l1,l2):
#      print(k,v) 
#^ ---------------------------------------------------------------------------------------------
#! 65. Write a Python program to move all zero digits to end of a given list of numbers. 
#* 	Expected output:
#* 	Original list:
#* 	[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
#* 	Move all zero digits to end of the said list of numbers:
#* 	[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1] 
# z = []
# for i in lst:
#     if i == 0:
#      z.append(i)
# nz = []
# for i in lst:
#     if i != 0:
#      nz.append(i)
# result = nz+z
# print(result)
#^ ---------------------------------------------------------------------------------------------
#! 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
# lst = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# mv= 0
# nl = []
# for val in lst:
#      s= sum(val)
#      if s>mv:
#           mv = s
#           nl = val
# print(nl)

#^ ---------------------------------------------------------------------------------------------
#! 67. Write a Python program to find all the values in a list are greater than a specified number.
# lst = [int(val) for val in input("ENTER LST Valeus : ").split()]
# n= int(input("Enter a number : ")) 
# for val in lst :
#      if val>n:
#           print(val)

#^ ---------------------------------------------------------------------------------------------
#! 68. Write a Python program to extend a list without append.      
#* 	Sample data: [10, 20, 30]
# *	[40, 50, 60]
# *	Expected output : [40, 50, 60, 10, 20, 30]
# l1 = [10, 20, 30]
# l2 = [40, 50, 60]
# # print(l2+l1)
# l2.extend(l1)
# print(l2)

#^ ---------------------------------------------------------------------------------------------
#! 69. Write a Python program to remove duplicates from a list of lists.      
#* 		Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# *		New List : [[10, 20], [30, 56, 25], [33], [40]]
# lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# nl= []
# for val in lst:
#     if val not in nl:
#      nl.append(val)
# print(nl)
#^ ---------------------------------------------------------------------------------------------
#! 70. Write a Python program to find the items starts with specific character from a given list. 
#* 		Original list:
# *		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
#* 		Expected Output:
#*		Items start with a from the said list:
#* 		['abcd', 'abc', 'acjd']
#* 		Items start with d from the said list:
#* 		['dagfa']
#* 		Items start with w from the said list:
#* 		[]

# lst = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# al = [ch for ch in lst if ch[0]=="a"]
# dl = [ch for ch in lst if ch[0]=="d"]
# wl = [ch for ch in lst if ch[0]=="w"]
# print(f"Items start with a : {al}")
# print(f"Items start with d : {dl}")
# print(f"Items start with w : {wl}")

#^ ---------------------------------------------------------------------------------------------
#! 71. Write a Python program to check whether all dictionaries in a list are empty or not. 
#* 	Sample list : [{},{},{}]
#* 	Return value : True
#* 	Sample list : [{1,2},{},{}]
#* 	Return value : False
# l1 = [{},{},{}]
# res = True
# for j in l1:
#           if len(j)>0:
#                res=False
#                break
# print(res)

# l2 = [{1,2},{},{}]
# res = True
# for j in l2:
#           if len(j)>0:
#                res= False
#                break
# print(res)
#^ ---------------------------------------------------------------------------------------------
#! 72. Write a Python program to flatten a given nested list structure.
#* 		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
#* 		Flatten list:
#* 		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


#^ ---------------------------------------------------------------------------------------------
#! 73. Write a Python program to remove consecutive duplicates of a given list. 
# *		Original list:
# *		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# *		After removing consecutive duplicates:
# *		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
# lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# nl  = [0,1,2,3,4]
# for i in lst:
#      if not nl  or nl[-1]!=i:
#           nl.append(i)
# print(nl)


#^ ---------------------------------------------------------------------------------------------
#! 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
#* 	Original list:
#* 	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
#* 	After packing consecutive duplicates of the said list elements into sublists:
#* 	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
# lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# nl = []
# for val in lst:
#      if not nl or nl[0][-1]==val :
#           nl.append([val])

# print(nl)

#^ ---------------------------------------------------------------------------------------------
# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4.3, 5, 1]
# 	List reflecting the run-length encoding from the said list:
# 	[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# 	Original String:
# 	automatically
# 	List reflecting the run-length encoding from the said string:
# 	[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

#^ ---------------------------------------------------------------------------------------------
# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	List reflecting the modified run-length encoding from the said list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Original String:
# 	aabcddddadnss
# 	List reflecting the modified run-length encoding from the said string:
# 	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]


#^ ---------------------------------------------------------------------------------------------
# 77. Write a Python program to decode a run-length encoded given list.
# 	Original encoded list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Decode a run-length encoded said list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]

#^ ---------------------------------------------------------------------------------------------
#! 78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
#* 	Original list:
#* 	[1, 1, 2, 3, 4, 4, 5, 1]
#* 	Length of the first part of the list: 3
#* 	Splited the said list into two parts:
#* 	([1, 1, 2], [3, 4, 4, 5, 1])

# lst = [1, 1, 2, 3, 4, 4, 5, 1]
# l1  = lst[:3]
# l2 = lst[3:]
# spl = (l1,l2)
# print(f"Splited the said list into two parts : {spl}")
   

#^ ---------------------------------------------------------------------------------------------
#! 79. Write a Python program to remove the K'th element from a given list, print the new list. Original list:
#* 	[1, 1, 2, 3, 4, 4, 5, 1]
# *	After removing an element at the kth position of the said list:
# *	[1, 1, 3, 4, 4, 5, 1]
# lst = [1, 1, 2, 3, 4, 4, 5, 1]
# k = 2
# if  k<len(lst):
#       lst.pop(k)
# print(lst)

#^ ---------------------------------------------------------------------------------------------
#! 80. Write a Python program to insert an element at a specified position into a given list. 
#* 	Original list:
# *	[1, 1, 2, 3, 4, 4, 5, 1]
#* 	After inserting an element at kth position in the said list:
#* 	[1, 1, 12, 2, 3, 4, 4, 5, 1]
# lst = 	[1, 1, 2, 3, 4, 4, 5, 1]
# lst.insert(2,12)
# print(lst)
#^ ---------------------------------------------------------------------------------------------
# 81. Write a Python program to extract a given number of randomly selected elements from a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Selected 3 random numbers of the above list:
# 	[4, 4, 1]
#^ ---------------------------------------------------------------------------------------------
# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. 
# HINT
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]

#^ ---------------------------------------------------------------------------------------------
#! 83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. 
#* 	Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
#* 	Result:
#* 	243

# lst = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# s = 0
# for i in lst:
#     s = s + round(i)
# print(s*len(lst))
     
#^ ---------------------------------------------------------------------------------------------
#! 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. 
#* 	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
#* 	Minimum value: 4
#* 	Maximum value: 22
#* 	Result:
#* 	20 25 45 55 60 70 80 90 110
# l1= [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# mxv  = round(max(l1))
# minv = round(min(l1))
# nl = []
# print(f"Maximum value : ",mxv)
# print(f"Minimum value : ",minv)
# l1.sort()
# for val in l1: 
#      if val not in nl:
#       nl.append(round(val)*5)

# print(nl)
# for val in nl:
#      print(val,end=" ")



#^ ---------------------------------------------------------------------------------------------
#! 85. Write a Python program to create a multidimensional list (lists of lists) with zeros. 
#* Multidimensional list: [[0, 0], [0, 0], [0, 0]]
# lst = []
# for i in range(3):
#      lst.append([0,0])
# print(lst)

#^ ---------------------------------------------------------------------------------------------
#! 86. Write a Python program to create a 3X3 grid with numbers.
#* 	3X3 grid with numbers:
# *	[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# lst = []
# for i in range(3):
#      lst.append([1,2,3])
# print(lst)

#^ ---------------------------------------------------------------------------------------------
# 87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. 
# 	Input rows: 2
# 	Input columns: 2
# 	Input number of elements in a row (1, 2, 3):
# 	1 2
# 	3 4
# 	sum for each column:
# 	4 6
#^ ---------------------------------------------------------------------------------------------
# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. 
# 	Input the size of the matrix: 3
# 	2 3 4
# 	4 5 6
# 	3 4 7
# 	Sum of matrix primary diagonal:
# 	14
#^ ---------------------------------------------------------------------------------------------
#! 89. Write a Python program to Zip two given lists of lists. 
#* 	Original lists:
#* 	[[1, 3], [5, 7], [9, 11]]
#* 	[[2, 4], [6, 8], [10, 12, 14]]
#* 	Zipped list:
#* 	[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]

# l1 = [[1, 3], [5, 7], [9, 11]]
# l2 = [[2, 4], [6, 8], [10, 12, 14]]
# nl = []
# for k,v in zip(l1,l2):
#      nl.append(k+v)
# print(nl)

# l1 = [[1, 3], [5, 7], [9, 11]]
# l2 = [[2, 4], [6, 8], [10, 12, 14]]
# nl = []
# for k,v in zip(l1,l2):
#      k.extend(v)
#      nl.append(k)
# print(nl)
#^ ---------------------------------------------------------------------------------------------
#! 90. Write a Python program to count number of lists in a given list of lists. 
#* 		Original list:
#* 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
#* 		Number of lists in said list of lists:
#* 		4
#* 		Original list:
#* 		[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
#* 		Number of lists in said list of lists:
#* 		3
# l1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# count = 0
# for val in l1:
#      count = count+1
# print(count)

# l2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# count = 0
# for i in l2:
#      count = count+1
# print(count)
#^ ---------------------------------------------------------------------------------------------
#!  91. Write a Python program to find the list with maximum and minimum length. 
# *	Original list:
#* 	[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 	List with maximum length of lists:
# 	(3, [13, 15, 17])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(3, [3, 5, 7])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(4, [1, 34, 5, 7])
# 	List with minimum length of lists:
# 	(1, [12])


  
#^ ---------------------------------------------------------------------------------------------
#! 92. Write a Python program to check if a nested list is a subset of another nested list. 
#* 		Original list:
#* 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
#* 		[[1, 3], [13, 15, 17]]
#* 		If the one of the said list is a subset of another.:
#* 		True
# *		Original list:
#* 		[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# *		[[[3, 4], [5, 6]]]
# *		If the one of the said list is a subset of another.:
# *		True
#* 		Original list:
#* 		[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
#* 		[[[3, 4], [5, 6]]]
# *		If the one of the said list is a subset of another.:
# *		False
# lst = [[1, 3], [13, 15, 17]]
# lst2 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# for val in lst:
#      if val in lst2:
#        print(True)
#      else:
#          print(False)

# l1 = [[[3, 4], [5, 6]]]
# l2 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# for val in l1:
#      if val in l2:
#        print(True)
#      else:
#          print(False)
     
# l1 = [[[3, 4], [5, 6]]]
# l2 =[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# for val in l1:
#      if val in l2:
#        print(True)
#      else:
#          print(False)
     

#^ ---------------------------------------------------------------------------------------------
#! 93. Write a Python program to count the number of sublists contain a particular element. 
#* 		Original list:
#* 		[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
#* 		Count 1 in the said list:
#* 		3
#* 		Count 7 in the said list:
#* 		2
#* 		Original list:
#* 		[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
#* 		Count 'A' in the said list:
#* 		3
#* 		Count 'E' in the said list:
#* 		1
# lst=  [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# cnt1 = 0
# cnt7 = 0

# for i in lst:
#     for j in i:
#       if j == 1:
#           cnt1 = cnt1 + 1
#       elif j == 7:
#           cnt7 = cnt7 + 1
# print(f"Count of 1 is {cnt1}")
# print(f"Count of 7 is {cnt7}")

# lst2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# cntA = 0
# cntE = 0
# for i in lst2:
#     for j in i:
#       if j == "A":
#           cntA = cntA + 1
#       elif j == "E":
#           cntE = cntE + 1
# print(f"Count of A is {cntA}")
# print(f"Count of E is {cntE}")
#^ ---------------------------------------------------------------------------------------------
#! 94. Write a Python program to count number of unique sublists within a given list. 
#* 	Original list:
#* 	[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
#* 	Number of unique lists of the said list:
#* 	{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
#* 	Original list:
#* 	[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
#* 	Number of unique lists of the said list:
#* 	{('green', 'orange'): 2, ('black',): 1, ('white',): 1}

# lst = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# key= {}
# for i in lst:
#      if tuple(i) not in key :
#         key[tuple(i)] +=1
# print(key) 

# l2 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# key= {}
# for i in l2:
#      if tuple(i) not in key :
#         key[tuple(i)] = l2.count(i)
# print(key) 

#^ ---------------------------------------------------------------------------------------------
# 95. Write a Python program to sort each sublist of strings in a given list of lists. 
# 	Original list:
#	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
#	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]





# 96. Write a Python program to sort a given list of lists by length and value. 
# 	Original list:
# 	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# 97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range. 
# 	Original list:
# 	[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# 	After removing sublists from a given list of lists, which contains an element outside the given range:
# 	[[13, 14, 15, 17]]

# 98. Write a Python program to scramble the letters of string in a given list. 
# 	Original list:
# 	['Python', 'list', 'exercises', 'practice', 'solution']
# 	After scrambling the letters of the strings of the said list:
# 	['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list. 
# 	Original list:
# 	['Python', 3, 2, 4, 5, 'version']
# 	Maximum and Minimum values in the said list:
# 	(5, 2)

# 100. Write a Python program to extract common index elements from more than one given list. 
# 	Original lists:
# 	[1, 1, 3, 4, 5, 6, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	Common index elements of the said lists:
# 	[1, 7]
# ==========================================================================
# Question Bank Part-1.txt
# Displaying Question Bank Part-1.txt.