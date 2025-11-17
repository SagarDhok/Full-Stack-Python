
#! Solve and write in notebook
# # Share


# You said:
# show python tricky quitions
# ChatGPT said:
# ChatGPT
# Here are some tricky Python questions to test your understanding and problem-solving skills:

# 1. Output Prediction
# What will be the output of the following code?

# python
# Copy code
# def func(a, b=[]):
#     b.append(a)
#     return b
# print(func(1))
# print(func(2))

# 2. Mutable Default Argument
# Why does the following code behave the way it does?

# python
# Copy code
# def add_to_list(val, my_list=[]):
#     my_list.append(val)
#     return my_list

# list1 = add_to_list(1)
# list2 = add_to_list(2)
# print(list1, list2)
# 3. Variable Scope
# What will be the output of the following code?

# python
# Copy code
# x = 10

# def modify():
#     global x
#     x += 5

# modify()
# print(x)


# 4. String Multiplication
# What happens when you execute this?

# python
# Copy code
# print("Hello" * -1)
# 5. Dictionary Key Error
# What will this code output?

# python
# Copy code
# my_dict = {1: "one", 2: "two", 3: "three"}
# print(my_dict[4])
# 6. Function Overriding
# What will be printed here?

# python
# Copy code
# def foo(x, y=5):
#     return x + y

# def foo(x, y=10):
#     return x * y

# print(foo(2))
# 7. Unpacking Mystery
# What will be the output?

# python
# Copy code
# a, *b, c = [1, 2, 3, 4, 5]
# print(a)
# print(b)
# print(c)
# 8. Unexpected Behavior
# What is the output, and why?

# python
# Copy code
# lst = [1, 2, 3, 4]
# for i in lst:
#     lst.remove(i)
# print(lst)
# 9. List Comprehension
# What will be the output?

# python
# Copy code
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat = [num for row in matrix for num in row if num % 2 == 0]
# print(flat)
# 10. Boolean Operations
# What will this print?

# python
# Copy code
# print(True == 1)
# print(False == 0)
# print(True + True)
# print(False - True)
# Would you like me to explain any of these or provide additional examples? 😊







# What will be the output of the following code?

# def tricky_function(lst, val):
#     lst.append(val)
#     return [lst] * 2

# list1 = [1, 2, 3,4] 
# result = tricky_function(list1, 4)

# # Modify result
# result[0].append(5)

# print("list1:", list1)
# print("result:", result)


# l1 = [1,2,3]
# l1.append(4)
# ls = [l1]*2
# ls[0].append(5)
# print(ls)


# Memory updated
# Here are more tricky Python snippets that will test and improve your understanding of Python concepts, including variable scope, mutability, and subtle behaviors.

# 1. Mutable Default Arguments
# python
# Copy code
# def append_to_list(val, lst=[]):
#     lst.append(val)
#     return lst

# list1 = append_to_list(10)
# list2 = append_to_list(20)

# print("list1:", list1)
# print("list2:", list2)
# Key Points:
# The default argument lst=[] is evaluated only once, leading to shared behavior.
# Expected Output:
# python
# Copy code
# list1: [10, 20]
# list2: [10, 20]
# Fix:
# Use None as the default argument and initialize inside the function:

# python
# Copy code
# def append_to_list(val, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(val)
#     return lst
# 2. Variable Scope and for Loops
# python
# Copy code
# x = 10

# def tricky_loop():
#     x = 5
#     for x in range(3):
#         pass
#     return x

# print("x:", x)
# print("tricky_loop:", tricky_loop())
# Key Points:
# The loop variable x in for x in range(3) creates a new local scope.
# Output:
# python
# Copy code
# x: 10
# tricky_loop: 2
# Explanation:
# x = 5 is overridden by the loop variable x during iteration.
# 3. Nested Scopes and nonlocal
# python
# Copy code
# def outer_function():
#     x = "outer"

#     def inner_function():
#         nonlocal x
#         x = "inner"
#         print("Inside inner_function:", x)

#     inner_function()
#     print("Inside outer_function:", x)

# outer_function()
# Key Points:
# The nonlocal keyword allows modifying variables in the nearest enclosing scope.
# Output:
# python
# Copy code
# Inside inner_function: inner
# Inside outer_function: inner
# 4. Tuple Immutability with Mutable Items
# python
# Copy code
# tuple1 = ([1, 2], [3, 4])

# tuple1[0].append(5)
# print("tuple1:", tuple1)
# Key Points:
# Tuples are immutable, but their contents (if mutable) can be changed.
# Output:
# python
# Copy code
# tuple1: ([1, 2, 5], [3, 4])
# 5. Unexpected Behavior with is
# python
# Copy code
# a = 256
# b = 256
# print(a is b)

# x = 257
# y = 257
# print(x is y)
# Key Points:
# Small integers (from -5 to 256) are cached in Python, so a is b is True.
# Larger integers like 257 are not cached, so x is y is False.
# Output:
# python
# Copy code
# True
# False
# 6. Dictionary Tricks
# python
# Copy code
# d = {}
# d[1] = "A"
# d[True] = "B"
# d[1.0] = "C"

# print(d)
# Key Points:
# Python treats 1, True, and 1.0 as the same key because they are equal (==).
# Output:
# python
# Copy code
# {1: 'C'}
# Would you like even more challenging problems? 😊






