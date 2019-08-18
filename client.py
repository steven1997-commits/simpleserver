import sys
from socket import *

#print "<server_address>: ",sys.argv[1]
#print "<n_port>: ",sys.argv[2]
#print "<req_code>: ",sys.argv[3]
#print "message: ",sys.argv[4]

if(len(sys.argv) < 5):
    print("Usage: python ./client.py <server_address> <n_port> <req_code> message")
    quit()

#get the servername and the n_port from the server
#(which should be started first), and then connect
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#get the request code from cmdline arguments, then send it
req_code = sys.argv[3]

clientSocket.send(req_code.encode())

#get the r_port from the server, check to see if
#the req_code is corrrect, r_port will be -1 if
#the req code is incorrect
r_port = int(clientSocket.recv(1024).decode())
if(r_port == -1):
    print("Wrong req_code, quitting...")
    clientSocket.close()
    quit()
clientSocket.close()

#create the udpsocket to send to message to the server
#over the r_port
udpName = sys.argv[1]
udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(sys.argv[4].encode(),(udpName,r_port))

#receive the reversed string and print it
msg, serverAddress = udpSocket.recvfrom(1024)

print(msg.decode())

udpSocket.close()
