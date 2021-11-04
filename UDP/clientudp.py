"""UDP client Program. Here Client is sender"""

##from os import _AddedDllDirectory
import matplotlib.pyplot as plt
import time
import socket
import threading
def transmission():
    global packets_log, count,end
    logger = threading.Timer(1.0, transmission)
    logger.start()
    packets_log.append(count)
    count = 0
    if end:
        logger.cancel()
start_time = time.time()
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 1002
Message = "Hello, Server".encode()
count=0
end=False
packets_log=[]
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM=UDP

file = open('hey.png', 'rb') ##reading image 

image_data = file.read(1024)
transmission()
while image_data:
   print("sending image")
   count=count+1
   clientSock.sendto(image_data, (UDP_IP_ADDRESS, UDP_PORT_NO))
   image_data = file.read(1024)
##print(count)
print(packets_log)
t=len(packets_log)
b=range(t)
file.close()
end =True
print("--- %s seconds ---" % (time.time() - start_time))
plt.plot(packets_log, b)
plt.show() #ploting throughput graph
