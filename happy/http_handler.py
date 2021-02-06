from http import server
from response import generate_response


class Happy_Handler(server.BaseHTTPRequestHandler):
    # respond to GET requests
    def do_GET(self):
        response = generate_response(self.path)
        if response.response_code == 404:
            # TODO send 404.html
            self.send_error(404)
        else:
            self.send_response(response.response_code)
            self.send_header('Content-type', response.content_type)
            self.end_headers()
            response_body = response.body
            # TODO encode images
            self.wfile.write(response_body.encode('utf-8'))
