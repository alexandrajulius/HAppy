# TODO
# this works when running the server:
from directory_tree import list_tree
from routing import resolve
from common import Response

# this works when running the tests:
# from happy.directory_tree import list_tree
# from happy.routing import resolve
# from happy.common import Response


# TODO content_type: text/plain and image
# TODO signature does not work with types when starting server
# def generate_response(path: str) -> Response:


def generate_response(path):
    file_list = list_tree('./happy/public')
    for key, abs_path in enumerate(file_list):
        # cut out 'public/' from paths
        file_list[key] = abs_path.replace('public/', '')

    # html -> 'text/html'
    # css -> 'text/css'
    # img -> 'image/img'
    if has_file_ending(path) and path in file_list:
        file_path = path.split('.')
        file_ending = file_path[-1]
        images = ['ico', 'png', 'gif', 'jpg']
        others = ['html', 'css']
        if file_ending in images:
            content_type = 'image/' + file_ending
        elif file_ending in others:
            content_type = 'text/' + file_ending
        response_code = 200
        public_path = path.replace('/happy', 'happy/public')
        with open(public_path) as f:
            response_body = f.read()
        return Response(response_code, content_type, response_body)
    if path == '/':
        path = '/homepage'
    return resolve(path)


def has_file_ending(path):
    if path.find('.') == -1:
        return False
    return True
