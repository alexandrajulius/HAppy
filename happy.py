from happy_server.http_handler import Happy_Handler
import socketserver

PORT = 8080

try:
    # Create an http server and define the handler
    # to manage the incoming requests:
    # 1. argument: a TCP address, that is a tuple (ip address, port number)
    # (passing an empty string as the ip address means that the server
    # will listen on any network interface (all available IP addresses))
    # 2. argument: my Happy_Handler
    server = socketserver.TCPServer(('', PORT), Happy_Handler)
    print('Started http server on port', PORT)

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the http server')
    server.socket.close()
