import sys
from socket import *

#print "<req_code>: ",sys.argv[1]
if(len(sys.argv) < 2):
    print("Usage: python ./server.py <req_code>")
    quit()

#create a tcp socket using a random available port number,
#then get the port number after and print it for the clients to use
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',0))

n_port = serverSocket.getsockname()[1]

serverSocket.listen(1)
print("SERVER_PORT=",n_port)

while(True):
    #receive req_codes through the tcp socket
    connectionSocket, addr = serverSocket.accept()
    req_code = connectionSocket.recv(1024).decode()
    if(req_code == sys.argv[1]):
        #if req_code is correct, create udp socket with random port number
        #send this port number to client
        udpSocket = socket(AF_INET,SOCK_DGRAM)
        udpSocket.bind(('',0))
        r_port = str(udpSocket.getsockname()[1])
        connectionSocket.send(r_port.encode())
        while(True):
            #receive the message to be reversed through the previously
            #created udp socket, reverse then send
            msg, clientAddress = udpSocket.recvfrom(1024)
            msg = msg.decode()
            msg = msg[::-1]
            udpSocket.sendto(msg.encode(),clientAddress)
            udpSocket.close()
            break
        connectionSocket.close()
    else:
        #send -1 if the code is wrong
        connectionSocket.send(str(-1).encode())
        connectionSocket.close()




