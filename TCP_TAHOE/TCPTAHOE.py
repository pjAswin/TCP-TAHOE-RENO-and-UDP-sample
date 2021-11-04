"""TCP Tahoe simulated . Output will be graph and congestion window values."""

import matplotlib.pyplot as plt
import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1
start_time = time.time()
file = open('hey.png', 'rb')
image_data = file.read(2048)
##print(client.recv(4096).decode())
cwin=1 #congestion window value
thrsld=100 #thresold value
print("sending image")
file = open('hey.png', 'rb')#reading image
image_data = file.read(1024)

totcwin=[]
totthres=[]
coun=0
while image_data:
    i=0
    print("sending file.....")
    while(i<cwin):
        client.send(image_data)
        coun=coun+1
        if image_data:
            a=(client.recv(4096).decode())
            if a=="pass":
                pass
            else:       #when we detect packact loss, these changes are made
                thrsld=cwin/2
                cwin=1
                break

            
        else:
            pass
        totthres.append(thrsld)
        i=i+1
        image_data = file.read(1024)
    
    if image_data:
        pass
    else:
        thrsld=cwin/2
        cwin=1



    totcwin.append(cwin)
    
    if(cwin<thrsld):
        cwin=cwin*2     #changing congestion window value after each transmisssion
        #print(cwin)
    elif(cwin>=thrsld):
        cwin=cwin+1
    if(image_data==None):
        cwin=1

print("Image Sent successfully")
file.close()
client.close()
print(totcwin)
print(totthres)
t=len(totcwin)
b=range(t)
file.close()
#end =True
print("--- %s seconds ---" % (time.time() - start_time))
plt.plot(b,totcwin)
plt.show()