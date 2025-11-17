#                      Recursion Test on string (solve any 6)
#^===============================================================================================
#!  Q1. Write a Python function that calculates the sum of all digits in a
# string using recursion. The string may contain both digits and non-
# digit characters. Your function should only sum the digits and ignore
# the non-digit characters.
# Input: a1b2c3
# Output:6

def sumofdigits(s):
    if not s:
        return 0
    if '0' <= s[0] <= '9':
        return int(s[0]) + sumofdigits(s[1:])
    return sumofdigits(s[1:])
s = "a1b2c3"
print(sumofdigits(s)) 

#^-----------------------------------------------------------------------------------------------
#! Q2. Write a Python function that removes all duplicate characters
# from a string using recursion. The function should return a new string
# that contains only the first occurrence of each character in the
# original string, preserving the order of characters.
# Input:aabbcc
# Output:abc

def rmvdp(s, result=""):
    if not s:
        return result
    
    if s[0] not in result:
        result += s[0]

    return rmvdp(s[1:], result)
s = "aabbcc"
print(rmvdp(s))  
#^-----------------------------------------------------------------------------------------------
#! Q3. Write a Python function that returns all substrings of a given
# string using recursion. The substrings should be returned as a list of
# strings. A substring is any contiguous sequence of characters within a
# string.
# Input:"abc"
# Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
def getsub(s, start=0):
    if start == len(s):
        return []

    sub= []
    for end in range(start + 1, len(s) + 1):
        sub.append(s[start:end])
    
    return sub + getsub(s, start + 1)

text = "abc"
print(getsub(text))

#^-----------------------------------------------------------------------------------------------
#! Q4. Write a Python function that removes all occurrences of the
# character &#39;x&#39; from a given string using recursion. The function should
# return a new string that contains all the characters of the original
# string except for x
# Input: axbxcdx
# Output: abcd

def rmx(s):
    if not s:
        return ""
    if s[0] == 'x':
        return rmx(s[1:])
    return s[0] + rmx(s[1:])
s = "axbxcdx"
print(rmx(s))  


#^-----------------------------------------------------------------------------------------------
#! Q5. Write a Python function that counts the number of occurrences
# of a specific character in a given string using recursion.
# Input: "hello","l"
# Output:2

def countchar(s, char):
    if not s:
        return 0
    if s[0] == char:
        return 1 + countchar(s[1:], char)
    return countchar(s[1:], char)
s = "hello"
char = "l"
print(countchar(s, char)) 




#^-----------------------------------------------------------------------------------------------
#!  Q7. Write a Python function that finds all palindromic substrings of a
# given string using recursion. A palindrome is a string that reads the
# same forward and backward.
# Input: "ababa"
# Output: ['a', 'b', 'a', 'b', 'a', 'aba', 'bab', 'aba', 'ababa']

def pal(s):
    return s == s[::-1]
def find(s, i=0):
    if i == len(s):
        return []

    ans = []
    for j in range(i + 1, len(s) + 1):
        cut = s[i:j]
        if pal(cut):
            ans.append(cut)

    return ans + find(s, i + 1)

text = "ababa"
print(find(text))


#^-----------------------------------------------------------------------------------------------
