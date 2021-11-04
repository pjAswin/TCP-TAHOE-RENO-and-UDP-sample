"""UDP server program. Server is reciver"""

from socket import *
import sys
import select

host="127.0.0.1"
port = 1002
s = socket(AF_INET,SOCK_DGRAM) #SOCK_DGRAM=UDP
s.bind((host,port))

addr = (host,port)
buf=1024

f = open("file.png",'wb') #writing image to file.png 

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print ("File Donwloaded")