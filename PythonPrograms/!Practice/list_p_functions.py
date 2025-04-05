# 1.append()
# lst = [0,1,2,3,4,5]
# print(lst,type(lst),id(lst))

# lst.append(["sagar",2+3j,34.55,9999999]) 
# print(lst,type(lst),id(lst))


# lst.append("sagar")
# lst.append(999999999999999)p
# lst.append(2+3j)
# lst.append(True)
# lst.append(23.42897)
# print(lst,type(lst),id(lst))

# 2.insert()
# lst = [0,1,2,3,4,5]
# print(lst,type(lst),id(lst))

# lst.insert(5,"sagar")
# print(lst,type(lst),id(lst))
# lst[4]=False                                    =========>   updating data
# print(lst,type(lst),id(lst))
# lst.insert(-1,True)
# print(lst,type(lst),id(lst))
# lst.insert(-10,"firstpositionadd")
# print(lst,type(lst),id(lst))
# lst.insert(10,"lastpositionadd")
# print(lst,type(lst),id(lst))
# lst.insert(1,["sagar",19,3+2005j])
# print(lst,type(lst),id(lst))




# 3.clear()
# lst=["sagar",19,3+2005j]
# print(lst,id(lst),len(lst))

# lst.clear()
# print(lst,id(lst),len(lst))

# lst= [10,20,30]
# lst.clear()
# print(lst,len(lst))
# print(lst.clear())
# print(lst.clear())

# print(list().clear())


# print(lst.clear())

# lst.append("sagar")
# lst.append("santosh")
# lst.append("dhok")
# print(lst,id(lst),len(lst))

# 4.remove(value)

# lst=["sagar",19,3+2005j]
# print(lst,id(lst),len(lst))

# lst.remove("sagar")
# print(lst,id(lst),len(lst))
# lst.remove(19)
# print(lst,id(lst),len(lst))
# lst.remove(3+2005j)
# print(lst,id(lst),len(lst))


# lst = [10,20,10,40,10]
# print(lst,id(lst),len(lst))

# lst.remove(10)
# print(lst,id(lst),len(lst))
# lst.remove(10)
# print(lst,id(lst),len(lst))
# lst.remove(10)
# print(lst,id(lst),len(lst))

# lst=[10,20,30,10,40,50,10,60]
# x=lst.remove(10)
# print(lst)

# lst=[10,20,30,10,40,50,10,60]
# lst.remove(10)
# print(lst)
# lst.remove(10)
# print(lst)
# lst.remove(10)
# print(lst)

# lst = [].remove()
# print(lst)
# print([].remove(20))
# print(list().remove(20))


# 5.pop(index)
# lst = [10,20,10,40,10]
# print(lst,id(lst),len(lst))

# lst.pop(-3)
# print(lst,id(lst),len(lst))
# lst.pop(-1)
# print(lst,id(lst),len(lst))
# lst.pop(1)
# print(lst,id(lst),len(lst))
# lst.pop(0)
# print(lst,id(lst),len(lst))
# lst.pop(0)
# print(lst,id(lst),len(lst))

# lst.pop(0)
# print(lst,id(lst),len(lst))                    ======> indexerror


# print(list().pop(-4))                          ======> IndexError

# lst=[10,20,30,10,40,50,10,60]
# lst.pop(3)
# print(lst)


# 6.pop()

# lst=["sagar",19,3+2005j]
# print(lst,id(lst),len(lst))
# lst.pop()
# print(lst,id(lst),len(lst))
# lst.pop()
# print(lst,id(lst),len(lst))
# lst.pop()
# print(lst,id(lst),len(lst))


# lst.pop()
# print(lst,id(lst),len(lst))        =====>indexerror
# print(list().pop())                =====>indexerror
# print([].pop())                    =====>indexerror



# 7.index()

# lst=[10,38,50,10,398,11]
# x=lst.index(11)
# print(x)




# lst = [10,20,30,40,50,2,10,4,10,5,10]
# count = 0
# for i in range(len(lst)):
#      if lst[i] == 10:
#       count+=1
#       if count == 2:
#          print(i)


# lst = [10,20,30,40,50,2,10,4,10,5,10]
# count = 0
# for i in lst:
#      if i == 10:
#       count+=1
#       if count == 2:
#          lst.remove(i)
# print(lst)
         

# lst = [10,20,30,40,50,2,10,4,10,5,10]
# val = 10
# while True:
#      if val in lst:
#           lst.remove(val)
#      else:
#         break
# print(lst)