"""TCP RENO CLIENT SIDE . CLIENT IS SENDER."""

import matplotlib.pyplot as plt
import socket
import time


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1
start_time = time.time()
file = open('hey.png', 'rb')
image_data = file.read(2048)
cwin=1 #congestion window
thrsld=100 #Thresold value
print("sending image")
file = open('hey.png', 'rb')
image_data = file.read(1024)#Reading image

totcwin=[]

while image_data:
    i=0
    print("sending file.....")
    while(i<cwin):
        client.send(image_data)
        ##coun=coun+1
        if image_data:
            a=(client.recv(4096).decode())
            if a=="pass":
                pass
            else:   #detecting packetloss
                thrsld=cwin/2
                cwin=cwin/2
                break

            
        else:
            pass
        ##totthres.append(thrsld)
        i=i+1
        image_data = file.read(1024)

    if image_data:
        pass
    else:
        cwin=cwin/2

    totcwin.append(cwin)
    if(cwin<thrsld):
        cwin=cwin*2
        #print(cwin)
    elif(cwin>=thrsld):
        cwin=cwin+1
    if(image_data==None):
        cwin=cwin/2

print("Image Sent successfully")
file.close()
client.close()
print(totcwin)
t=len(totcwin)
b=range(t)
file.close()
#end =True
print("--- %s seconds ---" % (time.time() - start_time))
plt.plot(b,totcwin)
plt.show() #graph output