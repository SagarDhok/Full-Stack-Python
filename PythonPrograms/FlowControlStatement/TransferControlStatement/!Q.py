


#*BREAK TRANSFER FLOW STATEMENT
# ? =================================================================================================
#! Write a Python program that iterates over the string s = "HELLOHELLOHELLO" using a while loop. Break the loop after the second occurrence of the letter "L".
# *FOR LOOP
# s = "HELLOHELLOHELLO"
# count = 0
# for i in s:
#      if (i == "L"):
#       count = count+1
#      if (count == 2):
#           break
#      print(i)
# else:
#      print("it is else block ")

# #*WHILE LOOP
# s = "HELLOHELLOHELLO"
# i = 0
# count = 0
# while(i<len(s)):
#      if (s[i]=="L"):
#           count = count + 1
#      if (count==2):
#           break
#      print(s[i])
#      i = i + 1
# else:
#      print("IT IS ELSE BLOCK "
# ? =================================================================================================
#! Create a program where you have a string s = "BANANAS". Use a while loop to count the occurrences of the letter "A". Stop counting after the third occurrence of "A", and print all the characters processed before that.
# *FOR LOOP
# s = "BANANAS"
# count = 0
# A_occurance = 0
# for i in s:
#     if (i == "A"):
#         count = count + 1
#         A_occurance += 1
#     if count == 3:
#         break
#     print(i)
# else:
#     print("it is else block of program ")

# print("the occurence of A i ", A_occurance)


#*WHILE LOOP
# s = "BANANAS"
# i = 0
# count = 0
# A_occurance = 0
# while i < len(s):
#     if s[i] == "A":
#         count = count + 1
#         A_occurance += 1
#     if count == 3:
#         break
#     print(s[i])
#     i = i + 1
# else:
#     print("it is else block of program ")

# print("the occurence of A i ", A_occurance)
# ? =================================================================================================
#! Write a program using a while loop to traverse the string s = "SUBMARINE". Break the loop once the first occurrence of the letter "R" is found. Print all the characters before "R".
# *FOR LOOP
# s = "SUBMARINE"
# for i in s:
#      if i == "R":
#           break
#      print(i)

#*WHILE LOOP
# s = "SUBMARINE"
# i = 0
# while(i<len(s)):
#      if s[i] == "R":
#           break
#      print(s[i])
#      i += 1
# ? =================================================================================================


#*CONTINUE TRANSFER FLOW STATEMENT
#? IN WHILE LOOP CONTINUE TRANSFER FLOW REQUIRES 2 INCREAMENT 
# ? =================================================================================================
#! Write a program that prints all numbers from 1 to 10, but skips the number 5 using the continue statement.
# *FOR LOOP
# for i in range(1,11):
#      if (i==5):
#       continue
#      print(i,end=" ")

# *WHILE LOOP
# n = 10
# i = 1
# while(i<=10):
#      if i==5:
#           i = i+1
#           continue
#      print(i,end=" ")
#      i = i+1

# ? =================================================================================================
#! Create a for-loop that iterates over the range of numbers from 1 to 20. Use the continue statement to skip numbers divisible by 3.
# *FOR LOOP
# for i in range(1,21):
#      if (i%3==0):
#           continue
#      print(i,end=" ")

# *WHILE LOOP
# i = 1
# while(i<=21):
#      if i%3==0:
#           i = i+1
#           continue
#      print(i,end=" ")
#      i = i+1
# ? =================================================================================================
#! Create a loop that goes through a list of numbers. Use the continue statement to skip over any even numbers and print only the odd ones.
# *FOR LOOP
# list = [1,2,3,4,5,6,7,8,9]
# for i in list:
#       if i%2==0:
#             continue
#       print(i,end=" ")

# *WHILE LOOP
# n = input("ENTER LIST VALUES ")
# x = n.split()
# print(x)
# i = 0
# while(i<len(x)):
#      if int(x[i])%2 ==0:
#           i = i+1
#           continue
#      print(x[i],end=" ")
#      i = i+1
# ? =================================================================================================
#! Create a Python program that asks the user to input several names and uses a while loop with continue to skip names that start with the letter 'A' or 'a'.


