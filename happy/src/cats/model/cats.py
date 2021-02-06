def call_cats():
    with open('./happy/public/cats/example/example.html') as f:
        cats_html = f.read()
    return cats_html
