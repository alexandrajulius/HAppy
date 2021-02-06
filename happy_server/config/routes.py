from typing import Dict


def import_routes() -> Dict:
    return {
        'hello': {
            'path': '/hello',
            'controller': '/happy_server/src/hello/controller/hello_controller.py',
            'action': 'index'
        },
        'cats/example': {
            'path': '/cats/example',
            'controller': '/happy_server/src/cats/controller/cats_controller.py',
            'action': 'index'
        }
    }
