# HAppy 
A **H**ttp **Ap**plication in **Py**thon. ![happy](https://user-images.githubusercontent.com/23189414/105613130-e9a5e700-5dc0-11eb-83fc-23245174fdb5.png)

Work in progress pet project that provides
  * a server running a http handler that can respond to GET requests

Eventually there will be
  * responses to POST request
  * a simple routing logic
  * asynchronous http handling
  * authentication handling

## Usage
Start the http web server on your local with
```
python happy.py
```
Then in your browser visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

An http web server is a process that is running on your machine and does two things:

  * Listen for incoming http requests on a specific TCP socket address (composed of an IP address and a port number)
  * Handle the request and sends a response back to the client.

For now the incoming requests are solely GET requests, the responses are HTML files.

### Note
You could also start a Python web server without any coding doing
```
python3 -m http.server 8080
```
but then you could not have a customised http handler.

## How to test
```
$ venv/bin/pytest -vvv
```

## Author Contact
[alexandra.julius@gmail.com](mailto:alexandra.julius@gmail.com)

