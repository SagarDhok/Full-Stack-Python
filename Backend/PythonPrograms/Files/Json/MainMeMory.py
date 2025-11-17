
#^----------------------------------------------------------------------------------------------
#! PROGRAM FOR CONVERTING JSON STR DATA INTO DICT DATA IN PYTHON
#*str json - dict data 
# import json
# jsondata='{"STNO":100,"NAME":"ROSSUM","MARKS":78.99}'
# print(jsondata,type(jsondata))         # Type of jsondata -  <class 'str'>

# dict = json.loads(jsondata)
# print(dict,type(dict))                 #Type of dict -  <class 'dict'>
# for k,v in dict.items():
#      print(f"{k}-->{v}")
#*or
# for k in dict:
#      print(k,"-->",dict[k])

#^----------------------------------------------------------------------------------------------
#! PROGRAM FOR CONVERTING DICT DATA TO JSON STR
#* dict - json str
# dict = {"STNO":"100","NAME":"ROSSUM","MARKS":"78.99"}
# # print(dict,type(dict))

# jsondata = str(dict)
# print(jsondata,type(jsondata))

#^----------------------------------------------------------------------------------------------