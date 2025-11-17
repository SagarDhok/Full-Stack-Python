
#*Without CSV
# with open("Dictwrite.csv","r") as fp:
#  filedata = fp.read()
#  print(filedata)

#^-----------------------------------------------------------------------------------------------
#!Program for Reading the Data from CSV File without using csv module
#*Example-1
# import csv
# with open("Dictwrite.csv", "r") as fp:
#  csvr = csv.reader(fp) # Here csvr is an object of <class, _csv.reader>
#  for record in csvr:
# #    print(record)   # here record is an object of <class, list>
#       for val in record:
#        print("\t",val, end="\t")
#       print()

#*pandas
#*Example-2 
# import pandas as pd
# fd = pd.read_csv("stud1.csv")
# #print(type(filedata))   #<class 'pandas.core.frame.DataFrame'>
# print(fd)


#*in dict
# import csv
# with open("Dictwrite.csv","r") as fp:
#      filedata= csv.DictReader(fp) 
#     # print(type(filedata))  ## here csvdr is an object of <class 'csv.DictReader'>
#      recno= 1
#      for dictrec in filedata:    
#           # print(type(dictrec)) # here dictrec is an object of <class, dict>   #dict print karte
#           print(f"Record : {recno}")
#           for k,v in dictrec.items():     # tya andarchya value  
#             print(f"{k} --> {v}")
#           print()
#           recno = recno+1
#^-----------------------------------------------------------------------------------------------
