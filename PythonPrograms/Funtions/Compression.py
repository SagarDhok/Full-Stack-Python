
#^ --------------------------------------------------------------------------------------------`# lst = [45,34,54,33,0,-1,-3,17,29,-36]
# pv = [ val  for val in lst if val>0]
# nv = [val for val in lst if val<0]
# print("positive values  : ",pv)
# print("negative values : ",nv)`
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING DICT COMPREHENSIOIN 
# def prime(i):
#     if i ==1 :
#      return False
#     res =True
#     for k in range(2,i//2+1):
#         if i%k==0:
#             res = False
#     return res 

# lst = input("ENTER VALUES : ").split() 
# lst_values = {int(i) for i in lst }
# lst_primes = {val:"PRIME" if prime(val) else "NOT PRIME" for val in lst_values }
# for k,v in lst_primes.items():
#     print(k,"-->",v)
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING LIST COMPREHENSIOIN 
# def decideprime(i):
#      res = True
#      for j in range(2,i//2+1):
#           if i%j == 0 :
#            res = False
#      return res 

# lst = input("ENTER COMMA SEPRATED VALUES : ").split()
# values = [int(val) for val in lst if int(val)>1 ]
# primes = [ i for i in values if decideprime(i)]
# non_primes = [i  for i in values if i<1 or  not decideprime(i)]
# print(primes)
# print(non_primes)
#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension to create a list of squares of numbers from 1 to 10.
# lst = [ i**2  for i in range(1,11)]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Use a list comprehension to generate a list of even numbers between 1 and 20.
# lst = [i for i in range(1,21) if i%2 == 0]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension that creates a list of numbers from 1 to 10, but only include numbers greater than 5.
# lst = [i for i in range(1,11) if i>5]
# print(lst)

#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension to convert all characters in the string "hello world" to uppercase.
# lst = [i.upper()  for i in "hello world" ]
# print("".join(lst))
#^ --------------------------------------------------------------------------------------------
#! Generate a list of tuples (x, x^2) for x in the range 1 to 10 using a list comprehension.
# lst = [(x,x**2) for x in range(1,11)]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 and the values are their cubes.
# d = {i:i**3 for i in range(1,6)}
# print(d)
#^ --------------------------------------------------------------------------------------------
#! Use a set comprehension to create a set of unique vowels present in the string "comprehension is fun".
# set = { i for i in "comprehension is fun" if i in "aeiouAEIOU" }
# print(set)
#^ --------------------------------------------------------------------------------------------
#! Use a list comprehension to flatten the following list of lists: [[1, 2, 3], [4, 5], [6, 7, 8]].
# lst = [[1, 2, 3], [4, 5], [6, 7, 8]]
# fst =  [j for i in lst for j in i]
# print(fst)