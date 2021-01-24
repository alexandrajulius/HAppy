# HAppy 🙃
A **H**ttp **Ap**plication in **Py**thon - or an attempt to create a minimalistic web framework.

This is a work in progress pet project that provides
  * a server running a http handler that responds to GET requests with static HTML

Eventually there will be
  * responses to POST requests
  * a simple routing logic 
  * dynamic HTML generation
  * asynchronous http handling
  * authentication handling

## Usage
Start the http server on your local with
```
$ python happy.py
```
Then in your browser visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

An http server is a process that is running on your machine and does two things:

  * Listen for incoming http requests on a specific TCP socket address (composed of an IP address and a port number)
  * Handle the request and sends a response back to the client.

For now the incoming requests are solely GET requests, the responses are HTML and image files.

### Note
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

