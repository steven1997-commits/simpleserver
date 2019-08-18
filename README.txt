These programs were built on python 2.7.12

Running the programs should be as simple as running the 
bash scripts with their proper commandline arguments.

This is a simple server/client program where a client sends 
a string to the server to be reversed.

First, the client will create a TCP connection with the server
with <server_address> and <n_port> (negotiation port) to agree
on a r_port, where the actual string will be sent.

The string will be send over UDP to the r_port to be reversed.
