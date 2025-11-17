
#^-----------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
 #* inside of class
# class student:
#    crs = "python"           
#    city= "Hydrabad"    #todo - Here crs and city are called class level data member


# s1 = student()
# # s2 = student()
# # print(type(s1),id(s1))  <class '__main__.student'> 2736275793168
# # print(f"The content of s1 : {s1.__dict__}")    #Class Level Data Members are Not available with Object and not part of object 
# #todo - Access the value of class level data members

# print(f"Student course : {s1.crs}")
# print(f"Student city : {s1.city}")
# # print(f"Student course : {s2.crs}")
# # print(f"Student city : {s2.city}")
# print("--------------or-----------------")
# print(f"Student Course : {student.crs}")   # todo - we can access class level data members by objcect and class name also
# print(f"Student City : {student.city}")

#^-----------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
#* inside of main program
# class student : pass

# student.crs = "Python"
# student.city = "Hyd"

# s = student()
# print(f"Content of s : {s.__dict__}") #Class Level Data Members are Not available with Object and not part of object 

# print(f"Student Course = {student.crs}")
# print(f"Student City : {student.city}") # todo - we can access class level data members by objcect and class name also

# print("---------or------------")

# print(f"Student Course : {s.crs}")
# print(f"Student City : {s.city}")
#^-----------------------------------------------------------------------------------------
