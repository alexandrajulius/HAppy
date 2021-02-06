from happy_server.response import Response
from happy_server.config.routes import import_routes


def resolve(path: str) -> Response:
    routes = import_routes()
    index = path[1:]
    if index in routes:
        config = routes[index]
        logic = str_to_logic(config['controller'])
        return Response(200, '', logic())
    return Response(404, '', '')


# returns the index method of a controller
def str_to_logic(controller_path: str):
    clean_path = controller_path[1:-3]
    module_path = clean_path.replace('/', '.')
    controller = __import__(module_path, fromlist=[''])
    return getattr(controller, 'index')
