from hamcrest import assert_that, equal_to
from happy_server.routing import resolve, str_to_logic
from happy_server.response import Response
from unittest.mock import patch
from tests.fixtures.src.hello.controller import hello_controller

hello_route = {
    'hello': {
            'path': '/hello',
            'controller': '/happy_server/src/hello/controller/hello_controller.py',
            'action': 'index'
    }
}

cats_route = {
    'cats/example': {
            'path': '/cats/example',
            'controller': '/happy_server/src/cats/controller/cats_controller.py',
            'action': 'index'
        }
}


@patch('happy_server.routing.import_routes', return_value=hello_route)
def test_routing_hello(mock_import_routes):
    path = '/hello'
    actual_response = resolve(path)
    mock_import_routes.assert_called_once()
    with open('./tests/fixtures/public/hello/hello.html') as body:
        assert_that(actual_response, equal_to(
            Response(200, '', body.read())
        ))


@patch('happy_server.routing.import_routes', return_value=cats_route)
def test_routing_cats(mock_import_routes):
    path = '/cats/example'
    actual_response = resolve(path)
    mock_import_routes.assert_called_once()
    with open('./tests/fixtures/public/cats/example/example.html') as body:
        assert_that(actual_response, equal_to(
            Response(200, '', body.read())
        ))


def test_str_to_logic():
    controller_path = '/tests/fixtures/src/hello/controller/hello_controller.py'
    actual_method = str_to_logic(controller_path)
    assert_that(actual_method, equal_to(
        hello_controller.index
    ))
