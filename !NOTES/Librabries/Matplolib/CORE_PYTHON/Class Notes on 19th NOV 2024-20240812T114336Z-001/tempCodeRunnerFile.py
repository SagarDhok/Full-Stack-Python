
print("Json data={}  Type={}".format(jsondata,type(jsondata)))
print("-"*70)
#Convert JsonData into Dict Type by using    loads()
#Syntax:  DictObject=json.loads(jsonstrdata)
d=json.loads(jsondata)
print("Dict Data={}   Type={}".format(d,type(d)))