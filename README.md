In this project, I learn socket programming for TCP connections, how to create a socket, bind it to a specific address and port, as well as send and receive a HTTP packet. The programming language used is Python. 

This Web server contains the following :
• Is capable of processing only one request, 
• Create a connection socket when contacted by a client (browser)
• Receive the HTTP request from this connection
• Parse the request to determine the specific file being requested
• Get the requested file from the server’s file system
• Create an HTTP response message consisting of the requested file preceded by header lines
• Send the response over the TCP connection to the requesting browser.
• If a browser requests a file that is not present in the server, the server return a “404 Not Found” error message.

Instructions on how to run the Web server:

Firstly, you need to open in your IDE the folder that contains the files Web_Server.py, hello.html and README.md. Then you need to run the Python code which is the file called Web_Server.py. After it will print a message ('the web server is up on port:', 80)
Ready to serve... and the connection message details. Next, you need to open the browser and provide the corresponding URL. In this case you need to type localhost/hello.html which is the name of the html file that is placed in the server directory. Also, we are not providing the port number because by default the browser assume port 80. After providing the correct URL you will be the message that the file hello.html has, which is Hello World!
Your File Exist!. If you type a request of a file that is not present in the server; for example, localhost/test.html the server will return a “404 Not Found” error message.


