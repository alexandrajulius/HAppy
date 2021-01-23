from hamcrest import assert_that, equal_to
from unittest.mock import patch
from happy_server.response import generate_response, Response
# TODO : add ignored files

# gotcha I: in the mock we need to import the mocked dependency
#           from where it is called (happy_server.response.list_tree),
#           not where it is defined (happy_server.directory_tree.list_tree)
#            (https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
#
# gotcha II: the order of the mocks in the signature of the test must be
#            the inverse order from the decorator list (@patch)


@patch('happy_server.response.list_tree', return_value=[])
def test_generate_response_for_valid_html_request_index(mock_list_tree):
    path = "/"
    response = generate_response(path)
    mock_list_tree.assert_called_once()
    with open('./tests/fixtures/public/index.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


@patch('happy_server.response.list_tree', return_value=[
    'public/hello/hello.html'
    ])
def test_generate_response_for_valid_html_request_hello(mock_list_tree):
    path = "hello/hello.html"
    response = generate_response(path)
    mock_list_tree.assert_called_once()
    with open('./tests/fixtures/public/hello/hello.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


@patch('happy_server.response.list_tree', return_value=[
    'public/example/example.html'
    ])
def test_generate_response_for_valid_html_request_example(mock_list_tree):
    path = "example/example.html"
    response = generate_response(path)
    mock_list_tree.assert_called_once()
    with open('./tests/fixtures/public/example/example.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


@patch('happy_server.response.list_tree', return_value=[])
def test_generate_response_for_invalid_html_request(mock_list_tree):
    path = "public/hello.html"
    response = generate_response(path)
    assert_that(response, equal_to(
        Response(404, 'text/html', '')
        )
    )

# TODO send images
# @patch('happy_server.response.list_tree', return_value=[])
# def test_generate_response_for_ico_request(mock_list_tree):
#     path = "/public/img/happy.ico"
#     response = generate_response(path)
#     print(response)
#     with open('./tests/fixtures/public/img/happy.ico') as body:
#         assert_that(response, equal_to(
#             Response(200, 'image/ico', body.read())
#             )
#         )
