from hamcrest import assert_that, equal_to
from happy.response import generate_response
from happy.common import Response
from unittest.mock import patch


# gotcha I: in the mock we need to import the mocked dependency
#           from where it is called (happy_server.response.list_tree),
#           not where it is defined (happy_server.directory_tree.list_tree)
#           (https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
#
# gotcha II: the order of the mocks in the signature of the test must be
#            the inverse order from the decorator list (@patch)


def test_generate_response_for_valid_html_request_index():
    path = '/'
    response = generate_response(path)

    with open('./tests/fixtures/public/index.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


@patch('happy.response.list_tree', return_value=['/hello'])
def test_generate_response_for_valid_html_request_hello(mock_list_tree):
    path = '/hello'
    response = generate_response(path)
    mock_list_tree.assert_called_once()
    with open('./tests/fixtures/public/hello/hello.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


@patch('happy.response.list_tree', return_value=['/cats/example'])
def test_generate_response_for_valid_html_request_example(mock_list_tree):
    path = '/cats/example'
    response = generate_response(path)
    mock_list_tree.assert_called_once()
    with open('./tests/fixtures/public/cats/example/example.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


def test_generate_response_for_invalid_html_request():
    path = 'public/hello.html'
    response = generate_response(path)
    assert_that(response, equal_to(
        Response(404, 'text/html', '')
        )
    )


@patch('happy.response.list_tree', return_value=['/happy/css/style.css'])
def test_generate_response_for_css(mock_list_tree):
    path = '/happy/css/style.css'
    response = generate_response(path)
    mock_list_tree.assert_called_once()
    with open('./tests/fixtures/public/css/style.css') as body:
        assert_that(response, equal_to(
            Response(200, 'text/css', body.read())
            )
        )

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 6:
# invalid continuation byte
#
# @patch('happy.response.list_tree', return_value=["/happy/img/happy.ico"])
# def test_generate_response_for_ico_request(mock_list_tree):
#     path = "/happy/img/happy.ico"
#     response = generate_response(path)
#     mock_list_tree.assert_called_once()
#     with open('./tests/fixtures/public/img/happy.ico') as body:
#         assert_that(response, equal_to(
#             Response(200, 'image/ico', body.read())
#             )
#         )
