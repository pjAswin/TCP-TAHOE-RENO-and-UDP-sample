"""TCP server for both TCP TAHOE and TCP RENO. Server is reciver here !!!. We are adding packet drop manually by sending manually generated acknowledge """

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()
##client_socket.send("lost".encode())
file = open('server_image.jpg', "wb") #write image to server_image.jpg file
counter=0
imagerecv = client_socket.recv(1024) 
client_socket.send("pass".encode()) # stream-based protocol
while imagerecv:
    file.write(imagerecv)
    counter=counter+1
    imagerecv = client_socket.recv(1024)
    if(counter==7000):      #manual adding data drop
        client_socket.send("lost".encode())
    else:
        client_socket.send("pass".encode())


file.close()
client_socket.close()