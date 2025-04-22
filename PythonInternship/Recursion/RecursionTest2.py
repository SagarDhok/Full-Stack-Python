
#                        Recursion Test-2 (Solve any 6 questions)
#^===============================================================================================
#! Q1. Given a number, we need to find sum of its digits using recursion.
# Examples: 
# Input : 12345
# Output : 15
# Input : 45632
# Output :20

# def sumdigits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sumdigits(n // 10)

# print(sumdigits(12345))  
# print(sumdigits(45632))  
#^-----------------------------------------------------------------------------------------------
#! Q2.Given two numbers N and r, find the value of  N C r  using recursion
# Examples:
# Input: N = 5, r = 2
# Output: 10
# Explanation: The value of 5C2 is 10
# Input: N = 3, r = 1
# Output: 3


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

print(nCr(5, 2))
print(nCr(3, 1))  
#^-----------------------------------------------------------------------------------------------
#! Q3. Write a recursive function to count the number of vowels in a given string.

def count_vowels(s):
    if not s:
        return 0
    vowels = "aeiouAEIOU"
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

print(count_vowels("AnthonyGunjlaiwhish"))  


#^-----------------------------------------------------------------------------------------------
#! Q4. Given a string calculate length of the string using recursion. 
# Examples: 
# Input : str = abcd;
# Output :4

def strl(s):
    if s == "":
        return 0
    return 1 + strl(s[1:])

print(strl("abcd"))  

#^-----------------------------------------------------------------------------------------------
#!  Q5. Given a decimal number as input, we need to write a program to convert the given
# decimal number into an equivalent binary number. 
# Examples : 
# Input : 7
# Output :111

# Input :10
# Output :1010

def dtob(n):
    if n == 0:
        return ""
    return dtob(n // 2) + str(n % 2)

print(dtob(7))   
print(dtob(10)) 

#^-----------------------------------------------------------------------------------------------
#! Q6. Count Set-bits of number using Recursion
# Given a number N. The task is to find the number of set bits in its binary representation
# using recursion.
# Examples: 
# Input : 21 
# Output : 3 
# 21 represented as 10101 in binary representation
# Input : 16 
# Output : 1 
# 16 represented as 10000 in binary representation

def csb(n):
    if n == 0:
        return 0
    return (n % 2) + csb(n // 2)

print(csb(21))  
print(csb(16))  



#^-----------------------------------------------------------------------------------------------
#! Q7. Given n friends, each one can remain single or can be paired up with some other friend.
# Each friend can be paired only once. Find out the total number of ways in which friends can
# remain single or can be paired up.
# Examples :
# Input: n = 3
# Output: 4
# Explanation:
# {1}, {2}, {3} : All single
# {1}, {2,3} : 2 and 3 paired but 1 is single.
# {1,2}, {3} : 1 and 2 are paired but 3 is single.
# {1,3}, {2} : 1 and 3 are paired but 2 is single.
# Note that {1,2} and {2,1} are considered same.

def countpair(n):
    if n == 0 or n == 1:
        return 1
    
    return countpair(n - 1) + (n - 1) * countpair(n - 2)

print(countpair(3)) 

#^-----------------------------------------------------------------------------------------------
#! Q8. Print Each Character of a String:

def printchars(s):
    if len(s) == 0:
        return
    print(s[0], end='')
    printchars(s[1:])
printchars("hello")  

#^-----------------------------------------------------------------------------------------------
