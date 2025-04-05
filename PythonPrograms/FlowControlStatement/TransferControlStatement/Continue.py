# ? =================================================================================================
#!  PROGRAM FOR DEMONSTRATING THE NEED OF CONTINUE STATEMENT
#* FOR_LOOP
# s="PYTHON"
# for ch in s:
#     if(ch=="T"):
#         continue
#     print("{}".format(ch))
# else:
#     print("I am from else Part")

#* WHILE_LOOP
# s = "PYTHOTN"
# i = 0
# count = 0

# while i < len(s):
#     if s[i] == "T":
#         count += 1
#         if count == 2:  
#           i += 1 
#           continue  
#     print(s[i])  
#     i += 1

# else:
#     print("It is the else block")

# ? =================================================================================================
#!  PROGRAM FOR DEMONSTRATING THE NEED OF CONTINUE STATEMENT
#* FOR_LOOP
# s = "PYTHON"
# for ch in s:
#     if(ch=="T") or (ch=="O") :
#         continue
#     print("{}".format(ch))
# else:
#     print("I am from else Part")


#* WHILE_LOOP
# s="PYTHON"
# i=0
# while(i<len(s)): # s="PYTHON"
#    if(s[i]=="T") or s[i]=="O":
#        i = i + 1
#        continue
#    else:
#      print(s[i])
#      i = i+1
# else:
#   print("I am from else Part")

#* EXAMPLE
# s = "python"
# for i in s:
#      if i  in ["t","o"]:
#       continue
#      print(i)
#? =================================================================================================
# !𝗣𝗿𝗼𝗴𝗿𝗮‍𝗺 𝗳𝗼𝗿 𝗮𝗰𝗰𝗲𝗽𝘁𝗶𝗻𝗴 𝗮 𝗟𝗶𝗻𝗲 𝗼𝗳 𝗧𝗲𝘅𝘁 𝗮𝗻𝗱 𝗘𝘅𝘁𝗿𝗮𝗰𝘁 𝗢𝗻𝗹𝘆 𝗩𝗼𝘄𝗲𝗹𝘀 𝗕𝘆 𝘂𝘀𝗶𝗻𝗴 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲 𝘀𝘁𝗺𝘁
# line=input("Enter line of Text:")
# nov=0
# for ch in line:
#     if(ch.lower() not in ['a','e','i','o','u'] ):
#         continue
#     print(ch,end=" " )
#     nov=nov+1
# print("Number of Vowels=",nov)
