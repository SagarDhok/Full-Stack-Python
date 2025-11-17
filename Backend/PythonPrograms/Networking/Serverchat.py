

#! (A) : Write a  Server Program in such way that It Should accept a message from Client Side Program and give 
#! Reply to the Client Side Program

import socket 

s = socket.socket()
s.bind(("localhost",9999))
s.listen(2)
while True:
      cs,ca = s.accept()
      csm = cs.recv(1024).decode()
      print("Student : ",csm)
      
      ssm = input("KVR : ")
      cs.send(ssm.encode())


