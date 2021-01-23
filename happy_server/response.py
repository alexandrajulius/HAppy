from collections import namedtuple
from directory_tree import list_tree
# does work for tests but not for server
# from happy_server.directory_tree import list_tree

Response = namedtuple('Response', ['response_code', 'content_type', 'body'])
# signature does not work with types
# def generate_response(path: str) -> Response:


def generate_response(path):
    file_list = list_tree('./public')
    for key, abs_path in enumerate(file_list):
        file_list[key] = abs_path.replace('public/', '')

    if ((path == "/") or (path in file_list)):
        response_code = 200
        # todo content_type: what about text/plain?
        if path == '/':
            content_type = 'text/html'
            # use context manager "with" to open file
            # it will close the file afterwards
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
