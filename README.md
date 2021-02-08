# HAppy 🙃
A **H**ttp **Ap**plication in **Py**thon - or an attempt to create a minimalistic web framework.

This is a work in progress pet project that implements:
  * an http handler that responds to GET requests (running on python's BaseServer) 
  * a simple routing logic that the handler passes the request url to 
  * the routing logic maps the request to the related business logic 
  * the business logic just returns static html so far

Eventually there will be:
  * image responses
  * improved test infrastructure
  * a simple templating engine to generate HTML dynamically
  * responses to POST requests
  * asynchronous http handling
  * authentication handling

## Usage
Start the http server on your local with
```
$ python happy.py
```
Then in your browser visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

By doing so, you are sending the first http request to your running server.
The response will be:

<img width="1023" alt="Screenshot 2021-02-08 at 13 53 57" src="https://user-images.githubusercontent.com/23189414/107222362-1ab72600-6a15-11eb-90f3-86101912776a.png">

Press the `Get Started` button and find a short documentation on how to create and use routes in HAppy.

### Note
A http server is a process that is running on your machine and does two things:

  * Listen for incoming http requests on a specific TCP socket address (composed of an IP address and a port number)
  * Handle the request and sends a response back to the client.

For now, the incoming requests are solely GET requests, the responses are HTML, CSS and image files.

You could also start a built-in Python http server without any coding:
```
$ python3 -m http.server 8080
```
but then you could not have a customised http handler.

## How to test
```
$ venv/bin/pytest -vvv
```

## Author Contact
[alexandra.julius@gmail.com](mailto:alexandra.julius@gmail.com)

