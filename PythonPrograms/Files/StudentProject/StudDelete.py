import pickle
def studdelete():
     try:
      with open("Nit.data","rb") as fp:
           lst  = [[10,"karan",80]]
           while True:
                try:
                 filedata= pickle.load(fp)
                 lst.append(filedata)
                except EOFError:
                    break
           sno = int(input("Enter Student number : "))
           res = False
           for val in lst:
               if sno == val[0]:
                   res= True
                   dr = val
                   break
           if res :
               lst.remove(dr)
               print("Record deleted Successfully ")
               with open("Nit.data","wb") as wp:
                   while True:
                        for val in wp:
                            wp = pickle.load(wp,val)
                            print(f"{val}",end = " ")
           else:
                print("Record Does not exits ")
     except FileNotFoundError:
         print("File does not exist")    
studdelete()


  
  