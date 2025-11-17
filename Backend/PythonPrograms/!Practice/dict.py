# d = {"sagar":1,"sagar":2,"sagar":3}
# print(d,type(d))
# print(len(d))

# d = {1:"aaaaaa",2:"bbbbbb",3:"cccccc"}
# print(d,type(d),id(d))
# print(len(d))
# print(d[3])
# d[3]="dddddddd"
# print(d[3])
# print(d,type(d),id(d))

# d ={"AC":49870,"NAME":"sagar","AGE":20}
# kv = d.items()
# print(kv,type(kv))
# for v in kv:
#      print(v,type(v),type(d),type(kv))

# k = d.keys()
# print(k)
# for k in k :
#      print(k)
# v = d.values()
# print(v)
# for v in v :
#      print(v)

# print(d.keys())
# print(d.values())
# print(d["NAME"])
# x = d.get("NAME")
# print(x)
# print(d.get("AGE"))
# for index,value in enumerate(d):
#      print(index,"=",value,d[value])
# print(d["AC"])

# d["NAME"]="JAYY"
# print(d["NAME"])
# print(d["AGE"])

# d= {}
# print(d,type(d),id(d))

# d["AC"]=49870
# d["NAME"]="sagar"
# d["AGE"]=20
# print(d,type(d),id(d))

# d["AC"]=3387
# print(d,type(d),id(d))

# d= dict()
# print(d,type(d),len(d))


# lst =[1393,33783,97856]
# print(len(lst[0]))
# # print(len(lst[1]))
# # print(len(lst[2]))

# x= lst[0].reverse()
# print(x)
# # print(lst[1][::-1])

# d1={10:1.2,20:3.4,30:4.5,40:2.3}
# print(d1,type(d1),id(d1))

# ks=d1.keys()
# print(ks,type(ks),id(ks))

# # lst =list(ks)

# # print(lst,type(lst),id(lst))

# for k in d1.keys():
# 		print(k)

# y=dict().items()
# print(y,type(y),len(y))

# d1={10:1.2,20:3.4,66:{"age":20,77:{1:90,2:10}},30:4.5,40:2.3}
# # x = d1[10]=333
# # print(d1)

# d1[66].clear()
# print(66)
# print(d1.get(66)[77].get(2))

# for k,v in d1.items():
#      print(k,"-->",v,type(v),type(d1))

# for k,v in d1[66][77].items():
# 	print(k,v)
	
# d1[66][77][1]="saagggggggggggggg"
# print(d1)

# print(d1[66][77][1]+d1[66][77][2])

# d1["ADDITION"]=d1[66][77][1]+d1[66][77][2]

# print(d1)



# list = [48,48,49,20,38,38]
# list.insert(1,list[0]+list[1]+list[3]+list[4]+list[5])
# print(list)


# x="1"*50
# print(len(x))




# d1={10:1.2,20:3.4,66:{"age",20,77},30:4.5,40:2.3}

# d1[66].clear()
# print(d1)



# d = {10:"paa", 20:"aniket",30:"bhudke"}
# print(d,id(d),len(d))
# print(d[10],d[20],d[30])
# d[10] = "randkhode"   
# d[40] = "muddu"
# print(d,id(d))


# d = {10:"paa", 20:"aniket",30:"bhudke"}
# print(d[0])   keyerror 
# print(d[10])
# print(d[20])
# print(d[30])

# d[10]="muddu"
# print(d)
# print(d.get(20)) 



# for index, value in enumerate (d):
#   print(index,"-->",value,"-->",d[value])


# d = {10:"paa", 20:"aniket",30:"bhudke"}
# print(d,len(d))
# x = d.clear()
# print(d,len(d))


# print({}.clear(),len({}.clear()))

# d = {10:"paa", 20:"aniket",30:"bhudke"}
# kv = d.keys()
# print(kv)
# print(d.keys())

# for keys in kv:
#      print(keys,type(keys),type(kv),type(d))

# for keys in d.keys():
#      print(keys)

# list= list(d.keys())
# print(list,type(list))


# d = {10:"paa", 20:"aniket",30:"bhudke"}
# vv = d.values()
# print(vv)
# for values in vv:
#      print(values)

# for values in d.values():
#       print(values)

# d = {10:"paa", 20:"aniket",30:"bhudke"}
# kv = d.items()
# print(kv)

# for k,v in kv:
#      print(k,"==>",v)

# print(d.items())
# for k,v in d.items():
#      print(k,"==>",v)

# print(d.items())
# for kv in d.items():
#      print(kv,type(kv))


# x= {}.keys()
# print(x,len(x))

# x= dict().values()
# print(x,len(x))


# x= {}.items()
# print(x,len(x))


# d = {10:"paa", 20:"aniket",30:"bhudke"}
# for k in d:
#      print(k)


# d = {10:"paa", 20:"aniket",30:"bhudke"}
# for k in d:
#      print(k,d[k])


# d = {10:"paa", 20:"aniket",30:"bhudke"}
# for k in d:
#      print(k,d.get(k))


# d = {"Name":"paa" ,"age":20, "gf":{1:"madhura",2:"sakshi",3:"sanika",4:"akanksha"},"sirname":"bhudke"}

# for kv in d.items():
#      print(kv,type(d.keys()),type(d.values()),type(d))

# for k,v in d.items():
#      print(k,"==>",v,type(k),type(v),type(d))

# for kv in d["gf"].items():
#      print(kv)

# for kv in d["gf"].values():
#      print(kv)

# d = {"Name":"paa" ,"age":20, "gf":{1:"madhura",2:"sakshi",3:"sanika",4:"akanksha"},"sirname":"bhudke"}
# d["gf"][5]="sakshi"
# print(d["gf"])
# d["gf"].pop(1)
# d["gf"].popitem()
# d["gf"].clear()
# print(d["gf"])
# d["gf"][1]="neha"
# print(d)
# del d["gf"]

# d["gf"].clear()
# print(d)

# print({}.clear())


# seouge us

# list = [0,1,2,3,4,[11,22,33],5,6,7]
# list[5].sort(reverse=True)

# a = 0
# if a :
#  print(a)
# else:
#    print("else")

# print(+True)

# dict = zip(name,occ)
# a = [1,2,3]
# b  = ["a","b","c"]
# print( dict(zip(a,b)))





#! Taking dynamic dict 
# n = int(input("Enter how many key value pair do you want to enter : "))
# dict = {input(f"Enter {i} key : "): int(input(f"Enter {i} value: "))  for i in range(1,n+1)}
# print(dict)
# print("KEY \t VALUE ")
# for k,v in dict.items():
#  print(k,"\t",v)



# dict1 = {"name":"Jay"}
# print(dict1.get("age"))
# print(dict1.setdefault("name","sagar"))    # ADD AND ACCESS NNNNJNJNNMJNMM]=
# print(dict1)