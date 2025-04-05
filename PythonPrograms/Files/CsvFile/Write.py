
#^---------------------------------------------------------------------------------------------
#!Program for creating a csv file
#*writer()
# import csv
# cn = ["Sno","Name","Marks"]
# records= [[10,"sd",100],
#          [20,"ab",200],
#          [30,"kk",300],
#          [40,"vv",400],
#          [50,"mm",500],
#          [60,"bb",600]]
# with open("stud1.csv","w") as fp:
#      csvwr= csv.writer(fp)
#      csvwr.writerow(cn)
#      csvwr.writerows(records)
#      print("File created succesfully - verify")


#* Taking dynamic data
# import csv
# nc = int(input("Enter how many colums do you want to enter :  "))
# if nc<=0:
#      print("Invalid inut- please enter again ")
# else:
#  column= []
#  for i in range(1,nc+1):
#       val = input(f"Enter {i} column name : ")
#       column.append(val)
#  else:
#    nr = int(input("Enter how many records do you have : "))
#    if nc<=0:
#         print("Invalid inut- please enter again ")
#    else:
#        main_record = []
#        for j in range(1,nr+1):
#           print(f"Enter {j} record")
#           record = []
#           for k in range(len(column)):
#                val = input(f"Enter value for {column[k]} : ")
#                record.append(val)
#           else:
#              main_record.append(record)
#        else: 
#           while True:
#            filename = input("Enter filename : ")
#            if filename.endswith(".csv"):
#             with open(filename,"w") as fp:
#                 cswr = csv.writer(fp)
#                 cswr.writerow(column)
#                 cswr.writerows(main_record)
#                 print("csv file created succesfully ")
#                 break
            
#            else:
#               print("Invalid input please try again")


#^---------------------------------------------------------------------------------------------
#* DictWriter()
# import csv
# cn = ["sno","Name","Marks"]
# record =   [
#     {"sno": 1, "Name": "Alice", "Marks": 85},
#     {"sno": 2, "Name": "Bob", "Marks": 90},
#     {"sno": 3, "Name": "Charlie", "Marks": 78},
#     {"sno": 4, "Name": "David", "Marks": 92},
#     {"sno": 5, "Name": "Ella", "Marks": 88},
#     {"sno": 6, "Name": "Fiona", "Marks": 76},
#     {"sno": 7, "Name": "George", "Marks": 84},
#     {"sno": 8, "Name": "Hannah", "Marks": 91},
#     {"sno": 9, "Name": "Ian", "Marks": 79},
#     {"sno": 10, "Name": "Jasmine", "Marks": 87}
# ]

# with open("Dictwrite.csv","w") as fp:
#      csvdwr = csv.DictWriter(fp , fieldnames=cn)
#      csvdwr.writeheader()
#      csvdwr.writerows(record)


#* TAKING DYNAMIC DATA
# import csv
# nc = int(input("Enter how many colums do you want to enter : "))
# if nc<=0:
#      print("Invalid input - Please try again")
# else:
#      colums = []
#      for val in range(1,nc+1):
#           cval = input(f"Enter {val} column name : ")
#           colums.append(cval)
#      else:
#           nr  = int(input("Enter how many records do you hava : "))
#           if nr <=0:
#                print("Invalid input - please try again")
#           else:
#                main_record = []
#                for i in range(1,nr+1):
#                     print("-"*50)
#                     print(f"Enter {i} Record : ")
#                     print("-"*50)
#                     record= {}
#                     for j in range(len(colums)):
#                          val = input(f"Enter value for - {colums[j]}  : ")
#                          record[colums[j]]= val
#                     else:
#                          main_record.append(record)
#                else:
#                     while True:
#                          filename = input("Enter filename : ")
#                          if filename.endswith(".csv"):
#                               with open(filename,"w") as fp:
#                                csvdwr = csv.DictWriter(fp, fieldnames=colums)
#                                csvdwr.writeheader()
#                                csvdwr.writerows(main_record)
#                                print("File created succesfully - verify ")
#                               break
#                          else:
#                               print("Invalid filename - please enter input")

#^---------------------------------------------------------------------------------------------
