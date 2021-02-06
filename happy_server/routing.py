# this works when running the server:
from config.routes import import_routes
from common import Response


# this works when running the tests:
# from happy_server.config.routes import import_routes
# from happy_server.common import Response


# def resolve(path: str) -> Response:
def resolve(path):
    routes = import_routes()
    index = path[1:]
    if index in routes:
        config = routes[index]
        logic = str_to_logic(config['controller'])
        return Response(200, 'text/html', logic())
    return Response(404, 'text/html', '')


# returns the index method of a controller
def str_to_logic(controller_path):
    clean_path = controller_path[1:-3]
    module_path = clean_path.replace('/', '.')
    controller = __import__(module_path, fromlist=[''])
    return getattr(controller, 'index')
