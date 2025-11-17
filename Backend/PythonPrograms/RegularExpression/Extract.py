
#^===============================================================================================
#! Program for extracting the Names from Given Text Data
#! NamesExtractEx1.py
# import re
# gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
# sp  = "[A-Z][a-z]+"
# names = re.findall(sp,gd)
# print("Name of the Students")
# for name in names :
#      print("\t",name)
#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data
#! NamesMarksExtractEx1.py
# import re
# gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
# sp = r"\d{2}"
# markslist = re.findall(sp,gd)
# # print(markslist)
# print("Marks of student")
# for marks in markslist:
#      print("\t",marks)
#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data
#! NamesMarksExtractEx1.py
# import re
# gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
# msp = r"\d{2}"
# nsp = r"[A-Z][a-z]+"
# nameslist = re.findall(nsp,gd)
# markslist = re.findall(msp,gd)
# # print(nameslist)
# # print(markslist)

# print("Names \t Marks")
# for n,m in zip(nameslist,markslist):
#   print(f"{n}\t{m}")
#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data which is Present in File
#! NamesMarksExtractEx2.py
# import re
# try:
#  with open("E:\\FULL STACK PYTHON\\PythonPrograms\\RegularExpression\\data.txt","r") as fp:
#       filedata = fp.read()
#       namelist = re.findall(r"[A-Z][a-z]+",filedata) 
#       markslist = re.findall(r"\d{2}",filedata)
      
#       print("Names \t Marks")
#       for n,m in zip(namelist,markslist):
#          print(n,"\t",m)
         
#       #*Apply the Regular Expression
# except FileNotFoundError:
#    print("File does not exist")

#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data which is Present in File
#! NamesMarksExtractEx3.py
# import re
# try:
#      with open("E:\\FULL STACK PYTHON\\PythonPrograms\\RegularExpression\\data2.txt","r")  as fp:
#           filedata = fp.read()
#           nameslist = re.findall(r"[A-z][a-z]+",filedata)
#           emaillist = re.findall(r"\S+@\S+",filedata)
#           for n,m in zip(nameslist,emaillist):
#                print(f"{n} \t {m}")
# except FileNotFoundError:
#      print("File does not exists ")
#^===============================================================================================