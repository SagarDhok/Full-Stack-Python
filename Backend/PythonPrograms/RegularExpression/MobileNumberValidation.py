
#^===============================================================================================
#! Program for Validation of Mobile Number
#! MobileNumberValidEx1.py
# import re
# mono = input("Enter Your Mobile Number : ")
# if len(mono)==10:
#      res = re.search(r"\d{10}",mono)
#      if res!=None:
#           print(f"{res.group()} Is Valid Mobile Number")
#      else:
#           print(f"{res} is invalid mobile number its length - it must contain integer values - try again")

# else :
#      print(f"{mono} is Invalid Mobile Number lenght - Try again ")
#^===============================================================================================
#! Program for validating Mobile Number Validation with country code
#! MobileNumberValidationEx2.py
# import re 
# while True:
#      mno = input("Enter Your Mobile Number  wiht country code : ")
#      if len(mno) == 13:
#           res = re.search(r"\+91\d{10}",mno)
#           if res!=None:
#              print(f"{res.group()} is valid Mobile Number : ")
#              break
#           else:
#               print(f"{res} is not a mobile number try again")
#      else:
#          print(f"{mno} is invalid mobile number length")

#^===============================================================================================
#! Program for validating Mobile Number Validation with country code
#! MobileNumberValidationEx3.py
# import re
# while True:
#  mno = input("Enter Your Mobile Number With Country Code : ")
#  if len(mno)==13:
#       res = re.search(r"\+9198\d{8}" ,mno)
#       if res !=None:
#         print(f"{res.group()} Is Valid Mobile Number ")
#         break
#       else:
#          print(f"{res} is not a mobile number")
#  else:
#     print(f"{mno} is invalid number lenght - try again")
#^===============================================================================================
#! Program for validating Mobile Number Validation with country code
#! MobileNumberValidationEx4.py
# import re
# while True:
#      mno= input("Enter Your Mobile with country code ")
#      if len(mno)==13:
#           res = re.search(r"\+91[98]\d{8}",mno)
#           if res !=None:
#                print(f"{res.group()} Is valid Number ")
#           else:
#                print(f"{res} is invalid number")
#      else:
#           print(f"{mno} is invalid length number")

# +91898123456 Is valid Number
## +91989812345 Is valid Number 
#^===============================================================================================