import socket
import os
import time

SERVER = ("<IP_ADDRESS>", <PORT_NUMBER>)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(SERVER)
AUTH = "<AUTHENTICATION_KEY>"
s.send(AUTH.encode())

while True:
    # Wait for server approval
    auth_response = s.recv(1024).decode().strip()
    if auth_response != "<AUTHENTICATION_KEY>":
        print("Connection has been rejected by server. Retrying authentication...")
        s.close()
        time.sleep(5)
        continue
    else:
        print("Connected and approved!")
        while True:
            print("Enter command to execute: ")
            s.send(input().encode())
            print(s.recv(65536).decode())
