from hamcrest import assert_that, equal_to
from happy.response import generate_response
from happy.common import Response


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


def test_generate_response_for_valid_html_request_hello():
    path = '/hello'
    response = generate_response(path)

    with open('./tests/fixtures/public/hello/hello.html') as body:
        assert_that(response, equal_to(
            Response(200, 'text/html', body.read())
            )
        )


def test_generate_response_for_valid_html_request_example():
    path = '/cats/example'
    response = generate_response(path)

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


def test_generate_response_for_css():
    path = '/happy/css/style.css'
    response = generate_response(path)
    with open('./tests/fixtures/public/css/style.css') as body:
        assert_that(response, equal_to(
            Response(200, 'text/css', body.read())
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
