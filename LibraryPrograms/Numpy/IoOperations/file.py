
#! Normal python text file
#^=========================================================================================
#& Writing the Data to the Text File 
# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\1.txt","w") as fp:
#      fp.write("1.0 2.0 3.0 \n4.0 5.0 6.0 \n7.0 8.0 9.0 ") 
#      print("Text file is created Succesfully")

#& Reading the Data from the Text File  
# try:
#  with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\1.txt" , "r") as fp:
#     filedata = fp.read()
#     print(filedata)
# except FileNotFoundError:
#   print("File does not found")
#^=========================================================================================
#!normal numpy text files
#!loadtxt() - Numpy reading data funtions
#^=========================================================================================
#&read the Data from text File by using numpy.loadtxt()
# import  numpy as np 
# filedata = np.loadtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\1.txt") 
# print("FILEDATA")
# print(filedata,type(filedata))

#! np.savetxt()
# #& Program for Demonstrating Writing the ndarray object data to text file
# import numpy as np
# a = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print("Given Ndarray Object ")
# print(a)
# np.savetxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\2.txt",a)
# print("Ndarray data saved in file successfully ")


#&Program for Demonstrating Writing the ndarray object data to text file
# import numpy as np
# a = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print("Given Ndarray data")
# print(a)
# np.savetxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\3.txt",a,delimiter="     ",fmt="%1.1f")
# print("Ndarray data saved in text file")


#& read the Data from text File by using numpy.loadtxt()
# import numpy as np
# filedata = np.loadtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\3.txt")
# print(filedata,type(filedata))

#^=========================================================================================
#!Binary files
#^=========================================================================================
#&Program for Demonstrating Writing the ndarray object data to Binary file
#!save()
#*npy extension for binary files
# import numpy as np
# a  = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print("GIven ndarray object ")
# print(a)
# np.save("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\4.npy",a)
# print("Ndarray data saved in binary file - verify")

#!load()
#& Program for Demonstrating Reading data from Binary file into ndarray object
# import numpy as np
# filedata = np.load("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\4.npy")
# print("Filedata")
# print(filedata,type(filedata))

#&Program for Demonstrating Reading data from Binary file into ndarray object
# import numpy as np
# filedata = np.load("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\4.npy")
# print("filedata")
# print(filedata[0:1,::],type(filedata))

#& Program for Demonstrating Reading data from Binary file into ndarray object
# import numpy as np
# filedata= np.load("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\4.npy")
# print("Filedata")
# for val in np.nditer(filedata):
#      print(val)
#^=========================================================================================
#!csv files
#*.csv  extension
#^=========================================================================================
#!fp.write()
#& Writing the Data to the CSV File 
# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\5.csv","w") as fp:
#      fp.write("1.0  2.0 3.0 \n 4.0 5.0 6.0 \n 7.0 8.0 9.0")
#      print("Csv file created and data saved in file")

#!np.genfromtxt()
#& Reading  the Data from the CSV File 
# import numpy as np
# filedata  = np.genfromtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\5.csv",delimiter="")
# print(filedata,type(filedata))


#& Writing the Data to the CSV File 
# import numpy as np
# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\6.csv","w") as fp:
#      fp.write("1.0,2.0,3.0\n 4.0,5.0,6.0\n7.0,8.0,9.0")
#      print("csv file created and data saved successfully")

#& Reading  the Data from the CSV File 
# import numpy as np
# filedata = np.genfromtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\6.csv",delimiter=",")
# print(filedata)


#!10-02-2025
#& Writing the Data to the CSV File 
# import numpy as np
# a = np.array([["big","boy","big"],["life","big","dreams"],["rise","to","top"]])
# np.savetxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\7.csv",a,fmt="%s",delimiter=",")
# print("Data Saved in Csv File successfully")

#& Reading  the Data from the CSV File where It contains str data
# import numpy as np
# filedata = np.genfromtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\7.csv",delimiter=",")
# print(filedata,type(filedata))


#& Reading  the Data from the CSV File where It contains str data
# import numpy as np
# filedata = np.genfromtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\7.csv",dtype=str,delimiter=",")
# print(filedata,type(filedata))

#& Reading  the Data from the CSV File where It contains str data
# import numpy as np
# filedata = np.genfromtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\7.csv",dtype=str,delimiter=",")
# print(filedata,type(filedata))
#^=========================================================================================
#& Create a NumPy array with both numeric and string data
# import numpy as np
# a = np.array([
#      [1,"GUIDO ROSSUM",95.5],
#      [2,"TRAVIS OLIPHANT",88.3],
#      [3,"DENNIS RITCHIE",90.5],
#      [4,"JOHN HUNTER",94.58],
# ],dtype=object)
# print("Content of ndarray")
# print(a,type(a))
# #* Write the above ndarray data to CSV File

# import csv
# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit.csv","w") as fp:
#      cswr = csv.writer(fp)
#      cswr.writerows(a) #* here a is called ndarray object
#      print("Ndarray data written to the file - verify")


# #& Create a NumPy array with both numeric and string data
# import csv
# import numpy as np
# a = np.array([
#      [1,"TRAVIS OLIPHANT",90.3],
#      [2,"GUIDO ROSSUM",88.33],
#      [3,"JOHN HUNTER",95.33]],dtype= object)
# print(a,type(a))

# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit2.csv","w") as fp:
#      cswr = csv.writer(fp)
#      # cswr.writerow(["ID", "Name", "Score"]) #* writing column names
#      for row in a:
#           cswr.writerow(row)
#      print("ndarray data wriiten successfully")



#!x
# import numpy as np
# dtype = [('Id','i4'),('Name','U10'),('Score','f4')]
# filedata = np.genfromtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit2.csv",delimiter=",",dtype=dtype,names=True)
# print(filedata)

#& Most IMP: This Reads the Data from CSV File where It Contains Different Col names with Diff type
# import numpy as np
# #* Define the path to the CSV file
# csv_file_path = "E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit2.csv"
# #* Define the data types for each column
# dtype = [('Id','i4'),('Name','U10'),('Score','f4')]

# #* Read the CSV file into a structured NumPy array
# filedata = np.genfromtxt(csv_file_path,delimiter=",",dtype=dtype,names=True)
# print(filedata)



# for row in filedata:
#      print(row)

# for row in filedata:
#      for val in row:
#           print(val,end="\t")
#      print()


# ! Most Imp: Writing the Ndarray object data to text File and Reading the Text File Data
# import numpy as np
# data_array = np.array([[10,20,30],[40,50,60],[70,80,90]])
# np.savetxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit.data",data_array,fmt="%1.1f")
# print("Data is saved in text file successfully")


# import numpy as np
# loaded_array = np.loadtxt("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit.data")
# print("Orginal numpy array")
# print(loaded_array,type(loaded_array))
# print(loaded_array.dtype)

# print("original numpy array with int")
# loaded_array = loaded_array.astype("i4")
# print(loaded_array)
# print(loaded_array.dtype)


# print("original numpy array with int")
# loaded_array = loaded_array.astype("U20")
# print(loaded_array)
# print(loaded_array.dtype)

# print("original numpy array with int")
# loaded_array = loaded_array.astype("i2")
# print(loaded_array)
# print(loaded_array.dtype)
#^=========================================================================================
#! json data
# import json
# jsnemp=' {"id":"09", "name": "Rossum", "department":"IT"} '
# # print(jsondata,type(jsondata))                    #<class 'str'>

# # &here we converted json str data into Dict Data - only for converting
# dictemp = json.loads(jsnemp)
# print(dictemp,type(dictemp))


#& save the Dict Object into Json File
# import json
# dictobj={'id': '09', 'name': 'Rossum', 'department': 'IT'} 
# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit.json","w") as fp:
#      json.dump(dictobj,fp)
#      print("Dict data saved in json file successfully")

#& Read Json File Data into ndarray object
import json
import numpy as np
with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit.json","r") as fp:
     jsndata = json.load(fp)
     # print(jsndata,type(jsndata))    #Here json data is of type <class,dict'
    #*Convert dict type data into ndarray object data by using array()
     a = np.array(jsndata)
     print(a,type(a))

     for k,v in jsndata.items():
          print(f"{k} -> {v}")



#& Read Json File Data into ndarray object
# import json
# import numpy as np
# with open("E:\\FULL STACK PYTHON\\LibraryPrograms\\Numpy\\IoOperations\\nit2.json","r") as fp:
#      jsndata = json.load(fp)
#      # print(jsndata,type(jsndata))    #Here json data is of type <class,dict'
#     #*Convert dict type data into ndarray object data by using array()
#      a = np.array(jsndata)
#      # print(a,type(a))

#      for k,v in jsndata.items():
#           print(f"{k} -> {v}")
#^=========================================================================================