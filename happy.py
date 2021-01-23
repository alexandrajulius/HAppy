from happy_server.http_handler import Happy_Handler
import socketserver

PORT = 8080

# TCP Server get a TCP address (that is a tuple (ip address, port number))
# and the Handler (that i have to implement)
# (passing an empty string as the ip address means that the server
# will listen on any network interface (all available IP addresses))
httpd = socketserver.TCPServer(("", PORT), Happy_Handler)
print("serving at port", PORT)
httpd.serve_forever()
