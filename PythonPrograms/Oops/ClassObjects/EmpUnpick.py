import pickle

class EmpUnpick:
     def readdata(self):
          with open("Empdata.Pick","rb") as fp:
               while True:
                try:
                 records = pickle.load(fp)
                 records.dispvals()
                except EOFError:
                   break
                
eo = EmpUnpick()
eo.readdata()
                   
               

