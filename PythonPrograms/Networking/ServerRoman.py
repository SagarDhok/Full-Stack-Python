
# import socket
# s = socket.socket()
# s.bind(("localhost",9999))
# s.listen(2)
# print("SSP IS READY FOR CSP REQUEST ")

# while True:
#      try:
#         cs,ca =s.accept()
#         csdata = cs.recv(1024).decode()
#         val = int(csdata)
       
#         if val<=0:
#                 cs.send(f"{val} Does not contain roman number ".encode())
#         else:                
#           rn = ""
#           while val>=1000:
#                 rn = rn+"M"
#                 val = val-1000
#           if val>=900:
#                 rn = rn+"CM"
#                 val = val-900
#           if val>=500:
#                 rn = rn+"D"
#                 val = val-500
#           if val>=400:
#                 rn = rn+"CD"
#                 val = val-400
#           while val>=100:
#                 rn = rn+"C"
#                 val = val-100
#           if val>=90:
#                 rn = rn+"XC"
#                 val = val-90
#           if val>=50:
#                 rn = rn+"L"
#                 val = val-50
#           if val>=40:
#                 rn = rn+"XL"
#                 val = val-40
#           while val>=10:
#                 rn = rn+"X"
#                 val = val-10
#           if val >=9:
#                 rn = rn+"IX"
#                 val = val-9
#           if val>=5:
#                 rn = rn+"V"
#                 val = val-5
#           if val>=4:
#                 rn = rn+"IV"
#                 val = val-4
#           while val>=1:
#                 rn = rn+"I"
#                 val = val-1
#           cs.send(rn.encode())
          
#      except ValueError:
#            cs.send("Dont Enter Alnums,Strs, and stymbols - try again".encode())
