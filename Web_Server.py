# Import socket 
from socket import *    

# Assign a port number
serverPort = 80

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to stablish address connection
serverSocket.bind(('', serverPort))

# Listen to at minimum 1 connection at a time
serverSocket.listen(1)

print ("the web server is up on port:",serverPort)


while True:
    #server is ready to stablish the connection
	print ('Ready to serve...')
	
	# Set up a new connection from the accepted client
	connectionSocket, addr = serverSocket.accept()
	
	try:
		# getting the request message from the client
		message =  connectionSocket.recv(1024)
		
		#Print the connection message
		print(message)

        # getting file name from the message
		filename = message.split()[1]

		#Print the file name
		print(filename[1])
		
		# opening the file  
		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read()

		# Send the HTTP response header line to the connection socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		print ("404 Not Found")
		connectionSocket.send("""HTTP/1.0 404 Not Found\r\n""".encode())

		# Close the client connection socket
		connectionSocket.close()

serverSocket.close()  
