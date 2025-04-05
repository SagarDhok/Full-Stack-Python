
#! Server:	(A). Write a  Server Program in such way that It Should a Numerical Value from Client Side Program, Square It and Send the Result to Client Side Program
# ! ServerSquare.py

# import socket
# s = socket.socket()
# s.bind(("localhost",9999))
# s.listen(2)
# print("SSP is Ready to accept any CSP Request")
# while True:
#     try:
#      cs,ca =s.accept()
#      csdata= cs.recv(1024).decode()
#      val = float(csdata)
#      res = val**2
#      cs.send(str(res).encode())
#     except ValueError:
#        cs.send("Dont Enter alnums,alphabets ,symbols")
   
