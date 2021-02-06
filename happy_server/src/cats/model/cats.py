def call_cats():
    # business logic
    with open('./public/cats/example/example.html') as f:
        cats_html = f.read()
    return cats_html
