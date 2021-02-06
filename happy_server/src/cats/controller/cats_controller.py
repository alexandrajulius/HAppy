from happy_server.src.cats.model.cats import call_cats


def index():
    return call_cats()
