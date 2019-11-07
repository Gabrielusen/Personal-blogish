import socket   # Imports the attributes of the socket module
Hostname = ' '  # Defines the host name/IP address of the server.

PortNumber = 22222  # Defines a dedicated port number for the server
Buffer = 1024       # Defines the maximum size of data that can be exchanged
ServerAddress = (Hostname, PortNumber)  # Defines the address of the server
Server_Socket = socket.SOCK_STREAM    # Creates a stream #socket for the server
Server_Socket.bind(ServerAddress)     # Binds the server address to #the server socket
