# s = "python"
# print(s.capitalize())
# print(s,id(s))

# s = s.capitalize()
# print(s,id(s))

# s= "abc123"
# print(s.upper())

# s = "PYTHON PUBG"
# print(s,id(s))
# print(s.isupper())
# s = s.isupper()
# print(s,id(s))

# print(s.isalpha())

# s = "f hs hj"
# print(s.islower())

# s = "575.66"
# print(s.isdigit())



# s="Python is an oop lang"
# print(s.split())
# print(len(s))

# s="12-09-2022"
# print(s.split("-"))


# s="Apple#Banana#nkiwi/Guava"
# print(s.split("#"))

# s="pahama"
# print(s.split("a"))

# set = {"my", "name", "is", "sagar", "dhok" }
# s = "-"
# print(s.join(set))

# s = "python"
# print(s.startswith("48p"))


# s = "python"
# print(s.endswith("python"))

# s="Python is an oop lang" 
# print(s.endswith("6ng"))


# s= "paa bhudke" 
# s.replace("paa","aniket")
# print(s.replace("paa","1222"))


# txt = ",,,,,ssaaww.....banana"

# x = txt.lstrip(",.asw")

# print(x)

# s = "paa        ,    "
# print(s.rstrip())

# s="     Nirkar   Behra   "
# print(s,len(s))
# print(s.strip(),len(s.strip()))

# s = ",,,---sagar----,,,"
# print(s.strip(",-"))


# s= "name  is what i dont know what ok what"
# print(s)
# s= s.replace("what" , "paa")
# print(s) 


# s = "sagar"
# print(s.find("d"))



#Program for Deciding the word whether It is Vowel or not
# #SimpleIfStmtEx3.py
# word=input("Enter any word:").lower() # apple
# # or: Used to check if at least one condition is true (at least one vowel exists in the word)
# if ('a'in word) or ('e'in word) or ('i'in word) or ('o'in word) or ('u'in word):
#     print("{} is a Vowel Word".format(word))
# #     and: Used to check if all conditions are true (no vowels exist in the word).
# if ('a' not in word) and ('e'not in word) and ('i' not in word) and ('o' not in word) and ('u' not in word):
#     print("{} is not a Vowel Word".format(word))


#Program for Deciding the word whether It is Vowel or not
#SimpleIfStmtEx4.py
# word=input("Enter any word:").lower() # apple    isdsjoint no  common true
# if (set(word).isdisjoint(set(list("aeiou")))):              #common   false
#     print("{} is not a Vowel Word".format(word))
# if (not set(word).isdisjoint(set(list("aeiou")))):
#     print("{} is  a Vowel Word".format(word))

#^ --------------------------------------------------------------------------------------------
# n = input("ente a line :")
# lst= []
# for i in n:
#      if 'A' <= i <= 'Z': 
#       lst.append(chr(ord(i)+32))
#      else:
#         lst.append(i)
# print("".join(lst))
#^ --------------------------------------------------------------------------------------------



