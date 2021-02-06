from hamcrest import assert_that, equal_to
from happy.routing import resolve, str_to_logic
from happy.common import Response
from unittest.mock import patch
from tests.fixtures.src.hello.controller import hello_controller


index_route = {
    'homepage': {
            'controller': '/happy/src/index/controller/index_controller.py'
        }
    }

hello_route = {
    'hello': {
            'controller': '/happy/src/hello/controller/hello_controller.py'
        }
    }

cats_route = {
    'cats/example': {
            'controller': '/happy/src/cats/controller/cats_controller.py'
        }
    }


@patch('happy.routing.import_routes', return_value=index_route)
def test_routing_index(mock_import_routes):
    path = '/homepage'
    # TODO resolve still finds the controller path in happy_server.src
    # the src namespace should be mocked from fixtures
    actual_response = resolve(path)
    mock_import_routes.assert_called_once()
    with open('./tests/fixtures/public/index.html') as body:
        assert_that(actual_response, equal_to(
            Response(200, 'text/html', body.read())
        ))


@patch('happy.routing.import_routes', return_value=hello_route)
def test_routing_hello(mock_import_routes):
    path = '/hello'
    actual_response = resolve(path)
    mock_import_routes.assert_called_once()
    with open('./tests/fixtures/public/hello/hello.html') as body:
        assert_that(actual_response, equal_to(
            Response(200, 'text/html', body.read())
        ))


@patch('happy.routing.import_routes', return_value=cats_route)
def test_routing_cats(mock_import_routes):
    path = '/cats/example'
    actual_response = resolve(path)
    mock_import_routes.assert_called_once()
    with open('./tests/fixtures/public/cats/example/example.html') as body:
        assert_that(actual_response, equal_to(
            Response(200, 'text/html', body.read())
        ))


def test_str_to_logic():
    controller_path = '/tests/fixtures/src/hello/controller/hello_controller.py'
    actual_method = str_to_logic(controller_path)
    assert_that(actual_method, equal_to(
        hello_controller.index
    ))
