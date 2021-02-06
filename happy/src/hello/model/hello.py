def say_hello():
    with open('./happy/public/hello/hello.html') as f:
        hello_html = f.read()
    return hello_html
