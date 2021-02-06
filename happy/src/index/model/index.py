def show_homepage():
    with open('./happy/public/index.html') as f:
        index_html = f.read()
    return index_html
