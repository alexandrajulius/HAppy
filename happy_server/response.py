from collections import namedtuple
# TODO
# this works when running the server:
# from directory_tree import list_tree
# this works when running the tests:
from happy_server.directory_tree import list_tree

Response = namedtuple('Response', ['response_code', 'content_type', 'body'])
# TODO content_type: text/plain
# TODO signature does not work with types when starting server
# def generate_response(path: str) -> Response:


def generate_response(path):
    file_list = list_tree('./public')
    for key, abs_path in enumerate(file_list):
        file_list[key] = abs_path.replace('public/', '')

    if ((path == "/") or (path in file_list)):
        response_code = 200
        if path == '/':
            content_type = 'text/html'
            # context manager "with" will open file, read and close
            with open('./public/index.html') as f:
                response_body = f.read()
        else:
            file_path = path.split('.')
            file_ending = file_path[-1]
            images = ['ico', 'png', 'gif', 'jpg']
            if file_ending in images:
                content_type = 'image/' + file_ending
            else:
                content_type = 'text/' + file_ending
            public_path = './public/' + path
            with open(public_path) as f:
                response_body = f.read()
    else:
        response_code = 404
        response_body = ''
        content_type = 'text/html'
    return Response(response_code, content_type, response_body)
