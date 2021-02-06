from hamcrest import assert_that, equal_to
from happy_server.directory_tree import list_tree
# TODO : add ignored files


def test_directory_tree():
    root = "./tests/fixtures/public"
    file_list = list_tree(root)
    assert_that(file_list, equal_to(
        [
            '/tests/fixtures/public/cats/example/example.html',
            '/tests/fixtures/public/cats/example1_2/example1_2.html',
            '/tests/fixtures/public/cats/cats.html',
            '/tests/fixtures/public/index.html',
            '/tests/fixtures/public/example2/example2.html',
            '/tests/fixtures/public/img/happy.ico',
            '/tests/fixtures/public/hello/hello.html'
        ]
    ))
