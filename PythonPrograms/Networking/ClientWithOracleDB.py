
#! B) Write a Client Side Program in such a way that It should accept employee number from KBD , and get Other details from Server Side Program

import socket
s = socket.socket()
s.connect(("localhost",9999))
empno = input("Enter Employee Number to view Details ")
s.send(empno.encode())
empres= s.recv(1024).decode()
print("-"*50)
print(f"\tEmployee Details ")
print("\t\t",empres)
print("-"*50)