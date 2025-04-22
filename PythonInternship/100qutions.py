
#! 1. Find the Missing Number in an Array
# Given an array of n-1 integers ranging from 1 to n with no duplicates,
# find the missing number. The array contains distinct integers.
# Example:
# Input: [1, 2, 4, 5, 6]
# Output: 3

def find_missing_number(arr):
    n = len(arr) + 1
    for i in range(1, n + 1):
        if i not in arr:
            return i
print(find_missing_number([1, 2, 4, 5, 6]))