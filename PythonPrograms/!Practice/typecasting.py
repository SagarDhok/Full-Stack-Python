a = 35

# Int to Float:
# How do you convert an integer to a float in Python? Provide an example.
b = float(a)
print(b)

# Float to Int:
# What happens when you convert a floating-point number to an integer in Python? Give an example and explain the result
a = int(16.4874)
print(a)


# Str to Int:
# How can you convert a string representing a number into an integer? What will happen if the string contains non-numeric characters?
a = int("38474")
print(a)

# b = int("sagar")
# print(b)                             -------> valueerror  


# Int to Str:
# Write a Python code snippet to convert an integer to a string. What are the possible use cases for this conversion?

# After converting an integer to a string, how can you verify the type of the resulting value in Python? Write a code snippet to demonstrate this. 
a = 49
b = str(a)
print(b, type(b))

print(str(-76),type(str(-76)))


# Str to Float:
# How can you convert a string containing a decimal number to a float? What will happen if the string has non-numeric characters?

a = "56.57"
print(float(a))

# b = float("sagar")
# print(b)                          ------->ValueError 


# Float to Str:
# How do you convert a floating-point number to a string? Provide an example showing the conversion.

a = str(46.55)
print(a) 

# bool to int:
# How does Python convert boolean values (True and False) to integers? Illustrate with examples.

a= int(True)
print(a)

b = int(False)
print(b)

# Int to Bool:
# How do you convert an integer to a boolean in Python? What will be the result of converting 0, 1, and other non-zero integers?
print(bool(1))

print(bool(0))

a = bool(4674)
print(a)


# Combining Typecasting:
# Given the string "42.5", how can you convert it first to a float, then to an integer, and finally to a string again? Write the Python code for this process.


s = "42.5"

# str to float
float = float(s)
print(float)

# float to str
int= int(float)
print(int)

# int to str
s = str(int)
print(s)




