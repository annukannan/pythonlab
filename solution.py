# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  #serverSocket = socket(AF_INET, SOCK_STREAM)
  server = socket(AF_INET, SOCK_STREAM)
  server.bind(('127.0.0.1', port))
  #Prepare a server socket
  #serverSocket.bind(('127.0.0.1', port))
  #Fill in start
  server.listen()
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = server.accept()
    try:

      try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket.
        #Fill in start
        okMessage = 'HTTP/1.1 200 OK \r\n'
        #Fill in end

        #Send the content of the requested file to the client
        connectionSocket.send(okMessage.encode())
        
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        #Send response message for file not found (404)
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 File Not Found \r\n'.encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  server.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
