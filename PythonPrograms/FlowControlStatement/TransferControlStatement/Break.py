
#? ==================================================================================================
#! PRINTING PYTH WITHOUT INDEXING AND SLICING WITH BREAK STATMENT 
# ! FOR LOOP
#* LOGIC_1
# s = "python"
# for i in s:
#      if (i=="o"):
#           break
#      print(i)
# else:
#      print("this is while loop else block ")
# print("THIS IS OTHER STATEMENT ")


# * LOGIC_2
# s = "python"
# for i in s:
#      if (i=="o"):
#           break
#      else:
#       print(i)
# else:
#      print("this is while loop else block ")
# print("THIS IS OTHER STATEMENT ")


#? ==================================================================================================
#! PRINTING PYTH WITHOUT INDEXING AND SLICING WITH BREAK STATMENT 
#! WHILE LOOP

#* LOGIC_1
# s= "python"
# i = 0
# while(i<len(s)):
#      if (s[i]=="o"):
#           break
#      print(s[i])
#      i= i+1
# else:
#      print("it is else block ")


#* LOGIC_2
# s = "python"
# i = 0
# while i < len(s):
#     if s[i] == "o":
#         break
# #     print(s[i])
#     else:
#      print(s[i])
#     i = i+1
# else:
#      print("It is the else block of the while loop")

#? ==================================================================================================
#* EX_1
# s = "MISSISSIPPI"
# cnt=0
# for ch in s: # s="MISSISSIPPI"
#     if(ch=="I"):
#         cnt=cnt+1
#     if(cnt==2):
#         break
#     print("{}".format(ch),end="")


#* EX_2
# s = "MISSISSIPPI"
# cnt=0
# i=0
# so = 0
# while(i<len(s)): # s="MISSISSIPPI"

#     if(s[i]=="S"):
#         so += 1
#         cnt=cnt+1
      
#     if(cnt==3):
#         break
#     print("{}".format(s[i]),end="")

#     i=i+1
# else:
#     print("IT IS ELSE BLOCK ")
# print()
# print("Occurence of s : {}".format(so))
#? ==================================================================================================

