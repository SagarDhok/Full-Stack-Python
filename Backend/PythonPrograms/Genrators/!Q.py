# ^-----------------------------------------------------------------------------------------------
#! Basic Concepts
# * Simple Generator Creation Write a Python generator function count_up_to(n) that yields numbers from 1 up to (and including) n.
# def sdrange(n):
#      i = 1
#      while i<=n:
#           yield i
#           i = i+1

# n = int(input("Enter a Number : "))
# res = sdrange(n)
# for i in res:
#      print(i)

# ^-----------------------------------------------------------------------------------------------
#! Even Number Generator
# * Write a generator even_numbers(n) that yields all even numbers from 1 to n.
# def evengen(n):
#      i = 0
#      while i<=n:
#           if i%2==0:
#                yield i
#           i = i+1

# n = int(input("Enter A Number : "))
# res = evengen(n)
# for i in res:
#      print(i)

# ^---------------------------------------------------------------------------------------------
# ! Intermediate Questions
# *Infinite Generator
# *Create a generator infinite_fibonacci() that generates Fibonacci numbers indefinitely.
# def infinite_fibonacci():
#      a = 0
#      b = 1

#      while True:
#           yield a
#           a = b
#           b = a+b
# res = infinite_fibonacci()
# for i in res:
#      print(i)

# ^---------------------------------------------------------------------------------------------
#! Prime Numbers
# * Write a generator function generate_primes() that yields prime numbers one at a time.
# def generate_primes(n):
#   for i in range(2,n+1): # 2,3,4,,5,6,7,8,9
#      res = True
#      for j in range(2,i):
#           if i%j==0:
#                res=  False
#                break

#      if res :
#       yield i

# n= int(input("Enter a number : "))
# r = generate_primes(n)
# for val in r:
#      print(val)

# ^-----------------------------------------------------------------------------------------------
#! Yielding from Lists
# * Given a list of strings, write a generator function string_lengths(strings) that yields the length of each string.
# def string_lengths(s):
#      for i in s:
#       yield len(i)


# s= [word for word in input("Enter line of text : ").split()]
# res = string_lengths(s)
# for val in res:
#      print(val)

# def string_lengths(s):
#      i = 0
#      while i<len(s):
#           yield len(s[i])
#           i = i+1

# s= [word for word in input("Enter line of text : ").split()]
# res = string_lengths(s)
# for val in res:
#      print(val)


# ^-----------------------------------------------------------------------------------------------
#! Advanced Use Cases
# * Custom Range Generator
# * Implement a generator custom_range(start, end, step) that mimics Python's range() function but uses yield.
# def kvrrange(start,end=None,step=1):
#      if end is None:
#           end = start
#           start =  0
#      while start<=end:
#         yield start
#         start = start +step


# res = kvrrange(1,20,)
# for val in res:
#      print(val)
# print("*"*50)
# res = kvrrange(1,5)
# for val in res:
#      print(val)
# print("*"*50)
# res = kvrrange(6)
# for val in res :
#      print(val)


# try:
#  def kvrrange(start, end=None, step=1):
#      if end is None:
#          end = start
#          start = 0  # If only start is provided, we want to start from 0
 
#      if step == 0:
#          raise ValueError
 
#      while start <= end:
#          yield start
#          start += step
 
#  # Test cases
#  res = kvrrange(1, 20, 0)
#  for val in res:
#      print(val)
 
#  print("*" * 50)
 
#  res = kvrrange(1, 5)
#  for val in res:
#      print(val)
 
#  print("*" * 50)
 
#  res = kvrrange(5)
#  for val in res:
#      print(val)

# except ValueError:
#      print("step cannot ba zero")


# ^-----------------------------------------------------------------------------------------------
#! File Line Reader
#* Write a generator function read_large_file(file_path) that reads and yields one line at a time from a large text file.




# ^----------------------------------------------------------------------------------------------
#! Chunked Data Processing
#* Create a generator  that splits a list into chunks of size size.

# def chunk_data(data, size):
#  for i in range(0,len(data),size):
#           yield data[i:i+size]
                
# data = ["my","name","is","anthony","gunjwish","india","is","my","country","all","indians"]
# size = int(input("Enter a numer : "))
# res = chunk_data(data,size)
# for val in res:
#      print(val)



# ^-----------------------------------------------------------------------------------------------
#! Error Handling
#* Generator with Exception Handling
#* Create a generator safe_divide(numbers, divisor) that divides each number in the list numbers by divisor but yields None if the division fails (e.g., division by zero).
# def safe_divide(numbers, divisor):
#      for i in numbers:
#       try:        
#        yield i/divisor
#       except ZeroDivisionError:
#        print("Dont Enter Zero as denominator")
#        yield None
# numbers = [10,20,30,40,50]
# divisor = int(input("Enter A number : "))
# res = safe_divide(numbers, divisor)
# for val in res:
#      print(val)
# # ^----------------------------------------------------------------------------------------------
#! Performance
#* Compare Memory Usage
#* Write a program to compare the memory usage of a generator producing numbers 1 to 10,000 vs. a list containing the same numbers. Use Python’s sys.getsizeof() function to check memory usage.
#* Integration Questions
#* Generator Chaining
#* Write two generators:

# import sys

# # Create a generator that yields numbers from 1 to 10,000
# def number_generator():
#     for i in range(1, 10001):
#         yield i

# # Create a list containing numbers from 1 to 10,000
# number_list = list(range(1, 10001))

# # Calculate and print the memory usage of the list and generator
# list_size = sys.getsizeof(number_list)
# generator_size = sys.getsizeof(number_generator())

# print(f"Memory usage of the list: {list_size} bytes")
# print(f"Memory usage of the generator: {generator_size} bytes")


# ^-----------------------------------------------------------------------------------------------

#! range_squared(start, end) to yield the squares of numbers between start and end.
#* filter_even_squares() to filter only even numbers from the squares.
#* Use them together in a pipeline.
#* Generator Decorator
#* Write a decorator reverse_yield(generator_function) that reverses the output of a generator function.



# ^-----------------------------------------------------------------------------------------------
