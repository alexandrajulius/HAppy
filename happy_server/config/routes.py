# from typing import Dict


# TODO add action (index) and method (GET)
# def import_routes() -> Dict:
def import_routes():
    return {
        'homepage': {
            'controller': '/happy_server/src/index/controller/index_controller.py'
        },
        'hello': {
            'controller': '/happy_server/src/hello/controller/hello_controller.py'
        },
        'cats/example': {
            'controller': '/happy_server/src/cats/controller/cats_controller.py'
        }
    }
