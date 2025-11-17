# Create a list of 5 random numbers. How do you access the first and last element of the list?
# list= ["paa",66,2+3j,True,33.33]
# print(list[0],list[-1])

# Add an element to the end of a list and remove an element from the list.
#list= ["paa",66,2+3j,True,33.33]
# list.append("bhudke")
# list.remove(66)
# print(list)

# Check if the number 7 is present in the list. If it is, print its index.
# list= ["paa",7,66,2+3j,True,33.33,]
# if 7 in  list:
#      print(list.index(7))
# else:
#      print("it doesnt contain 7")

# Reverse the order of elements in the list without using the built-in reverse() function.
# list = [48,439,348,38][::-1]
# print(list)


# Sort the list in ascending and descending order.
# list = [48,439,348,38]
# list.sort()
# print(list)
# print(list.sort(reverse=True))
# print(list)

# List Operations:
# Write a program to count the number of even and odd numbers in a list.
# Find the largest and smallest number in a list.
# How do you remove duplicates from a list?
# Write a Python program that combines two lists and removes duplicate values.
# Given a list of strings, create a new list containing only strings that start with the letter 'a'.
# List Comprehensions:
# Create a list of squares of all numbers from 1 to 10 using list comprehension.
# Given a list of numbers, create a new list with only the even numbers using list comprehension.
# Using list comprehension, generate a list of the first 10 multiples of 3.
# Write a list comprehension that creates a new list from an existing list, converting all negative numbers to their absolute values.
# List and Functions:
# Write a function that takes a list as input and returns the sum of all elements in the list.
# Write a function that returns the second largest element in a list.
# Create a function that checks if a list is a palindrome (reads the same forwards and backwards).
# Write a function that returns the index of the minimum element in a list.
# Write a function that removes all instances of a given value from a list.
# Advanced List Manipulation:
# Given a list of integers, rotate the list to the right by n positions.
# How do you flatten a list of lists (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4])?
# Write a program that counts the frequency of each element in a list.
# Given two lists of numbers, find the common elements between them.
# Create a list of tuples, where each tuple contains a number and its square, for all numbers from 1 to 5.
# Problem-Solving with Lists:
# Given a list of grades, write a program that calculates the average grade and prints the grades above the average.
# Write a program that finds all pairs of numbers in a list that add up to a target sum.
# Given a list of words, write a program that returns a new list with the lengths of each word.
# Write a Python program that splits a list into two sublists, one containing all the positive numbers and the other containing all the negative numbers.
# Write a program that takes a list and returns a new list with only the unique elements, keeping the original order.
# Given a list of integers, find all the triplets whose sum equals zero.









# Convert two lists into a dictionary:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict = dict(zip(keys,values))
# print(dict)
# Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Merge two Python dictionaries into one:
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# dict3 = dict1|(dict2)
# print(dict3,)
# dict1.update(dict2)
# print(dict1,id(dict1))
# print(dict2,id(dict2))
# print(dict1,id(dict1))       
# Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}


# Print the value of key ‘history’ from the below dictionary:
# sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
# res = sampleDict["class"]["student"]["marks"].get("history")
# res = sampleDict.get("sagar","not found")   # second value will be answer if the first value doesnt exist
# res = sampleDict.get("class").get("student").get("marks").get("history")
# print(res)
# Expected output: 80


# Initialize dictionary with default values:
# Python
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# Expected output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

# Basic Match Case: Write a program that takes an integer input from the user and uses a match statement to print whether the number is negative, zero, or positive.
# Example Input/Output:
# Input: -5
# Output: Negative number

# val = int(input("ENTER A VALUE:"))
# match(val):
#      case val if val>0:
#           print("it is positive number ")
#      case num if val<0:
#           print("it is negative number ")
#      case 0:
#           print("it is ZERO ")


# String Matching: Create a program that takes a string input representing a day of the week (e.g., "Monday", "Tuesday") and uses a match statement to print whether it's a a weekday or a a weekday.

# Example Input/Output:

# Input: Saturday
# Output: Weekend

# day = input("ENTER A DAY : ").lower()
# match(day):
#      case "sunday":
#           print("it is  a weekend ")
       
#      case "monday":
#           print("it is a weekday ")
       
#      case "tuesday":
#           print("it is a weekday ")
       
#      case "wednsday":
#           print("it is a weekday ")
       
#      case "thirsday":
#           print("it is a weekday ")
       
#      case "friday":
#           print("it is a weekday ")
       
#      case "saturday":
#           print("it is a weekend ")
       

# Tuple Matching: Write a function that accepts a tuple of two integers and uses a match statement to print whether the first integer is greater than, less than, or equal to the second integer.

# Example Input/Output:

# Input: (3, 5)
# Output: 3 is less than 5

# List Matching: Implement a function that takes a list as input and uses a match statement to check if the list is empty, contains one element, or contains multiple elements.

# Example Input/Output:

# Input: [1, 2, 3]
# Output: List has multiple elements

# list = [23,5,6 ]
# match(list):
#      case []:
#           print("it is empty list")
#      case _:
#           print("it contains multiple value ")


# Complex Matching: Create a program that takes a string input that describes a person’s details in the format "Name: Age: Occupation". Use a match statement to extract and print the person's name, age, and occupation.

# Example Input/Output:

# Input: John: 30: Engineer
# Output: Name: John, Age: 30, Occupation: Engineer
 
# name = input("enter your name : ")
# age = input("enter your age : ")
# occ = input("enter your occupution : ")

# s = (name<,age,occ)
# # s = (name.split(),age.split(),occ.split())
# # print(s)

# match(s):
#      case [name,age,occ]:
#           print(f"name:{name} , age:{age} , occ:{occ}")
       

# Basic Syntax: Write a while loop that prints numbers from 1 to 10.

# i = 1
# while(i<=20):
#      print(f"{i}",end=" ")
#      i = i+1
# else:
#      print()
#      print("--------------------------------------------------")


# i = 10
# while(i>=1):
#      print(f"{i}",end=" ")
#      i = i-1
# else:
#      print("------------")


# print((-25)**0.5)

# import math
# x = math.sqrt(-25)
# print(x)

# import cmath
# result = cmath.sqrt(-25)
# print(result)  # Output: 5.0

# s  a  g  a  r
#   0  1  2  3  4
# len(5)


# Write a Python program using a while loop to print numbers from 1 to 10.
# n= int(input("ENTER A NUMBER : "))
# i = 1
# while(i<=n):
#     print(i)
#     i+=1
# else:
#     print("it is else block")


# How would you use a while loop to calculate the sum of the first 50 natural numbers?
# v =50
# n=0
# i = 0
# while(i<=v):
#      n=n+i
#      print(i)
#      i=i+1
# print(f"sum of first {v} natural number is {n}")

# User Input: Create a while loop that keeps asking the user for a number and prints it. The loop should stop if the user enters a negative number.




# while(True):
#  number =  int(input("ENTER A NUMBER : " ))
#  if(number<0):
#   print(f"{number} is negative ! Enter valid input")

# n =  int(input("ENTER A NUMBER : " ))
# for i in range(n,0,1):
#      print(i)


