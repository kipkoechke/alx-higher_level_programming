![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python - Network #0

![meme](http://www.quickmeme.com/img/6a/6ac5d6205b48a3387e6013d4c2bbeb6e778cd422df3d26ecb54c8f78726f5e04.jpg)

## Intro

In this networking project, I used `curl` in Bash scripts to send various types
of HTTP headers. In the process, I learned about how URL's work, domain names,
the many different HTTP request/repsonse header fields and status codes, and
how to utilize cookies.

Task six was an algorithm challenge separate from the overall project theme
completed in Python.

## Resources

**Read or Watch**:

1. [HTTP(Hyper Text Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)(except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
2. [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Learning objectives

By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) **Without the help of Google**

### General

- [x] What a URL is
- [x] What HTTP is
- [x] How to read a URL
- [x] The scheme for a HTTP URL
- [x] What a domain name is
- [x] What a sub-domain is
- [x] How to define a port number in a URL
- [x] What a query string is
- [x] What an HTTP request is
- [x] What an HTTP response is
- [x] What HTTP headers are
- [x] What the HTTP message body is
- [x] What an HTTP request method is
- [x] What an HTTP response status code is
- [x] What an HTTP Cookie is
- [x] How to make a request with cURL
- [x] What happens when you type google.com in your browser (Application level)

## Quiz

[Quizes](./quiz.md)

## Tests :heavy_check_mark:

- [tests](./tests): Folder of test files. Provided by ALX.

## Tasks :page_with_curl:

NOTE: The `curl` behavior in all Bash scripts were written to interact with a
server set up on a container provided by ALX.

- **0. cURL body size**

  [0-body_size.sh](./0-body_size.sh): Bash script that sends a `GET` request to
  a given URL and displays the size of the response body in bytes.

* **1. cURL to the end**

  - [1-body.sh](./1-body.sh): Bash script that sends a `GET` request to a given
    URL and displays the response body for a `200` status code response.

* **2. cURL Method**

  - [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to
    a given URL and displays the response body.

* **3. cURL only methods**

  - [3-methods.sh](./3-methods.sh): Bash script that displays all HTTP methods
    the server of a given URL will accept.
