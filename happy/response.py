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
        file_list[key] = abs_path.replace('public/', '')

    if is_image(path) and path in file_list:
        file_path = path.split('.')
        file_ending = file_path[-1]
        images = ['ico', 'png', 'gif', 'jpg']
        if file_ending in images:
            content_type = 'image/' + file_ending
            response_code = 200
            response_body = 'todo: send image code :)'
            return Response(response_code, content_type, response_body)
    if path == '/':
        path = '/homepage'
    return resolve(path)


def is_image(path):
    if path.find('.') != -1:
        return False
    return False
