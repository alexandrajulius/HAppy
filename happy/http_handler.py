from http import server
from response import generate_response


class Happy_Handler(server.BaseHTTPRequestHandler):
    # respond to GET requests
    def do_GET(self):
        response = generate_response(self.path)
        if response.response_code == 404:

            self.send_error(404)
        else:
            self.send_response(response.response_code)
            self.send_header('Content-type', response.content_type)
            self.end_headers()
            self.wfile.write(bytes(response.body))
