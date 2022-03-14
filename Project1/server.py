from socket import *
serverPort=12000
serverSocket = socket(AF_INET, SOCK_STREAM) # Sreate a TCP welcoming socket
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)  # Serve begin to listen
print'The server is ready to receive',serverPort
while True: #loop forever
 print 'waiting for request'
 connectionSocket, addr = serverSocket.accept() #Server waits on accept() for incoming request 

 try:

     message = connectionSocket.recv(1024)
     print message,'::',message.split()[0],':',message.split()[1]  #print HTTP request
     filename = message.split()[1]
     f = open(filename[1:])
     Data = f.read()
     print Data #Response data on HTML message 
     connectionSocket.send('\nHTTP/1.1 200 OK\n\n')# Send HTTP headline into socket
     connectionSocket.send(Data)
     connectionSocket.close()
 
 except IOError:# Response not found
         connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
         connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
         print 'HTTP/1.1 404 Not Found'
         
